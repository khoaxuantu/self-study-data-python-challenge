# Great work! But seems like u did not implement the bonus points.

import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime

URL = "https://itviec.com/jobs"

response = requests.get(URL)
if response.status_code != 200:
    raise Exception("Failed to load page {}".format(URL))

soup = BeautifulSoup(response.text, "html.parser")

job_cards = soup.find_all("div", class_="job")

programming_languages = r"(Python|JavaScript)"
keywords_include = r"(remote|full-time)"
keywords_exclude = r"(internship|part-time)"

filtered_jobs = []

for job in job_cards:
    job_title = job.find("h2", class_="title").text.strip()
    company_name = job.find("div", class_="company-name").text.strip()
    job_location = job.find("div", class_="location").text.strip()
    job_description = job.find("div", class_="description").text.strip()
    job_link = job.find("a", class_="job__link")["href"].strip()
    date_posted = datetime.now().strftime("%Y-%m-%d")

    if (
        re.search(programming_languages, job_description, re.IGNORECASE)
        and re.search(keywords_include, job_description, re.IGNORECASE)
        and not re.search(keywords_exclude, job_description, re.IGNORECASE)
    ):

        filtered_jobs.append(
            {
                "Job Title": job_title,
                "Company Name": company_name,
                "Location": job_location,
                "Description": job_description,
                "Date Posted": date_posted,
                "Link": f"https://itviec.com{job_link}",
            }
        )

csv_file = "filtered_job_listings.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=filtered_jobs[0].keys())
    writer.writeheader()
    writer.writerows(filtered_jobs)

print(f"Saved {len(filtered_jobs)} filtered job listings to {csv_file}")
