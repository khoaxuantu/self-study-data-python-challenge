# Great work! I did comment on your code (find NOTE:).

import time
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule


class JobCrawler:
    def __init__(self, include_keywords, exclude_keywords, max_pages=4):
        self.include_keywords = include_keywords
        self.exclude_keywords = exclude_keywords
        self.max_pages = max_pages
        self.job_data = []
        self.base_url = "https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=8&page={}&sort_q="

    def filter_jobs(self, job_tags):
        for tag in job_tags:
            if any(
                re.search(kw, tag.text, re.IGNORECASE) for kw in self.exclude_keywords
            ):
                return False
            if any(
                re.search(kw, tag.text, re.IGNORECASE) for kw in self.include_keywords
            ):
                return True
        return False

    def fetch_job_listings(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        service = Service(r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe")

        with webdriver.Chrome(service=service, options=options) as browser:
            # NOTE: should handle the case where the page does not exist, because you wrap the `browser.get` in a try-except block, thus if the page does not exist, the program will stop.
            for page in range(1, self.max_pages + 1):
                current_url = self.base_url.format(page)
                print(f"Fetching jobs from page: {page}")
                browser.get(current_url)
                time.sleep(10)
                soup = BeautifulSoup(browser.page_source, "html.parser")

                job_links = soup.find_all(
                    "a",
                    class_="relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white border-se-blue-10",
                )
                for link in job_links:
                    job_title = link.find(
                        "div",
                        class_="relative lg:w-full w-11/12 flex items-start flex-1 overflow-hidden pr-2 lg:pr-8",
                    ).text.strip()
                    company = link.find(
                        "h3",
                        class_="inline-block text-grey-48 text-[16px] leading-6 truncate pr-2 max-w-[240px] lg:max-w-full",
                    ).text.strip()
                    job_url = urljoin(current_url, link["href"])

                    try:
                        browser.get(job_url)
                        WebDriverWait(browser, 30).until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH,
                                    '//*[contains(@class, "jsx-5b2773f86d2f74b")]',
                                )
                            )
                        )
                        job_soup = BeautifulSoup(browser.page_source, "html.parser")
                        job_section = job_soup.find(
                            "div",
                            class_="jsx-5b2773f86d2f74b px-4 md:px-10 py-4 bg-white shadow-sd-12 rounded-sm",
                        )

                        if job_section and self.filter_jobs(
                            job_section.find_all(
                                "a",
                                class_="inline-block mb-2 text-12 font-semibold px-2 py-1 rounded-md bg-[#EFEFF0] text-se-neutral-80 mr-2",
                            )
                        ):
                            description = (
                                job_section.find(
                                    "div",
                                    class_="jsx-5b2773f86d2f74b mb-2 text-14 break-words text-se-neutral-80 text-description",
                                ).text.strip()
                                if job_section.find(
                                    "div",
                                    class_="jsx-5b2773f86d2f74b mb-2 text-14 break-words text-se-neutral-80 text-description",
                                )
                                else "No description"
                            )
                            location = (
                                job_section.find(
                                    "h3", class_="jsx-5b2773f86d2f74b mb-2 flex text-14"
                                ).text.strip()
                                if job_section.find(
                                    "h3", class_="jsx-5b2773f86d2f74b mb-2 flex text-14"
                                )
                                else "No location"
                            )
                            posted_date = (
                                job_section.find("p", class_="text-14").text.strip()
                                if job_section.find("p", class_="text-14")
                                else "No date"
                            )

                            self.job_data.append(
                                {
                                    "Job_Title": job_title,
                                    "Company": company,
                                    "Location": location,
                                    "Description": description,
                                    "Posted_Date": posted_date,
                                    "Job_Link": job_url,
                                }
                            )
                    except Exception as error:
                        print(f"Error on page {page} for job {job_url}: {error}")
                        continue

    def save_to_file(self, filepath):
        df = pd.DataFrame(self.job_data)
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
        print(f"Job data stored at: {filepath}")
        print(df)

    def send_email_alert(self, sender, recipient, app_password):
        email_subject = "Latest Job Opportunities"
        email_body = "Check out the latest job listings:\n\n"
        for job in self.job_data:
            email_body += f"Job Title: {job['Job_Title']}\n"
            email_body += f"Company: {job['Company']}\n"
            email_body += f"Location: {job['Location']}\n"
            email_body += f"Description: {job['Description']}\n"
            email_body += f"Posted Date: {job['Posted_Date']}\n"
            email_body += f"Link: {job['Job_Link']}\n\n"

        email_msg = MIMEMultipart()
        email_msg["From"] = sender
        email_msg["To"] = recipient
        email_msg["Subject"] = email_subject
        email_msg.attach(MIMEText(email_body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as mail_server:
                mail_server.starttls()
                mail_server.login(sender, app_password)
                mail_server.send_message(email_msg)
            print("Email sent successfully.")
        except Exception as mail_error:
            print(f"Error sending email: {mail_error}")


crawler = JobCrawler(
    include_keywords=[r"IT Phần mềm", r"tester", r"Phân tích", r"mobile", r"web"],
    exclude_keywords=[r"IT Phần cứng", r"Intership", r"Thực tập sinh", r"Hà Nội"],
)
crawler.fetch_job_listings()
crawler.save_to_file(r"C:\Users\TGDD\OneDrive\Documents\Python\job_listings.csv")
crawler.send_email_alert(
    sender="xxxx@gmail.com",  # Don't send your email to me sis -_-
    recipient="xxxx@xxx.com",
    app_password="<<MASK_PASSWORD>>",  # Don't public the password plz
)
schedule.every().day.at("15:40").do(crawler.fetch_job_listings)

while True:
    schedule.run_pending()
    time.sleep(10)
