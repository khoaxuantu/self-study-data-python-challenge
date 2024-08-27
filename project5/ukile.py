import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Base URL for the job listings
base_url = "https://itviec.com/it-jobs?page={}"

# List to store all job data
all_jobs_data = []

# Define regular expressions for filtering
language_regex = re.compile(r'Python|JavaScript', re.I)
exclude_regex = re.compile(r'internship|part-time', re.I)

# Iterate over multiple pages
for page in range(1, 6):  # Modify the range as needed
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all job listings on the page
    job_listings = soup.find_all('div', class_='job__body')  # Adjust the class name as needed

    for job in job_listings:
        title = job.find('h3', class_='title').get_text(strip=True)  # Adjust the tag and class name as needed
        company = job.find('div', class_='company').get_text(strip=True)  # Adjust the class name as needed
        location = job.find('div', class_='location').get_text(strip=True)  # Adjust the class name as needed
        description = job.find('div', class_='description').get_text(strip=True)  # Adjust the class name as needed
        date_posted = job.find('div', class_='date').get_text(strip=True)  # Adjust the class name as needed
        job_link = job.find('a', href=True)['href']  # Adjust the tag as needed

        # Filter jobs based on criteria
        if language_regex.search(description) and not exclude_regex.search(description):
            all_jobs_data.append({
                'Job Title': title,
                'Company Name': company,
                'Location': location,
                'Description': description,
                'Date Posted': date_posted,
                'Job Link': f"https://itviec.com{job_link}"
            })

# Create a DataFrame from the list
df = pd.DataFrame(all_jobs_data)

# Check if DataFrame is empty
if df.empty:
    print("No job listings found.")
else:
    # Save the DataFrame to a CSV file
    df.to_csv('job_listings.csv', index=False)
    print("Job listings have been saved to job_listings.csv")