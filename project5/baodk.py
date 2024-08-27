from os import rename
from datetime import datetime
from csv import DictWriter, DictReader
from json import loads
from urllib.parse import quote, urlencode
from urllib3 import disable_warnings
from urllib3.util import Url
from urllib3.exceptions import InsecureRequestWarning
from html import unescape
import re
from requests import Session
from bs4 import BeautifulSoup, Tag

def flatten_dict(dd, separator='>', prefix=''):
	stack = [(dd, prefix)]
	flat_dict = {}
	
	while stack:
		cur_dict, cur_prefix = stack.pop()
		for key, val in cur_dict.items():
			new_key = cur_prefix + separator + key if cur_prefix else key
			if isinstance(val, dict):
				stack.append((val, new_key))
			else:
				flat_dict[new_key] = val
					
	return flat_dict

def get_csv_headers(filename):
	try:
		with open(filename, 'r', encoding='utf8') as f:
			reader = DictReader(f)
			headers = reader.fieldnames
			f.close()
		return headers
	except FileNotFoundError:
		return None

def ts_format():
	return r"%Y-%m-%d %H:%M:%S.%f"

def ts_filename_format():
	return r"%Y%m%d-%H%M%S"

def ts_topdev_posted_format():
	return r"%H:%M:%S %d-%m-%Y"

def get_timestamp(format=ts_format()):
	return datetime.now().strftime(format)

def new_dict(keys, values):
	d = {}
	for k, v in zip(keys, values):
		d[k] = v
	return d

def match_headers(headers1, headers2):
	if headers1 is None:
		return headers2, True
	if set(headers1) == set(headers2):
		return headers1, False
	addingHeaders = list(set(headers2) - set(headers1))
	removingHeaders = list(set(headers1) -  set(headers2))
	if len(addingHeaders)==0 and len(removingHeaders)==0:
		return headers1, False
	headers = headers1 + addingHeaders
	return [ h for h in headers if h not in removingHeaders], True


def create_csv_writer(filename:str , headers):
	columns = get_csv_headers(filename)
	fieldnames, needRewrite = match_headers(columns, headers)
	if needRewrite and columns is not None:
		bakFileName = f"{'.'.join(filename.split('.')[:-1])}_{get_timestamp(ts_filename_format())}.csv"
		rename(filename, bakFileName)
	f = open(filename, 'a', newline='', encoding='utf8')
	writer = DictWriter(f, fieldnames=fieldnames)
	if needRewrite:
		writer.writeheader()
	return writer, f

class Job:
	def __init__(self, **kwargs):
		for kw, val in kwargs.items():
			setattr(self, kw, val)

	def is_used_api(self):
		return hasattr(self, 'api')

class TopdevJob(Job):
	dns = "topdev.vn"
	search_path = "it-jobs"
	api = Url(scheme="https", host="api.topdev.vn", path="/td/v2/jobs")
	api_query = {"fields[job]":"job_types_str,slug,id,title,company,job_levels_str,published,skills_str,addresses,content", "page_size": 20, "locale": "en_US", "ordering": "newest_job"}
	link_format = "detail-jobs/{slug}-{id}"
	page_query_name = "page"
	jobTypeItems = { 'remote': 'remote-kt1623'
						, 'in-office': 'in-office-kt8792'
						, 'hybrid': 'hybrid-kt8642'
						, 'oversea': 'oversea-kt1625'
	}
	jobDetailItems = 	{ 'Job title': 'title'
							, 'Company name': 'company>display_name'
							, 'Job level': 'job_levels_str'
							, 'Location': 'addresses>full_addresses'
							, 'Job types': 'job_types_str' 
							, 'Job description': 'content'
							, 'Skills': 'skills_str'
							, 'Date posted': 'published>datetime'}
	jobDetailWays = 	{ 'Job description': 'select'
							, 'Skills': 'select'}
	
	def get_search_api(self, **job_type):
		if not job_type.keys():
			if self.api_query.get("job_types_ids") is not None:
				del self.api_query["job_types_ids"]
			api = Url(scheme=self.api.scheme,host=self.api.host,path=self.api.path,query=urlencode(self.api_query))
			return api.url, True
		jobTypesIds = []
		for jTKey, jTVal in job_type.items():
			if not jTVal:
				continue
			val = self.jobTypeItems.get(jTKey.replace('_', '-'))
			if not val:
				del job_type[jTKey]
				continue
			jobTypesIds.append(val[-4:])
		self.api_query["job_types_ids"]=','.join(jobTypesIds)
		api = Url(scheme=self.api.scheme,host=self.api.host,path=self.api.path,query=urlencode(self.api_query))
		return api.url, True

	def get_search_paths(self, **job_type):
		if not job_type.keys():
			return list(map(lambda x: '/'.join(['', self.search_path, x]), self.jobTypeItems.values()))
		searchPaths = []
		for kw in job_type.keys():
			path = self.jobTypeItems.get(kw.replace('_', '-'))
			if path is None:
				del job_type[kw]
				continue
			searchPaths.append('/'.join(['', self.search_path, path]))
		return searchPaths

	@classmethod
	def is_thumbnail_job(cls, tag: Tag):
		if tag.name != 'li':
			return False
		if not tag.parent:
			return False
		_tag = tag.find_parent('ul', class_='mt-4')
		if not _tag:
			return False
		_maintag = _tag.fetchParents(id='tab-job')
		return _maintag
	

class ItVietJob(Job):
	dns = 'itviec.com'
	search_path = 'it-jobs'

class JobHub:
	def __init__(self, job_class):
		self.jobClass = job_class
		self.jobClassInstance = self.jobClass()
		self.baseUrl = 'https://' + getattr(self.jobClassInstance, 'dns')
		self.jobSlug = '/' + getattr(self.jobClassInstance, 'search_path')

	def set_job_slug(self, job_slug):
		self.jobSlug = job_slug

	def path_built(self, slug=None, query_params=None):
		_slug = self.jobSlug if slug is None else unescape(slug)
		if _slug[0]!='/':
			_slug = '/' + _slug
		if query_params is None:
			return f"{self.baseUrl}{_slug}"
		return f"{self.baseUrl}{_slug}"
	
	def get_search_slugs(self, **kwargs):
		if self.jobClassInstance.is_used_api():
			return [self.jobClassInstance.get_search_api(**kwargs)]
		return [(self.path_built(slug=p), False) for p in self.jobClassInstance.get_search_paths(**kwargs)]

	def is_thumnailjob_func(self):
		return self.jobClass.is_thumbnail_job

	def get_jobdetailproperties(self):
		items = self.jobClassInstance.jobDetailItems
		ways = self.jobClassInstance.jobDetailWays
		for kw in items.keys():
			w = ways.get(kw)
			if w is None:
				ways[kw]='select_one'
		return items, ways

	def get_jobs_api(self, json_content):
		jsonJobs = loads(json_content)
		jobList = jsonJobs.get('data')
		jobs = []
		props, _ = self.get_jobdetailproperties()
		for j in jobList:
			jobDict = flatten_dict(j)
			jobInfo = {"Job link": self.path_built(self.jobClassInstance.link_format.format(**jobDict))}
			for prop, kw in props.items():
				info = jobDict.get(kw, '')
				if isinstance(info, str):
					if prop=='Date posted':
						info = datetime.strptime(info, ts_topdev_posted_format()).strftime(ts_format())
					jobInfo[prop] = info
				elif isinstance(info, list):
					jobInfo[prop] = ';'.join(info)
				else:
					jobInfo[prop] = str(info)
			jobs.append(jobInfo)
		return jobs

	def get_jobs(self, html_content):
		jobs = []
		soup = BeautifulSoup(html_content, "html.parser")
		jobList = soup.find_all(self.is_thumnailjob_func())
		props, pways = self.get_jobdetailproperties()
		for job in jobList:
			anchor = job.find('a')
			if not anchor:
				continue
			url = self.path_built(anchor.get('href'))
			# print(url)
			jobInfo = {'Job link': url}
			for prop, propSelector in props.items():
				selectFunc = getattr(anchor, pways.get(prop))
				element:Tag = selectFunc(propSelector)
				if element:
					if isinstance(element, list):
						jobInfo[prop]='; '.join([e.text for e in element])
					else:
						jobInfo[prop]=element.text
			jobs.append(jobInfo)
		return jobs


class JobCrawler:
	def __init__(self):
		self.hubs = { 'topdev': JobHub(TopdevJob)
						, 'itviec': JobHub(ItVietJob) }
	
	def get_hub(self, hub_key):
		return self.hubs.get(hub_key)
	
	def execute_parsing(self, session, url, parse_func):
		resptext = session.get(url).text
		rowdicts = parse_func(resptext)
		headers = rowdicts[0].keys()
		writer, f = create_csv_writer(f'{quote(url, safe='')[:32]}.csv', headers)
		writer.writerows(rowdicts)
		f.close()

	def all_jobs(self, hub_key):
		hub = self.get_hub(hub_key)
		ss = Session()
		ss.verify = False
		for url, isUsedApi in hub.get_search_slugs():
			if isUsedApi:
				self.execute_parsing(ss, url, hub.get_jobs_api)
			else:
				self.execute_parsing(ss, url, hub.get_jobs)
			
def main():
	
	crawl = JobCrawler()
	disable_warnings(InsecureRequestWarning)
	crawl.all_jobs('topdev')

if __name__ == '__main__':
	main()