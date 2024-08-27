import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_job_listings(url, keywords, exclude_keywords):

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  job_listings = []

  # Replace with appropriate selectors based on the website's structure
  job_containers = soup.find_all('div', class_='job-listing')

  for job in job_containers:
    job_title = job.find('h2', class_='job-title').text.strip()
    company = job.find('span', class_='company').text.strip()
    location = job.find('span', class_='location').text.strip()
    description = job.find('div', class_='job-description').text.strip()
    date_posted = job.find('span', class_='date-posted').text.strip()
    job_link = job.find('a', class_='job-link')['href']

    # Filter based on keywords
    include_job = False
    for keyword in keywords:
      if keyword.lower() in description.lower():
        include_job = True
        break

    for exclude_keyword in exclude_keywords:
      if exclude_keyword.lower() in description.lower():
        include_job = False
        break

    if include_job:
      job_listings.append({
        'job_title': job_title,
        'company': company,
        'location': location,
        'description': description,
        'date_posted': date_posted,
        'job_link': job_link
      })

  return job_listings

def save_to_csv(job_listings, filename):
  with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['job_title', 'company', 'location', 'description', 'date_posted', 'job_link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(job_listings)

# Example usage
keywords = ['python', 'javascript', 'machine learning']
exclude_keywords = ['internship', 'part-time']

job_listings = scrape_job_listings('https://example.com/jobs', keywords, exclude_keywords)
save_to_csv(job_listings, 'jobs.csv')