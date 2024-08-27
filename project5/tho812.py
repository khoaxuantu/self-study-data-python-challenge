Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... from bs4 import BeautifulSoup
... import re
... import csv
... import os
... 
... urls = [
...     'https://www.vietnamworks.com/viec-lam?g=5',
...     'https://itviec.com/it-jobs?job_selected=senior-frontend-engineer-angular8-bbv-vietnam-2138'
... ]
... 
... include_lang = r'\bpython\b'
... exclude_keywords = r'\b(internship|part-time|parttime)\b'
... 
... job_listings = []
... 
... def scrape_jobs(url):
...     while url:
...         response = requests.get(url)
...         soup = BeautifulSoup(response.content, 'html.parser')
...         
...         if 'vietnamworks' in url:
...             job_cards = soup.find_all('div', class_='job-item')
...             next_page = soup.find('a', {'aria-label': 'Next'})
...             next_url = next_page['href'] if next_page else None
...         elif 'itviec' in url:
...             job_cards = soup.find_all('div', class_='job')
...             next_page = soup.find('a', class_='pagination__next')
...             next_url = next_page['href'] if next_page else None
...         
...         for card in job_cards:
...             title = card.find('h2').get_text(strip=True)
...             company = card.find('div', class_='company-name').get_text(strip=True)
...             location = card.find('div', class_='location').get_text(strip=True)
...             description = card.find('div', class_='description').get_text(strip=True)
            date_posted = card.find('time').get_text(strip=True)
            link = card.find('a')['href']
            
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Location: {location}")
            print(f"Description: {description}")
            print(f"Date Posted: {date_posted}")
            print(f"Link: {link}")
            print('-' * 40)
            
            if (re.search(include_lang, description, re.IGNORECASE) and
                not re.search(exclude_keywords, description, re.IGNORECASE)):
                job_listings.append({
                    'Job Title': title,
                    'Company Name': company,
                    'Location': location,
                    'Description': description,
                    'Date Posted': date_posted,
                    'Job Link': link
                })

        if next_url:
            url = next_url
        else:
            break

for url in urls:
    scrape_jobs(url)

output_file = os.path.join('D:\\project5', 'filtered_jobs.csv')

if job_listings:
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=job_listings[0].keys())
        writer.writeheader()
        writer.writerows(job_listings)
    print(f'Saved {len(job_listings)} jobs to CSV.')
else:
    print('No jobs found matching the criteria.')

