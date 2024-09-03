import re
import json
import scrapy
from urllib.parse import urlencode
from datetime import datetime
from w3lib.html import remove_tags
from apscheduler.schedulers.blocking import BlockingScheduler

class IndeedSearchSpider(scrapy.Spider):
    name = "indeed_search"
    custom_settings = {
        'FEEDS': {'data/%(name)s.csv': {'format': 'csv'}}
    }

    def get_indeed_search_url(self, keyword, location, offset=0):
        parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
        return "https://jobs.vn.indeed.com/jobs?" + urlencode(parameters)

    def start_requests(self):
        keyword_list = ['Backend']
        location_list = ['Hanoi']
        for keyword in keyword_list:
            for location in location_list:
                indeed_jobs_url = self.get_indeed_search_url(keyword, location)
                yield scrapy.Request(
                    url=indeed_jobs_url,
                    callback=self.parse_search_results,
                    meta={'keyword': keyword, 'location': location, 'offset': 0}
                )

    def parse_search_results(self, response):
        location = response.meta['location']
        keyword = response.meta['keyword']
        offset = response.meta['offset']

        script_tag = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', response.text)
        if script_tag:
            json_blob = json.loads(script_tag[0])

            jobs_list = json_blob.get('metaData', {}).get('mosaicProviderJobCardsModel', {}).get('results', [])
            for index, job in enumerate(jobs_list):
                job_description = job.get('snippet', '')
                job_title = job.get('title', '')

                job_description_clean = remove_tags(job_description)

                pub_date_unix = job.get('pubDate')
                pub_date = None
                try:
                    if isinstance(pub_date_unix, (int, float)):
                        if pub_date_unix > 1_000_000_000:
                            pub_date_unix /= 1_000
                        pub_date = datetime.utcfromtimestamp(pub_date_unix).strftime('%Y-%m-%d %H:%M:%S')
                except (OSError, ValueError, TypeError):
                    pub_date = 'Invalid Date'

                yield {
                    'keyword': keyword,
                    'location': location,
                    'page': round(offset / 10) + 1 if offset > 0 else 1,
                    'position': index,
                    'company': job.get('company'),
                    'companyRating': job.get('companyRating'),
                    'companyReviewCount': job.get('companyReviewCount'),
                    'highlyRatedEmployer': job.get('highlyRatedEmployer'),
                    'jobkey': job.get('jobkey'),
                    'jobTitle': job_title,
                    'jobLocationCity': job.get('jobLocationCity'),
                    'jobLocationPostal': job.get('jobLocationPostal'),
                    'jobLocationState': job.get('jobLocationState'),
                    'maxSalary': job.get('estimatedSalary', {}).get('max', 0),
                    'minSalary': job.get('estimatedSalary', {}).get('min', 0),
                    'salaryType': job.get('estimatedSalary', {}).get('max', 'none'),
                    'pubDate': pub_date,
                    'jobDescription': job_description_clean
                }

            if offset == 0:
                meta_data = json_blob.get("metaData", {}).get("mosaicProviderJobCardsModel", {}).get("tierSummaries", [])
                num_results = sum(category.get("jobCount", 0) for category in meta_data)
                num_pages = (num_results // 10) + (1 if num_results % 10 else 0)

                for new_offset in range(10, min(num_results, 50) + 10, 10):
                    url = self.get_indeed_search_url(keyword, location, new_offset)
                    yield scrapy.Request(
                        url=url,
                        callback=self.parse_search_results,
                        meta={'keyword': keyword, 'location': location, 'offset': new_offset}
                    )

def schedule_spider():
    scheduler = BlockingScheduler()
    
    # Lên lịch chạy Spider mỗi ngày vào lúc 00:00
    scheduler.add_job(lambda: scrapy.crawl('indeed_search'), 'cron', hour=0, minute=0)
    
    # Bắt đầu chạy scheduler
    scheduler.start()

if __name__ == "__main__":
    schedule_spider()
