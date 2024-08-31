import scrapy
import requests
import json
import re
from datetime import datetime
import pandas as pd
from urllib.parse import urlencode
from bs4 import BeautifulSoup  # Import BeautifulSoup

# Discord channel webhook URL to send notifications
# Really, you hardcoded the webhook URL in the code? Please don't do this in production code. And also you should let the users know about this in the README file.
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/<WEBHOOK_URL_MASK>"
# File name to save data into a spreadsheet
SPREADSHEET_FILE = "job_listings.xlsx"


class DataJobsSpider(scrapy.Spider):
    name = "data_jobs_spider"

    def __init__(self, *args, **kwargs):
        super(DataJobsSpider, self).__init__(*args, **kwargs)
        # Get the list of keywords and locations from input parameters
        self.keyword_list = kwargs.get("keywords", ["Data Intern"])
        self.location_list = kwargs.get("locations", ["Hanoi"])
        # List to store job data
        self.job_data = []

    def get_job_search_url(self, keyword, location, offset=0):
        # Create job search URL based on keyword, location, and offset
        parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
        return {
            "indeed": "https://jobs.vn.indeed.com/jobs?" + urlencode(parameters),
        }[self.job_board]

    def start_requests(self):
        # Start requests for each keyword and location
        for keyword in self.keyword_list:
            for location in self.location_list:
                for job_board in ["indeed", "topdev", "itviec", "jobstreet"]:
                    self.job_board = job_board
                    search_url = self.get_job_search_url(keyword, location)
                    yield scrapy.Request(
                        url=search_url,
                        callback=self.parse_search_results,
                        meta={
                            "keyword": keyword,
                            "location": location,
                            "offset": 0,
                            "job_board": job_board,
                        },
                    )
        # Send notification when spider starts
        self.notify_discord("Data Jobs Spider has started.")

    def parse_search_results(self, response):
        # Parse search results from the response
        job_board = response.meta["job_board"]
        location = response.meta["location"]
        keyword = response.meta["keyword"]
        offset = response.meta["offset"]

        if job_board == "indeed":
            # Find and parse job data from script tag
            script_tag = re.findall(
                r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});',
                response.text,
            )
            if script_tag:
                json_blob = json.loads(script_tag[0])
                jobs_list = json_blob["metaData"]["mosaicProviderJobCardsModel"][
                    "results"
                ]
                if jobs_list:
                    for job in jobs_list:
                        self.logger.info("Job data: %s", job)

                        # Only get jobs with 'intern' or 'junior' in the title
                        job_title = job.get("title", "").lower()
                        if "intern" in job_title or "junior" in job_title:
                            posted_date_timestamp = job.get("pubDate", 0)
                            posted_date = datetime.fromtimestamp(
                                posted_date_timestamp / 1000
                            ).strftime("%Y-%m-%d %H:%M:%S")

                            # Process job description
                            job_description = (
                                job.get("jobdescription")
                                or job.get("description")
                                or job.get("snippet", "N/A")
                            )

                            # Remove HTML tags from job description
                            soup = BeautifulSoup(job_description, "html.parser")
                            job_description = soup.get_text(separator=" ", strip=True)

                            # Create Discord notification message
                            job_message = (
                                f"**{job.get('title')}**\n"
                                f"**Company:** {job.get('company')}\n"
                                f"**Location:** {job.get('jobLocationCity')}, {job.get('jobLocationState')}\n"
                                f"**Estimated Salary:** {job.get('estimatedSalary', {}).get('min', 'N/A')} - {job.get('estimatedSalary', {}).get('max', 'N/A')}\n"
                                f"**Posted Date:** {posted_date}\n"
                                f"**Job Link:** https://www.indeed.com/viewjob?jk={job.get('jobkey')}\n"
                                f"**Job Description**: {job_description}\n"
                                f"--------------------------------------------------------"
                            )
                            # Send notification to Discord and store data
                            self.notify_discord(job_message)
                            self.job_data.append(
                                {
                                    "Job Title": job.get("title"),
                                    "Company": job.get("company"),
                                    "Location": f"{job.get('jobLocationCity')}, {job.get('jobLocationState')}",
                                    "Estimated Salary": f"{job.get('estimatedSalary', {}).get('min', 'N/A')} - {job.get('estimatedSalary', {}).get('max', 'N/A')}",
                                    "Posted Date": posted_date,
                                    "Job Link": f"https://www.indeed.com/viewjob?jk={job.get('jobkey')}",
                                    "Job Description": job_description,
                                }
                            )

                # Handle pagination if applicable
                if offset == 0:
                    meta_data = json_blob["metaData"]["mosaicProviderJobCardsModel"][
                        "tierSummaries"
                    ]
                    num_results = sum(category["jobCount"] for category in meta_data)
                    if num_results > 1000:
                        num_results = 50

                    for new_offset in range(10, num_results + 10, 10):
                        url = self.get_job_search_url(keyword, location, new_offset)
                        yield scrapy.Request(
                            url=url,
                            callback=self.parse_search_results,
                            meta={
                                "keyword": keyword,
                                "location": location,
                                "offset": new_offset,
                                "job_board": job_board,
                            },
                        )

    def closed(self, reason):
        # Send notification when spider is completed and save data to spreadsheet
        self.notify_discord("Data Jobs Spider has finished: " + reason)
        self.save_to_spreadsheet()

    def notify_discord(self, message):
        # Send notification to Discord
        payload = {"content": message}
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            self.logger.info("Notification sent successfully.")
        else:
            self.logger.error(
                f"Failed to send notification, HTTP status code: {response.status_code}"
            )

    def save_to_spreadsheet(self):
        # Save data to Excel file
        df = pd.DataFrame(self.job_data)
        try:
            existing_df = pd.read_excel(SPREADSHEET_FILE)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_excel(SPREADSHEET_FILE, index=False)
