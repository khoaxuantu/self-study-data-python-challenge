# Great work! I commented on the code, please find NOTE: to see the comments.

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime

# Define the URL
BASE_URL = "https://itviec.com/jobs"


# Function to get the HTML content of the page
def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None


# Function to parse the HTML and extract job listings
def parse_job_listings(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    jobs = []

    for job_card in soup.find_all("div", class_="job"):
        title = job_card.find("h3").get_text(strip=True)
        company = job_card.find("div", class_="company").get_text(strip=True)
        location = job_card.find("div", class_="location").get_text(strip=True)
        description = job_card.find("div", class_="description").get_text(strip=True)
        date_posted = job_card.find("div", class_="distance-time").get_text(strip=True)
        link = job_card.find("a")["href"]

        jobs.append(
            {
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Description": description,
                "Date Posted": date_posted,
                "Link": link,
            }
        )

    return jobs


# Function to filter job listings using regular expressions
def filter_jobs(jobs, include_keywords=[], exclude_keywords=[]):
    filtered_jobs = []
    for job in jobs:
        include = any(
            re.search(keyword, job["Description"], re.IGNORECASE)
            for keyword in include_keywords
        )
        exclude = any(
            re.search(keyword, job["Description"], re.IGNORECASE)
            for keyword in exclude_keywords
        )

        if include and not exclude:
            filtered_jobs.append(job)

    return filtered_jobs


# Function to save the jobs to a CSV file
def save_to_csv(jobs, filename="jobs.csv"):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Saved {len(jobs)} jobs to {filename}")


# Main function to scrape and filter jobs
def main():
    html_content = get_html_content(BASE_URL)
    if html_content:
        jobs = parse_job_listings(html_content)
        filtered_jobs = filter_jobs(
            jobs,
            include_keywords=["Python", "JavaScript"],
            exclude_keywords=["Internship", "Part-time"],
        )
        save_to_csv(filtered_jobs)


if __name__ == "__main__":
    main()

# BONUS POINT:


# Pagination Handling
def main():
    page_number = 1
    all_jobs = []

    while True:
        # NOTE: Should handle the case when the pages don't exist
        url = f"{BASE_URL}?page={page_number}"
        html_content = get_html_content(url)

        if not html_content:
            break

        jobs = parse_job_listings(html_content)

        if not jobs:
            break

        all_jobs.extend(jobs)
        page_number += 1

    filtered_jobs = filter_jobs(
        all_jobs,
        include_keywords=["Python", "JavaScript"],
        exclude_keywords=["Internship", "Part-time"],
    )
    save_to_csv(filtered_jobs)


# Scheduling the Script
import schedule
import time


def job():
    main()


schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# Notification system via email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(filtered_jobs):
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@gmail.com"
    password = "your_password"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Daily Job Listings"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    html_content = "<h2>Daily Job Listings</h2>"
    for job in filtered_jobs:
        html_content += f"<p><b>{job['Job Title']}</b> at {job['Company']} in {job['Location']} - {job['Date Posted']}<br>{job['Link']}</p>"

    part = MIMEText(html_content, "html")
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent!")


# Modify the main function to include sending an email
def main():
    # ... previous code ...
    send_email(filtered_jobs)


# Discord bot integration
import discord
from discord.ext import tasks
import os

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    job_scrape.start()


@tasks.loop(hours=24)
async def job_scrape():
    # Run the main scraping and filtering function
    main()

    # Load the filtered jobs
    jobs_df = pd.read_csv("jobs.csv")

    channel = client.get_channel(CHANNEL_ID)

    for _, job in jobs_df.iterrows():
        await channel.send(
            f"**{job['Job Title']}** at {job['Company']} in {job['Location']}\n{job['Link']}"
        )


client.run("YOUR_DISCORD_BOT_TOKEN")
