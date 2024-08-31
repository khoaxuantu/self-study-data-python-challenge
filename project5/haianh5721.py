# Great work! But I think u have not implemented any features in bonus points session.

import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime


def scrape_itviec(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("div", class_="job_content")

    job_listings = []

    for job in jobs:
        title = job.find("h3", class_="title").text.strip()
        company = job.find("div", class_="company-name").text.strip()
        location = job.find("div", class_="city").text.strip()
        description = job.find("div", class_="description").text.strip()
        date_posted = job.find("div", class_="posted-date").text.strip()
        job_link = "https://itviec.com" + job.find("a", class_="job_link")["href"]

        job_listings.append(
            {
                "title": title,
                "company": company,
                "location": location,
                "description": description,
                "date_posted": date_posted,
                "job_link": job_link,
            }
        )

    return job_listings


def filter_jobs(job_listings, include_keywords, exclude_keywords):
    filtered_jobs = []

    for job in job_listings:
        include_match = any(
            re.search(keyword, job["description"], re.IGNORECASE)
            for keyword in include_keywords
        )
        exclude_match = any(
            re.search(keyword, job["description"], re.IGNORECASE)
            for keyword in exclude_keywords
        )

        if include_match and not exclude_match:
            filtered_jobs.append(job)

    return filtered_jobs


def save_to_csv(job_listings, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "title",
            "company",
            "location",
            "description",
            "date_posted",
            "job_link",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in job_listings:
            writer.writerow(job)


if __name__ == "__main__":
    url = "https://itviec.com/it-jobs"
    include_keywords = ["python", "javascript", "remote"]
    exclude_keywords = ["internship", "part-time"]

    job_listings = scrape_itviec(url)
    filtered_jobs = filter_jobs(job_listings, include_keywords, exclude_keywords)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"job_listings_{timestamp}.csv"
    save_to_csv(filtered_jobs, filename)

    print(f"Scraped and filtered {len(filtered_jobs)} jobs. Saved to {filename}")
