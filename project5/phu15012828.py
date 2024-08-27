from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime, timedelta

"""
First, use the TopDev website in English. The URL for job search is filtered with 'data' 
to reduce the number of job listings. You can also filter further by options like job level and contract 
type to minimize future filtering. If you want to see all available jobs, 
use this URL: https://topdev.vn/it-jobs 

Next, use Selenium to open the website, zoom in, and close any pop-ups if they appear. 
Then, click the 'See More' button to load additional job listings. 
Continue clicking this button until there are no more jobs to load.
"""
def parse_relative_time(relative_time_str):
    now = datetime.now()
    if 'hour' in relative_time_str:
        hours = int(re.findall(r'\d+', relative_time_str)[0])
        return now - timedelta(hours=hours)
    elif 'day' in relative_time_str:
        days = int(re.findall(r'\d+', relative_time_str)[0])
        return now - timedelta(days=days)
    elif 'week' in relative_time_str:
        weeks = int(re.findall(r'\d+', relative_time_str)[0])
        return now - timedelta(weeks=weeks)
    else:
        return now  

# Set up the Selenium WebDriver
driver = webdriver.Chrome() 
driver.maximize_window()
url = 'https://topdev.vn/it-jobs/data-k'
driver.get(url)

# Allow time for the page to load
time.sleep(5)

## Closing the pop-up ad
try:
    close_button = driver.find_element(By.XPATH, '//*[@id="btn-close-new-year-modal"]')
    close_button.click()
    time.sleep(2)  # Wait a moment after closing the ad
except:
    pass

## Load more jobs if there is a "Load More" button
while True:
    try:
        # Try clicking the "Load More" button
        more_button = driver.find_element(By.XPATH, '//*[@id="tab-job"]/div/div/div/button')
        more_button.click()
        time.sleep(2)  
    except:
        break 

## Scroll to the bottom of the page to load more jobs
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new content to load
    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height   
    

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Create Table 
job_table = soup.find('ul', class_='mt-4')

current_date_str = datetime.now().strftime('%d/%m/%Y')      
load_day = f'Load Day {current_date_str}'

table_column_titles = ['Job title','Company name', 'Job location', 'Job description', 'Date posted', 'Job link', load_day]

df = pd.DataFrame(columns = table_column_titles)

job_rows = job_table.find_all('li')

for row in job_rows:
    job_link_true = row.find('a', href=True)  # Ensure 'href' attribute is present
    if job_link_true:
        job_link = job_link_true.get('href')

        job_page_url = requests.compat.urljoin(url, job_link)  # Make sure href is an absolute URL
        job_page = requests.get(job_page_url)
        job_soup = BeautifulSoup(job_page.text, features='html.parser')

        # Take job description and job genertal information
        job_general_info_tag = job_soup.find('section', class_='w-full bg-white')
        job_general_info = job_general_info_tag.get_text().strip()  
        
        job_description_tag = job_soup.find(id='JobDescription')
        job_description = job_description_tag.get_text().strip() 
        
        job_general_info_lower = job_general_info.lower()
        job_description_lower = job_description.lower()

        # Filter job by choose
        # Job levels include intern - fresher - junior - middle - senior - leader - manager
        if 'junior' not in job_general_info_lower and 'fresher' not in job_general_info_lower:
            continue
        # Job contract types include fulltime - freelance - part-time
        if 'fulltime' not in job_general_info_lower:
            continue
        # Job types include in office - hybrid - remote - oversea
        if 'in office' not in job_general_info_lower:
            continue
        # Search for specific tools, keywords, .... in the job description 
        if 'sql' not in job_general_info_lower and 'sql' not in job_description_lower:
            continue

        # Extract job details
        detail_job_header = job_soup.find('section', id='detailJobHeader')
        if detail_job_header:
            job_title_tag = detail_job_header.find('h1')
            job_title = job_title_tag.get_text().strip()  

            company_name_tag = detail_job_header.find('p')
            company_name = company_name_tag.get_text().strip()  

            company_location_tag = detail_job_header.find('div', class_='w-11/12')
            company_location = company_location_tag.get_text().strip()  

            time_posted_tag = detail_job_header.find(class_="flex w-11/12 items-center text-base text-gray-500")
            time_posted = time_posted_tag.get_text().strip()
            time_posted_datetime = parse_relative_time(time_posted)
            time_posted = time_posted_datetime.strftime('%d/%m/%Y')  # Convert to desired format

        # Determine the next index
        next_index = len(df)
        
        # Add job data to the dataframe
        df.loc[next_index] = {
            'Job title': job_title,
            'Company name': company_name,
            'Job location': company_location,
            'Job description': job_description,
            'Date posted': time_posted,
            'Job link': job_page_url
        }

# Add data to a csv, change file_path 'File location' to desired path
file_path = r'File location\Project5.csv'
df.index = df.index + 1
if os.path.exists(file_path):
    with open(file_path, 'a') as f:
        f.write('\n')
    df.to_csv(file_path, mode='a', header=True, index=True, encoding='utf-8')
else:
    df.to_csv(file_path, mode='w', header=True, index=True, encoding='utf-8')
# Close the browser
driver.quit()

