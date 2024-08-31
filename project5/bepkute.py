#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Great work! I did comment on the code. Please check the comments and let me know if you have any questions.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime
import time
import logging
import os


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_job_listings(url):
    job_elements = []
    while url:
        print(url)
        try:
            response = requests.get(url)
            response.encoding = "utf-8"
            soup = BeautifulSoup(response.text, "html.parser")
            job_elements.extend(soup.find_all("li", class_="mb-4 last:mb-0"))

            # U did try to implement the pagination, but it's not working with your input website :D. The reason is topdev website uses a method called "infinite scroll" to load more job listings. So, the pagination is not working here. And if the page does not use "a" tag for the "Next" button, you can't get the next page link.
            # You can use Selenium to scrape this type of website.
            next_page = soup.find("a", {"aria-label": "Next"})
            url = "https://topdev.vn" + next_page["href"] if next_page else None
            print(url)

            time.sleep(1)
        except requests.RequestException as e:
            logging.error(f"Request error fetching job listings: {e}")
            break
        except Exception as e:
            logging.error(f"Error fetching job listings: {e}")
            break
    return job_elements


def fetch_job_details(link):
    try:
        response = requests.get(link)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        job_type_element = soup.find(
            "div", class_="item-card-info mb-2 w-1/2 md:mb-4 md:w-full"
        )
        job_type = job_type_element.get_text(strip=True) if job_type_element else "N/A"

        contract_type_element = soup.find(
            "div", class_="item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0"
        )
        contract_type = (
            contract_type_element.get_text(strip=True)
            if contract_type_element
            else "N/A"
        )

        contract_type = re.sub(r"^Cấp bậc", "", contract_type).strip()

        tech_stack_element = soup.find("div", class_="item-card-info mb-4")
        tech_stack = (
            ", ".join(
                [tech.get_text(strip=True) for tech in tech_stack_element.find_all("a")]
            )
            if tech_stack_element
            else "N/A"
        )

        return job_type, contract_type, tech_stack
    except requests.RequestException as e:
        logging.error(f"Request error fetching job details: {e}")
        return "N/A", "N/A", "N/A"
    except Exception as e:
        logging.error(f"Error fetching job details: {e}")
        return "N/A", "N/A", "N/A"


def parse_job_element(job):
    title_element = job.find("h3", class_="line-clamp-1")
    title = title_element.get_text(strip=True) if title_element else "N/A"

    company_element = (
        job.find("div", class_="mt-1").find("a") if job.find("div", "mt-1") else None
    )
    company = company_element.get_text(strip=True) if company_element else "N/A"

    location_div = job.find(
        "div", class_="flex flex-wrap items-end gap-2 text-gray-500"
    )
    location = (
        ", ".join([loc.get_text(strip=True) for loc in location_div.find_all("p")])
        if location_div
        else "N/A"
    )

    date_element = job.find("p", class_="whitespace-nowrap text-sm text-gray-400")
    date_posted = date_element.get_text(strip=True) if date_element else "N/A"

    link_element = job.find("a", href=True)
    link = "https://topdev.vn" + link_element["href"] if link_element else "N/A"

    return title, link, company, location, date_posted


def main():
    url = "https://topdev.vn/viec-lam-it"
    job_elements = fetch_job_listings(url)

    job_titles = []
    links = []
    companies = []
    locations = []
    dates_posted = []
    job_types = []
    contract_types = []
    tech_stacks = []
    date_nows = []

    for job in job_elements:
        title, link, company, location, date_posted = parse_job_element(job)

        if link == "N/A":
            continue

        job_type, contract_type, tech_stack = fetch_job_details(link)

        job_titles.append(title)
        links.append(link)
        companies.append(company)
        locations.append(location)
        dates_posted.append(date_posted)
        job_types.append(job_type)
        contract_types.append(contract_type)
        tech_stacks.append(tech_stack)

        date_nows.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    new_data = {
        "Title": job_titles,
        "Link": links,
        "Company": companies,
        "Location": locations,
        "Date Posted": dates_posted,
        "Job Type": job_types,
        "Contract Type": contract_types,
        "Tech Stack": tech_stacks,
        "DateNow": date_nows,
    }
    new_df = pd.DataFrame(new_data)

    file_exists = os.path.isfile("filtered_job_listings.csv")

    if file_exists:

        existing_df = pd.read_csv("filtered_job_listings.csv", encoding="utf-8-sig")

        combined_df = pd.concat([existing_df, new_df])

        combined_df.drop_duplicates(
            subset=["Title", "Company"], keep="last", inplace=True
        )

        combined_df.to_csv(
            "filtered_job_listings.csv", index=False, encoding="utf-8-sig"
        )
    else:

        new_df.to_csv(
            "filtered_job_listings.csv",
            mode="w",
            header=True,
            index=False,
            encoding="utf-8-sig",
        )

    logging.info("Data saved to filtered_job_listings.csv with UTF-8 encoding")


if __name__ == "__main__":

    while True:
        main()
        logging.info("Waiting for the next run...")
        # should use other method to perform scheduling tasks, such as schedule, apscheduler, etc.
        time.sleep(24 * 60 * 60)
