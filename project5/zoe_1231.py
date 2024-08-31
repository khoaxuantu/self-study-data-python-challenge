#!/usr/bin/env python
# coding: utf-8

# # Project 05
#
# - Extracting key information
# - Filter the job listings based on skill requirement
# - Export file to CSVlink

# In[14]:

# Great work! But seems like u did not implement the bonus points.

import re
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def automated_job_listing():

    url = "https://topdev.vn/viec-lam-it"
    url_topdev = "https://topdev.vn/"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Lấy Job title
    job_title_columns = soup.find_all(
        "a",
        class_=[
            "text-lg font-bold transition-all hover:text-primary",
            "text-lg font-bold transition-all text-primary",
        ],
    )
    job_title = [column.text for column in job_title_columns]

    # Lấy Company name
    company_name_columns = soup.find_all(
        "a", class_="text-gray-600 transition-all hover:text-primary"
    )
    company_name = [column.text for column in company_name_columns]

    # Lấy Job location
    job_location_columns = soup.find_all(
        "div", class_="flex flex-wrap items-end gap-2 text-gray-500"
    )
    job_location = [column.text for column in job_location_columns]

    # Lấy Job level
    job_level_columns = soup.find_all("p", class_="text-gray-500")
    job_level = [column.text for column in job_level_columns]

    # Lấy Skill requirement
    divs = soup.find_all("div", class_="line-clamp-1")
    skill_groups = [
        [a.text for a in div.find_all("a", class_="mr-2 inline-block")]
        for div in divs
        if div.find_all("a", class_="mr-2 inline-block")
    ]

    # Lấy Date posted
    date_posted_columns = soup.find_all(
        "p", class_="whitespace-nowrap text-sm text-gray-400"
    )
    date_posted = [column.text for column in date_posted_columns]

    # Lấy Job link
    lis = soup.find_all("li", class_="mb-4 last:mb-0")
    job_links = [
        url_topdev + li.find("a", href=True)["href"]
        for li in lis
        if li.find("a", href=True)
    ]

    # Lấy thời gian lấy data
    date_time = datetime.now()

    # Tạo bảng & import data
    data_dict = {
        "Job title": job_title,
        "Company name": company_name,
        "Job location": job_location,
        "Job level": job_level,
        "Skills": skill_groups,
        "Date posted": date_posted,
        "Job link": job_links,
        "TimeStamp": date_time,
    }

    df = pd.DataFrame(data_dict)

    # Bỏ dấu [] ở giá trị cột Skills
    df["Skills"] = df["Skills"].apply(lambda x: ", ".join(x))

    # Hỏi người dùng có muốn filter dữ liệu trước khi xuất file không
    filter_choice = (
        input("Do you want to filter the result? (yes/no): ").strip().lower()
    )

    if filter_choice == "yes":
        filter_keyword = input("Input the skill you want to filter (ex: SQL): ").strip()

        filter_pattern = re.escape(filter_keyword)

        # Filter the DataFrame using re.findall to check for matches
        df = df[
            df["Skills"].apply(
                lambda x: bool(re.findall(filter_pattern, x, flags=re.IGNORECASE))
            )
        ]

        # Check if the filtered DataFrame is empty
        if df.empty:
            print("No matching jobs found.")
            return  # Exit the function if no matches are found

    # Xuất file ra CSV (filtered or full)
    csv_file_path = (
        r"C:\Users\Admin\Python 35-days Challenge\Project 5\job_listings.csv"
    )

    if os.path.exists(csv_file_path):
        df.to_csv(
            csv_file_path, encoding="utf-8-sig", mode="a", header=False, index=False
        )
    else:
        df.to_csv(csv_file_path, encoding="utf-8-sig", index=False)

    print(df)


while True:
    automated_job_listing()
    time.sleep(10)
