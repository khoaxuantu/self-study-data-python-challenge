import time
from datetime import datetime
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
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule


Require_Term = [r'IT Phần mềm', r'tester', r'Phân tích', r'mobile', r'web']
Exclude_Term = [r'IT Phần cứng', r'Intership', r'Thực tập sinh', r'Hà Nội']

def meets_criteria(details_div):
    terms = details_div.find_all('a', class_='inline-block mb-2 text-12 font-semibold px-2 py-1 rounded-md bg-[#EFEFF0] text-se-neutral-80 mr-2')
    for term in terms:
        if any(re.search(exclude_term, term.text, re.IGNORECASE) for exclude_term in Exclude_Term):
            return False
        if any(re.search(require_term, term.text, re.IGNORECASE) for require_term in Require_Term):
            return True
    return False

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_service = Service(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver

def save_to_csv(job_listings):
    file_path = r'D:\python\joblistings.csv'
    df = pd.DataFrame(job_listings)

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', index=False, encoding='utf-8')
    else:
        df.to_csv(file_path, mode='w', index=False, encoding='utf-8')

    print(f"Data has been saved to {file_path}")
    print(df)

    send_email_notification(job_listings)

def send_email_notification(job_listings):
    sender_email = 'abc@xyz.com' # Bruh don't send me your email
    receiver_email = 'abc@abc.com' # Again?
    password = 'MASK_PASSWORD'

    subject = 'Latest Job Listings'
    body = 'Here are the latest job listings that match your criteria:\n\n'
    body += '\n\n'.join([f"Job Title: {job['Job Title']}\nCompany Name: {job['Company Name']}\nLocation: {job['Location']}\nDescription: {job['Description']}\nDate Posted: {job['Date Posted']}\nJob Link: {job['Job Link']}\nUpdate Time: {job['Update Time']}" for job in job_listings])

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print('Email notification sent successfully.')
    except Exception as e:
        print(f"Failed to send email: {e}")

def scrape_jobs(max_pages):
    driver = setup_driver()
    print("Scraping job listings...")
    job_listings = []

    base_url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=8&page={}&sort_q='

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        driver.get(url)
        time.sleep(10)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        for job in soup.find_all('a', class_='relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white border-se-blue-10'):
            title = job.find('div', class_='relative lg:w-full w-11/12 flex items-start flex-1 overflow-hidden pr-2 lg:pr-8').text.strip()
            company_name = job.find('h3', class_='inline-block text-grey-48 text-[16px] leading-6 truncate pr-2 max-w-[240px] lg:max-w-full').text.strip()
            job_link = job['href']
            full_job_link = urljoin(url, job_link)

            try:
                driver.get(full_job_link)
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "jsx-5b2773f86d2f74b")]'))
                )
                job_page_source = driver.page_source
                job_soup = BeautifulSoup(job_page_source, 'html.parser')
                details_div = job_soup.find('div', class_='jsx-5b2773f86d2f74b px-4 md:px-10 py-4 bg-white shadow-sd-12 rounded-sm')

                if details_div:
                    description = details_div.find('div', class_='jsx-5b2773f86d2f74b mb-2 text-14 break-words text-se-neutral-80 text-description').text.strip() if details_div.find('div', class_='jsx-5b2773f86d2f74b mb-2 text-14 break-words text-se-neutral-80 text-description') else "Description not found"
                    location = details_div.find('h3', class_='jsx-5b2773f86d2f74b mb-2 flex text-14').text.strip() if details_div.find('h3', class_='jsx-5b2773f86d2f74b mb-2 flex text-14') else "Location not found"
                    date_posted = details_div.find('p', class_='text-14').text.strip() if details_div.find('p', class_='text-14') else "Date posted not found"

                    if meets_criteria(details_div):
                        update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        job_listings.append({
                            'Job Title': title,
                            'Company Name': company_name,
                            'Location': location,
                            'Description': description,
                            'Date Posted': date_posted,
                            'Job Link': full_job_link,
                            'Update Time': update_time
                        })
            except Exception as e:
                print(f"An error occurred on page {page} for job link {full_job_link}: {e}")
                continue

    driver.quit()

    save_to_csv(job_listings)

def schedule_jobs(max_pages):
    schedule.every().day.at("09:00").do(scrape_jobs, max_pages)

    while True:
        schedule.run_pending()
        time.sleep(1)

scrape_jobs(3)

schedule_jobs(3)

