from os import rename
from datetime import datetime
from time import sleep
from csv import DictWriter, DictReader
from threading import Thread, Event
from queue import Queue, Empty
from bs4 import BeautifulSoup
from requests import get
from urllib3 import disable_warnings, exceptions


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
	f = open(filename, 'a', newline='')
	writer = DictWriter(f, fieldnames=fieldnames)
	if needRewrite:
		writer.writeheader()
	return writer, f

def get_request(url):
	return get(url = url, verify=False)

def parse_tag(tag):
	if tag.string:
		return tag.string
	tagChildren = tag.findChildren(recursive=False)
	if len(tagChildren)==0 and len(tag.text)>0:
		return tag.text
	childtag = [c for c in tagChildren if len(c.text)>0]
	if len(childtag)==0 and len(tag.text)>0:
		return tag.text
	texts = [parse_tag(t) for t in childtag]
	texts = [t for t in texts if t]
	if len(texts) == 0:
		return None
	return texts[0]

def parse_table_html(html_body, timestamp, allowed_coin_names):
	soup = BeautifulSoup(html_body, "html.parser")
	mainTbl = soup.find("table")
	tblRows = mainTbl.find_all("tr")[:5]
	tblHeaderElements = tblRows.pop(0).find_all("th")[3:-2]
	tblHeaders = ["Crypto Name"]
	tblHeaders.extend([h.text for h in tblHeaderElements])
	tblHeaders.append("Timestamp")
	rows = []
	for tblRow in tblRows:
		row = [parse_tag(td) for td in tblRow.find_all("td")[2:-2]]
		if row[0] in allowed_coin_names:
			row.append(timestamp)
			rows.append(row)
	return tblHeaders, rows

def scraper():
	fileName = "coinmarketcapdotcom.csv"
	baseUrl = "https://coinmarketcap.com/"
	allowedCoinNames = ["Bitcoin", "Ethereum", "BNB"]
	
	stopEvent = Event()
	disable_warnings(exceptions.InsecureRequestWarning)
	queue=Queue()
	def worker():
		while not stopEvent.is_set():
			try:
				urlItem = queue.get(timeout=1)
				if urlItem is None:
					continue
				response = get_request(urlItem)
				tsNow = get_timestamp()
				if response and response.status_code == 200:
					headers, rows = parse_table_html(response.text, tsNow, allowedCoinNames)
					writer, file = create_csv_writer(fileName, headers)
					columnWidths = [len(h) for h in headers]
					for row in rows:
						columnWidths = [max(o, len(c)) for o, c in zip(columnWidths, row)]
						writer.writerow(new_dict(headers, row))
					file.close()
					formattedHeaders = "|".join([" {:^{width}} ".format(h, width=colWidth) for h, colWidth in zip(headers, columnWidths)])
					print(formattedHeaders)
					print("="*len(formattedHeaders))
					formattedRows = "\r\n".join(["|".join([" {:<{width}} ".format(cell, width=colWidth) for cell, colWidth in zip(row, columnWidths)]) for row in rows])
					print(formattedRows)
					print("Extracted data successully at {}\r\n".format(tsNow))
				else:
					print("Failed to retrieve or parse the page.")
				queue.task_done()
			except Empty:
				continue
	
	thread = Thread(target=worker, daemon=True)
	thread.start()
	try:
		while not stopEvent.is_set():
			queue.put(baseUrl)
			sleep(10)
	except Exception:
		stopEvent.set()
		
	queue.join()
	thread.join()

if __name__ == '__main__':
	scraper()