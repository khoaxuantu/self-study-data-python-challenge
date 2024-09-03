# Great work! But seems like u did not implement the bonus points.

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_job_listings(url, criteria_regex):
    """
    Scrapes job listings from a website and filters them based on criteria.

    Args:
        url (str): The URL of the job board website.
        criteria_regex (str): Regular expression for filtering job listings.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped job listings.
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    job_listings = []

    # Find all job listing elements (adjust based on website structure)
    job_elements = soup.find_all("div", class_="job-item")

    for job_element in job_elements:
        # Extract job details
        job_title = job_element.find("h3").text.strip()
        company_name = job_element.find("h4").text.strip()
        job_location = job_element.find("span", class_="job-location").text.strip()
        job_description = job_element.find("div", class_="job-description").text.strip()
        date_posted = job_element.find("span", class_="job-date").text.strip()
        job_link = job_element.find("a")["href"]

        # Apply criteria filtering using regular expression
        if re.search(criteria_regex, job_title) or re.search(
            criteria_regex, job_description
        ):
            job_listings.append(
                {
                    "Job Title": job_title,
                    "Company Name": company_name,
                    "Job Location": job_location,
                    "Job Description": job_description,
                    "Date Posted": date_posted,
                    "Job Link": job_link,
                }
            )

    # Create DataFrame from scraped data
    df = pd.DataFrame(job_listings)
    return df


# Example usage
url = "https://topdev.vn/viec-lam-it"
criteria_regex = r"Python|Data Science|Machine Learning"  # Example criteria

# Scrape and filter job listings
df = scrape_job_listings(url, criteria_regex)

# Print the DataFrame
print(df)
df.to_csv("Job_script.csv", index=False)
