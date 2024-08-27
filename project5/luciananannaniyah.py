import csv
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import re
import schedule
import time
import pytz

BASE_URL = "https://itviec.com"
URL = "https://itviec.com/it-jobs"
CRITERIA = {
    'include': [r'\bPython\b'],
    'exclude': [r'\bHybrid\b']
}
EMAIL_SENDER = "xxxx@gmail.com" # Don't send me your email sis -_-
EMAIL_RECEIVER = "xxxx@gmail.com"
EMAIL_PASSWORD = "<<PASSWORD_MASK>>" # Don't send me your password
SMTP_PORT = 587

def save_to_csv(job_list, filename='jobs_list.csv'):
    if not job_list:
        print("No jobs to save.")
        return

    fieldnames = ['Scraping Time', 'Job Title', 'Company Name', 'Job Location', 'Posted Date', 'Description', 'Job link']
    scraping_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for job in job_list:
                job['Scraping Time'] = scraping_time
                writer.writerow(job)
        print(f"Job list saved to {filename}.")
    except Exception as e:
        print(f"Error saving CSV file: {e}")

def send_email(job_list):
    if not job_list:
        print("No jobs to send.")
        return

    email_content = ""
    for job in job_list:
        email_content += f"Job Title: {job.get('Job Title')}\n"
        email_content += f"Company: {job.get('Company Name')}\n"
        email_content += f"Location: {job.get('Job Location')}\n"
        email_content += f"Posted Date: {job.get('Posted Date')}\n"
        email_content += f"Description: {job.get('Description')}\n"
        email_content += f"Link: {job.get('Job link')}\n\n"

    subject = f"{len(job_list)} NEW JOB LISTINGS"

    if not all([EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD]):
        print("Email credentials are not set.")
        return

    try:
        session = smtplib.SMTP('smtp.gmail.com', SMTP_PORT)
        session.starttls()
        session.login(EMAIL_SENDER, EMAIL_PASSWORD)

        message = MIMEMultipart()
        message['From'] = EMAIL_SENDER
        message['To'] = EMAIL_RECEIVER
        message['Subject'] = subject
        message.attach(MIMEText(email_content, 'plain'))

        session.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
        session.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f"Error sending email: {e}")

def filter_job(text):
    include_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in CRITERIA['include']]
    exclude_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in CRITERIA['exclude']]

    if (any(pattern.search(text) for pattern in include_patterns) and
        not any(pattern.search(text) for pattern in exclude_patterns)):
        return True
    else:
        return False

def scrape_jobs():
    job_list = []
    latest_job_list = [] #in 24hrs
    page = 1
    found_day_job = False

    while True:
        url = f"{URL}?page={page}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        print(f"Scraping page {page}: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find('div', class_='card-jobs-list')
        if not jobs:
            print("No jobs found on this page.")
            break

        job_cards = jobs.find_all('div', class_='job-card')
        if not job_cards:
            print("No more jobs found.")
            break

        for item in job_cards:
            try:
                job_item = item.find('div', class_='ipy-2')
                job_title = job_item.find('h3').find('a').text.strip()
                job_company = item.find('div', class_='imy-3').find('span').find('a').text.strip()
                job_location = item.find('svg', class_='feather-icon').find_parent('div').find('span').text.strip()
                job_date = item.find('div', class_='d-flex').find('span').text.strip()[7:]
                job_type = item.find('g').find_parent('div').find('span').text.strip()
                job_tags = ", ".join(tag.text.strip() for tag in item.find_all('div', class_='itag'))
                job_description = f"Type: {job_type}. Tags: {job_tags}. "
                description_tag = item.find('ul')

                if description_tag:
                    job_description += ". ".join(li_tag.text.strip() for li_tag in description_tag.find_all('li'))
                job_link = BASE_URL + item.find('a').get('href')
                if not filter_job(job_description):
                    continue

                if 'day' in job_date and not found_day_job:
                    found_day_job = True
                    latest_job_list = job_list.copy()
                job_entry = {
                    'Job Title': job_title,
                    'Company Name': job_company,
                    'Job Location': job_location,
                    'Posted Date': job_date,
                    'Description': job_description,
                    'Job link': job_link
                }
                job_list.append(job_entry)

            except AttributeError as e:
                print(f"Error parsing job item: {e}")

        page += 1

    return job_list, latest_job_list

def job_scraper():
    job_list, latest_job_list = scrape_jobs()
    save_to_csv(job_list)
    send_email(latest_job_list)

# job_scraper()
local_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
local_now = datetime.now(local_timezone)
schedule.every().day.at("09:00").do(job_scraper)

while True:
    schedule.run_pending()
    time.sleep(60)
