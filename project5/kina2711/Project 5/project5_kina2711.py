# Great job! I did comment on the code. Please check the comments (find NOTE:) and let me know if you have any questions.
# It seems like u have not implemented filter job using regex.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import csv
import schedule
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a set to store the job links that have already been sent
sent_job_links = set()


def extract(page):
    # NOTE: instead of creating a new driver for each page, you can create a single driver and use it for all pages.
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=option
    )
    url = f"https://careerviet.vn/viec-lam/Data-Analyst-k-trang-{page}-vi.html"
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    driver.quit()
    return soup


def transform(soup):
    job_data = []
    job_find = soup.find(class_="no-search")
    if job_find:
        return job_data
    else:
        job_results_div = soup.find(id="jobs-side-list-content")
        job_listings = job_results_div.find_all(class_="job-item")
        for job in job_listings:
            job_title_element = job.find("a", class_="job_link")
            job_title = job_title_element.contents[0].strip()
            job_link_tag = job.find(class_="job_link")
            job_link = job_link_tag.get("href")
            company_name_element = job.find(class_="company-name")
            company_name = company_name_element.text
            job_location_element = job.find(class_="location")
            job_location_tag = job_location_element.find_all("li")
            job_location = " | ".join([li.text.strip() for li in job_location_tag])
            job_salary_element = job.find(class_="salary")
            job_salary = job_salary_element.text
            job_date_element = job.find(class_="time")
            job_date = job_date_element.find("time").text.strip()
            application_deadline_element = job.find(class_="expire-date")
            application_deadline = application_deadline_element.text
            job_data.append(
                {
                    "Job Title": job_title,
                    "Job Link": job_link,
                    "Company Name": company_name,
                    "Job Location": job_location,
                    "Salary": job_salary,
                    "Date posted": job_date,
                    "Application Deadline": application_deadline,
                }
            )
        return job_data


def send_email(job_data):
    global sent_job_links
    new_job_data = []
    for job in job_data:
        if job["Job Link"] not in sent_job_links:
            new_job_data.append(job)
            sent_job_links.add(job["Job Link"])
    if new_job_data:
        email_content = f"Found {len(new_job_data)} new job listings:\n\n"
        for job in new_job_data:
            email_content += f"Job Title: {job['Job Title']}\n"
            email_content += f"Job Link: {job['Job Link']}\n\n"
            email_content += f"Company Name: {job['Company Name']}\n"
            email_content += f"Job Location: {job['Job Location']}\n"
            email_content += f"Salary: {job['Salary']}\n"
            email_content += f"Date posted: {job['Date posted']}\n"
            email_content += f"Application Deadline: {job['Application Deadline']}\n"
            email_content += f"-------------------------------------\n"

        sender_email = "abc@abc.com"
        receiver_email = "abc@xyz.com"
        subject = "Latest Job Listings"
        password = "MASK_PASSWORD"  # App passwords

        try:
            session = smtplib.SMTP("smtp.gmail.com", 587)
            session.starttls()
            session.login(sender_email, password)
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(email_content, "plain"))
            session.sendmail(sender_email, receiver_email, message.as_string())
            session.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")


def scrape_jobs():
    job_data = []
    i = 1
    # NOTE: what if user wants to stop the program? Your program will not return any data if user stops the program using Ctrl-C.
    while True:
        print(f"Getting page, {i}")
        soup = extract(i)
        new_job_data = transform(soup)
        if not new_job_data:
            break
        job_data.extend(new_job_data)
        i += 3  # NOTE: why i += 3?

    return job_data


job_data = scrape_jobs()
df = pd.DataFrame(job_data)
print(df.head())
df.to_csv("job_data.csv")
# send_email(job_data)
schedule.every().day.at("06:00").do(scrape_jobs)
while True:
    schedule.run_pending()
    time.sleep(60)
