import requests
from bs4 import BeautifulSoup
import re
import csv

wish_ls = ['python', 'javascript', 'internship', 'part-time', 'fulltime']

# Base URL of the job listings
base_url = 'https://topdev.vn/'
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')
new_job_tab = soup.find('section', id='popular-companies-container')
for job_card in new_job_tab.find_all('div', class_='card-link'):
    job_card = job_card.find('div', class_='mt-2')
    job_title = job_card.find_all('h3')
    job_position = job_title[0].text.strip()
    job_company = job_title[1].text.strip()
    job_location = job_card.p.text.strip()
    job_requirement = job_card.find_all('div', class_='mt-2')[-1]
    job_requirement = [a.text.strip() for a in job_requirement.find_all('a')]
    job_skills = job_requirement
    complete_jd = job_position.upper() + ' --- Comapany: ' + job_company + '\n' + job_location + '\n' + '(' + ', '.join(job_skills) + ')'
    for element in wish_ls:
        if element in complete_jd.lower():
            print(complete_jd)
            print('\n\n')
            break

    
