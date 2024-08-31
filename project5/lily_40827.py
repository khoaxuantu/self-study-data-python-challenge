#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Great work! But seems like you did not implement the filter and mail features.
# I also commented on the code, please find NOTE: to see the comments.

import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import re
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Set up the Selenium WebDriver
def get_data_source(url):
    driver = webdriver.Chrome()
    driver.get(url)
    SCROLL_PAUSE_TIME = 2
    try:
        close_button = driver.find_element(
            By.XPATH, '//*[@id="btn-close-new-year-modal"]'
        )
        close_button.click()
        time.sleep(1)  # Wait a moment after closing the ad
    except:
        print("No advertisement to close or the SVG element wasn't found.")
    # Get initial page height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page
        time.sleep(7)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # After scrolling, get the page source
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # Close the browser
    driver.quit()
    return soup


# In[2]:


# Create table

base_url = "https://topdev.vn"
soup = get_data_source("https://topdev.vn/viec-lam-it")
table_column_titles = [
    "Job Title",
    "Company Name",
    "Job Location",
    "Job Description",
    "Date Posted",
    "Job Link",
    "Experience",
    "Level",
    "Job Type",
    "Contract Type",
    "Tech Stack",
]
dm = pd.DataFrame(columns=table_column_titles)


# Create function scrapping job_details from a link
def automated_job_data_pull(x):
    job_details = requests.get(x)
    soup2 = BeautifulSoup(job_details.text, features="html.parser")
    # Job filter:
    filter_general = soup2.find(
        "div",
        class_="container flex flex-wrap items-start gap-6 px-0 md:flex-nowrap md:px-4",
    )
    # Tech Stack Keyword
    tech_stack_filter = filter_general.find("div", class_="flex flex-wrap gap-y-2")
    tech_stack = []
    for skill in tech_stack_filter:
        tech_stack.append(skill.text)
    # Another keywords
    information = filter_general.find("div", class_="flex flex-wrap")
    data = [a.text.strip() for a in information.find_all("a")]
    experience, level, job_type, contract_type = (data + ["N/A"] * 4)[:4]

    # Job details
    job_title = soup2.find("h1", class_="text-2xl font-bold text-black").text.strip()
    job_name = soup2.find(
        "p", class_="my-1 line-clamp-1 text-base font-bold text-gray-500"
    ).text.strip()
    job_location = soup2.find(
        "div", class_="my-2 max-w-[540px] text-base text-gray-500"
    ).text.strip()
    job_des = soup2.find("div", id="JobDescription").text.strip()
    job_posted = soup2.find(
        "div", class_="mb-2 max-w-[540px] text-base text-gray-500"
    ).text.strip()
    # Get current date and time
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_posted = job_posted + " since " + date_time
    job_link = x
    # Determine the next index
    dm.loc[len(dm)] = {
        "Job Title": job_title,
        "Company Name": job_name,
        "Job Location": job_location,
        "Job Description": job_des,
        "Date Posted": date_posted,
        "Job Link": job_link,
        "Experience": experience,
        "Level": level,
        "Job Type": job_type,
        "Contract Type": contract_type,
        "Tech Stack": tech_stack,
    }


m1 = soup.find_all("li", class_="mb-4 last:mb-0")
job_links = []
for job in m1:
    m2 = job.find_all("a", href=True)
    if len(m2) <= 0:
        continue
    link = m2[1]["href"]
    if link.startswith("/vi/"):
        clean_link = link[3:]
    else:
        clean_link = link
    link = base_url + clean_link
    automated_job_data_pull(link)
dm
dm.to_csv("Project_5.csv")


# In[ ]:


num_criteria = int(input("How many criteria do you want to filter: "))
filter = {}
for i in range(num_criteria):
    print(f"Criteria {i+1}: ")
    column = input(f"Please choose column you want to filter:{dm.columns.tolist()} ")
    type_of_filter = input(
        "Type of filter ? include keyword (I) or exclude keywords (E)"
    )
    num_keywords = int(input("How many keyword "))
    keywords = []
    for j in range(num_keywords):
        keyword = input(f"Enter keyword {j+1}: ")
        keywords.append(keyword)
    key = "|".join(keywords)
    # Store the filter criteria in the dictionary
    if type_of_filter == "I":
        filter[column] = (key, "include")
    elif type_of_filter == "E":
        filter[column] = (key, "exclude")
    filter[column] = key

# Copy the original DataFrame for filtering
filter_dm = dm.copy()
# Apply the filters to the DataFrame
for column, (key, type_of_filter) in filter.items():
    if type_of_filter == "I":
        filter_dm = filter_dm[
            filter_dm[column].str.contains(key, case=False, na=False, regex=True)
        ]
    elif type_of_filter == "E":
        filter_dm = filter_dm[
            ~filter_dm[column].str.contains(key, case=False, na=False, regex=True)
        ]

# Save the filtered DataFrame to a CSV file
output_file = input("Enter the output file name (including '.csv'): ")
filter_dm.to_csv(output_file, index=False)
print(f"The results have been saved in {output_file}.")


# In[ ]:


def scrape_jobs_from_page(page_url):
    soup = get_data_source(page_url)
    table_column_titles = [
        "Job Title",
        "Company Name",
        "Job Location",
        "Job Description",
        "Date Posted",
        "Job Link",
        "Experience",
        "Level",
        "Job Type",
        "Contract Type",
        "Tech Stack",
    ]
    df = pd.DataFrame(columns=table_column_titles)
    # Extract job listings from the current page
    m1 = soup.find_all("li", class_="mb-4 last:mb-0")
    for job in m1:
        m2 = job.find_all("a", href=True)
        if len(m2) <= 0:
            continue
        link = m2[1]["href"]
        if link.startswith("/vi/"):
            clean_link = link[3:]
        else:
            clean_link = link
        link = base_url + clean_link
        automated_job_data_pull(link)
    output_file = input("Enter the output file name (including '.csv'): ")
    df.to_csv(output_file, index=False)
    print(f"The results have been saved in {output_file}.")


# Example URL with pagination (you'll need to adjust this to fit the site's URL structure)
def job():
    base_url = "https://topdev.vn/viec-lam-it?page="
    all_job_links = []
    # NOTE: should also handle the case where page does not exist
    for page_number in range(1, 6):
        page_url = f"{base_url}{page_number}"
        df = scrape_jobs_from_page(page_url)
        all_job_links.extend(df["Job Link"].tolist())
    filtered_df = pd.DataFrame(columns=table_column_titles)
    for link in all_job_links:
        automated_job_data_pull(link, filtered_df)
    filtered_df.to_csv("filtered_job_listings.csv", index=False)


import schedule
import time

schedule.every().day.at("09:00").do(job)
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute between checks
