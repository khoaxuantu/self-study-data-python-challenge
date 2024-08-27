import requests
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class TopDevScraper:
    def __init__(self, driver_path, url, email_config):
        self.driver_path = driver_path
        self.url = url
        self.email_config = email_config
        self.driver = self._setup_driver()
        self.last_update_file = 'last_update.txt'

    def _setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for better performance
        service = Service(self.driver_path)
        return webdriver.Chrome(service=service, options=chrome_options)

    def _get_last_update(self):
        if os.path.exists(self.last_update_file):
            with open(self.last_update_file, 'r') as file:
                return datetime.strptime(file.read().strip(), "%Y-%m-%d")
        return None

    def _update_last_update(self):
        with open(self.last_update_file, 'w') as file:
            file.write(datetime.now().strftime("%Y-%m-%d"))

    def close_popup(self):
        try:
            close_button = self.driver.find_element(By.ID, 'btn-close-new-year-modal')
            close_button.click()
            time.sleep(2)  # Wait for the popup to close
        except Exception as e:
            print(f"No popup to close or error: {e}")

    def scroll_to_bottom(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollBy(0, 2706);")
            time.sleep(4)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def scrape_page(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.close_popup()
        self.scroll_to_bottom()
        soup_main = BeautifulSoup(self.driver.page_source, 'html.parser')
        jobs = soup_main.find_all('h3', class_='line-clamp-1')
        job_links = []
        base_url = "https://topdev.vn"
        for job in jobs:
            link = job.find('a')
            if link:
                full_link = base_url + link['href']
                job_links.append(full_link)
        return job_links

    def parse_time(self, post_time_ago):
        if 'minutes' in post_time_ago:
            minutes_ago = int(post_time_ago.split()[0])
            post_time = datetime.now() - timedelta(minutes=minutes_ago)
        elif 'hours' in post_time_ago:
            hours_ago = int(post_time_ago.split()[0])
            post_time = datetime.now() - timedelta(hours=hours_ago)
        elif 'days' in post_time_ago:
            days_ago = int(post_time_ago.split()[0])
            post_time = datetime.now() - timedelta(days=days_ago)
        elif 'months' in post_time_ago:
            months_ago = int(post_time_ago.split()[0])
            post_time = datetime.now() - timedelta(days=30*months_ago)
        else:
            post_time = datetime.now()
        return post_time.strftime("%Y-%m-%d %H:%M:%S")

    def scrape_job_details(self, job_links):
        job_list = []
        for job_link in job_links:
            response_url = requests.get(job_link)
            soup_url = BeautifulSoup(response_url.content, 'html.parser')
            try:
                job_title = soup_url.find('h1', class_='text-2xl font-bold text-black').get_text()
                company_name = soup_url.find('p', class_='my-1 line-clamp-1 text-base font-bold text-gray-500').get_text()
                job_location = soup_url.find('div', class_='w-11/12').get_text()
                post_time_ago = soup_url.find('div', class_='flex w-11/12 items-center text-base text-gray-500').get_text()[7:]
                post_time = self.parse_time(post_time_ago)
                experience = soup_url.find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')[0].get_text()
                job_description_text = soup_url.find('div', class_='rounded bg-white p-4 md:px-6 md:py-4').get_text()
                job_description = re.sub(r'^\n+', '', job_description_text).replace('\n', '.').replace('..', '.')
                level_information = soup_url.find('div', class_='item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
                level = [a_tag.get_text() for a_tag in level_information.find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')] if level_information else []
                job_type = None
                job_type_information = soup_url.find_all('div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full')
                for info in job_type_information:
                    job_type_tag = info.find('a', class_="text-sm hover:text-primary-300 hover:underline md:text-base")
                    if job_type_tag:
                        job_type = job_type_tag['title']
                contract_type = None
                contract_type_information = soup_url.find_all('div', class_='item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
                for info in contract_type_information:
                    contract_type_tag = info.find('a', class_="text-sm hover:text-primary-300 hover:underline md:text-base")
                    if contract_type_tag:
                        contract_type = contract_type_tag['title']
                tech_stack = [info.get_text(strip=True) for info in soup_url.find_all('span', class_='whitespace-nowrap rounded border border-solid font-normal transition-all inline-flex items-center justify-center border-blue-light text-blue-dark bg-blue-light hover:border-blue-dark h-[1.625rem] px-2 text-xs md:h-7 md:px-2 md:text-sm')]
                job_content = (job_title + '$$' + company_name + '$$' + job_location + '$$' + str(post_time) + '$$' + job_description + '$$'
                               + experience + '$$' + str(level) + '$$' + str(job_type) + '$$' + str(contract_type) + '$$' + str(tech_stack) + '$$'
                               + job_link)
                job_list.append(job_content)
            except Exception as e:
                print(f"Error scraping job details: {e}")
        return job_list

    def filter_jobs(self, job_list):
        filtered_jobs = []
        include_patterns = [r'Python', r'JavaScript', r'Java', r'C++', r'Ruby', r'Go', r'Swift', r'PHP', r'C#', r'Scala']
        keyword_patterns = [r'remote', r'full-time', r'fulltime']
        exclude_patterns = [r'internship', r'part-time', r'intern', r'parttime']
        for job in job_list:
            include_match = any(re.search(pattern, job, re.IGNORECASE) for pattern in include_patterns)
            keyword_match = any(re.search(pattern, job, re.IGNORECASE) for pattern in keyword_patterns)
            exclude_match = any(re.search(pattern, job, re.IGNORECASE) for pattern in exclude_patterns)
            if include_match and keyword_match and not exclude_match:
                filtered_jobs.append(job)
        return filtered_jobs

    def send_email(self, job_list):
        if not job_list:
            print("No jobs to send.")
            return

        msg = MIMEMultipart()
        msg['From'] = self.email_config['from']
        msg['To'] = self.email_config['to']
        msg['Subject'] = "TopDevLatest IT Job Listings"

        body = "<h1>Latest IT Job Listings</h1><ul>"
        for job in job_list:
            body += f"<li>{job.replace('$$', '<br>')}</li>"
        body += "</ul>"

        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
            server.starttls()
            server.login(self.email_config['username'], self.email_config['password'])
            server.send_message(msg)
            print("Email sent successfully.")

    def run(self):
        if self._get_last_update() != datetime.now().date():
            job_links = self.scrape_page()
            job_list = self.scrape_job_details(job_links)
            filtered_jobs = self.filter_jobs(job_list)
            self.send_email(filtered_jobs)
            self._update_last_update()
        else:
            print("Data has already been updated today.")

if __name__ == "__main__":
    email_config = {
        'from': 'xxxx@gmail.com',
        'to': 'xxxx@gmail.com', # Don't send me your email bruh
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'username': 'xxxx@gmail.com',
        'password': '********' # Paste password to use
    }
    scraper = TopDevScraper(driver_path='D:/Drivers/chromedriver-win64/chromedriver.exe',
                           url="https://topdev.vn/it-jobs?src=topdev_home&medium=newjobs",
                           email_config=email_config)
    scraper.run()
