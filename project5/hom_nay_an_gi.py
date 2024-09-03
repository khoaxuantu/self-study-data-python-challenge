# Great work! But seems like you didn't implement the filter function as well as bonus point features.

import requests
from bs4 import BeautifulSoup
import re
import csv

# URL of the job board website
url = "https://topdev.vn/"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Define regex patterns for filtering
programming_languages = re.compile(r"\b(Python|JavaScript)\b", re.IGNORECASE)
keywords = re.compile(r"\b(remote|full-time)\b", re.IGNORECASE)
exclude_terms = re.compile(r"\b(internship|part-time)\b", re.IGNORECASE)

# List to store filtered job listings
filtered_jobs = []

# Find all job listings
job_listings = soup.find_all("div", class_="job-listing")

for job in job_listings:
    job_title = job.find("h2", class_="job-title").text.strip()
    company_name = job.find("div", class_="company-name").text.strip()
    job_location = job.find("div", class_="job-location").text.strip()
    job_description = job.find("div", class_="job-description").text.strip()
    date_posted = job.find("div", class_="date-posted").text.strip()
    job_link = job.find("a", class_="job-link")["href"]

    # Apply regex filters
    if (
        programming_languages.search(job_description)
        and keywords.search(job_description)
        and not exclude_terms.search(job_description)
    ):

        filtered_jobs.append(
            {
                "Job Title": job_title,
                "Company Name": company_name,
                "Job Location": job_location,
                "Job Description": job_description,
                "Date Posted": date_posted,
                "Job Link": job_link,
            }
        )

# Save filtered job listings to a CSV file
with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "Job Title",
        "Company Name",
        "Job Location",
        "Job Description",
        "Date Posted",
        "Job Link",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for job in filtered_jobs:
        writer.writerow(job)

print(f"Successfully saved {len(filtered_jobs)} job listings to filtered_jobs.csv")
