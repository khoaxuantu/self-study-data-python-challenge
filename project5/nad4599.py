# Great work! But seems like u did not implement mail feature.

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from urllib.parse import urljoin
import schedule
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# to run python3 nada_project5.py and add variable to .env DISCORD_WEBHOOK_URL
# Load Discord Webhook URL from environment variable
load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def send_discord_notification(message):
    if DISCORD_WEBHOOK_URL:
        data = {"content": message}
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Discord notification sent successfully.")
        else:
            print(
                f"Failed to send Discord notification. Status code: {response.status_code}"
            )
    else:
        print("Discord Webhook URL is not set.")


# Base URL and target URL
base_url = "https://www.kalibrr.id"
url = "https://www.kalibrr.id/id-ID/home/work_from_home/y"

# DataFrame to store job information
df = pd.DataFrame(
    columns=[
        "job_title",
        "job_position",
        "company_name",
        "location",
        "job_description",
        "job_timestamp_posted",
        "job_link",
    ]
)


def job_scrape(driver):
    global df
    try:
        # Pagination
        load_more_button = driver.find_element(By.CLASS_NAME, "k-btn-primary")
        load_more_button.click()
        time.sleep(3)  # Adjust the sleep time as needed

        # Get the page source and create BeautifulSoup object
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_cards = soup.find_all(
            "div",
            class_="k-font-dm-sans k-rounded-lg k-bg-white k-border-solid k-border hover:k-border-2 hover:k-border-primary-color k-border k-group k-flex k-flex-col k-justify-between css-1otdiuc",
        )

        for job_card in job_cards:
            job_divs_header = job_card.find(
                "div", class_="k-flex-1 k-h-full k-flex k-flex-col k-justify-center"
            )
            job_divs_subheader = job_card.find(
                "div", class_="blur k-flex k-flex-col k-gap-3 k-px-4 k-pb-4"
            )
            job_hover_card = job_card.find(
                "div", class_="k-flex k-gap-4 k-h-full k-justify-center k-items-center"
            )

            # Employment type
            employment_type = job_divs_subheader.find(
                attrs={"itemprop": "employmentType"}
            )
            job_position = job_card.find(
                "a", class_="k-font-dm-sans k-text-xs k-font-bold k-text-gray-600"
            ).get_text()
            pattern = re.compile(r"\bsupervisor\b", re.IGNORECASE)
            if employment_type and pattern.search(job_position):
                employment_type_text = employment_type.get_text(strip=True)
                if not re.search(r"\bFULL_TIME\b", employment_type_text):
                    continue  # Skip this job if it's not full-time
            else:
                continue

            # Job title
            job_title_h2 = job_divs_header.find(
                attrs={"data-tooltip-id": "job-title-tooltip-[object Object]"}
            )
            if job_title_h2:
                job_title_a = job_title_h2.find("a")
                job_title_text = (
                    job_title_a.get_text(strip=True) if job_title_a else "N/A"
                )
            else:
                job_title_text = "N/A"

            # Company name
            job_company_name_span = job_divs_header.find(
                "span", class_="k-inline-flex k-items-center k-mb-1"
            )
            if job_company_name_span:
                job_company_name_a = job_company_name_span.find("a")
                job_company_name_text = (
                    job_company_name_a.get_text(strip=True)
                    if job_company_name_a
                    else "N/A"
                )
            else:
                job_company_name_text = "N/A"

            # Job location
            job_location_span = job_divs_subheader.find(
                "span", class_="k-text-gray-500 k-block k-pointer-events-none"
            )
            job_location_text = (
                job_location_span.get_text(strip=True) if job_location_span else "N/A"
            )

            # Job link
            job_link = job_hover_card.find(
                "a",
                class_="k-w-36 k-text-center k-btn-primary k-bg-white k-text-primary-color",
            ).get("href")
            full_url = urljoin(base_url, job_link)

            # Visit detail page
            job_detail_page = requests.get(full_url)
            job_detail_page_soup = BeautifulSoup(job_detail_page.content, "html.parser")

            # Job timestamp posted
            job_timestamp_posted = job_detail_page_soup.find(
                attrs={"itemprop": "datePosted"}
            )
            if job_timestamp_posted:
                job_timestamp_posted = job_timestamp_posted.get_text(strip=True)
                try:
                    dt = datetime.fromisoformat(job_timestamp_posted)
                    formatted_job_timestamp_posted = dt.strftime("%d-%m-%Y %H:%M:%S")
                except ValueError:
                    formatted_job_timestamp_posted = "N/A"
            else:
                formatted_job_timestamp_posted = "N/A"

            # Job description
            job_descriptions = job_detail_page_soup.find(
                attrs={"itemprop": "description"}
            )
            job_description_text = "N/A"
            if job_descriptions:
                job_description_texts = [
                    desc.get_text(strip=True) for desc in job_descriptions.find_all("p")
                ]
                job_description_text = ", ".join(job_description_texts)

            # Save to DataFrame
            df.loc[len(df)] = [
                job_title_text,
                job_position,
                job_company_name_text,
                job_location_text,
                job_description_text,
                formatted_job_timestamp_posted,
                full_url,
            ]

        # Generate timestamp for filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"job_listings_{timestamp}.csv"

        # Check if DataFrame has any rows
        if not df.empty:
            send_discord_notification(
                f"New job listings have been scraped and saved to {filename}."
            )

        # Save DataFrame to CSV file
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Setup WebDriver
driver = webdriver.Chrome()

# Open URL with Selenium
driver.get(url)

# Initial scrape
job_scrape(driver)

# Schedule the scraping job every 5 minutes
schedule.every(5).minutes.do(job_scrape, driver)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
