import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import datetime
import os

def job_scraper():
    url = 'https://topdev.vn/it-jobs?src=topdev.vn&medium=mainmenu'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('section')
    column = table.find('ul')
    column1 = column.find_all('li', class_='mb-4 last:mb-0')
    # Create an empty DataFrame with the desired columns
    df = pd.DataFrame(columns=['Job Title', 'Link', 'Company Name', 'Level', 'Location', 'Date Posted','TimeStamp'])
    
    # List to collect dictionaries (rows) before concatenating
    rows = []
    
    for row in column1:
        # Extract job title
        job = row.find('h3', class_='line-clamp-1')
        job_title = job.text.strip() if job else None
    
        # Extract job link
        link = row.find('a', href=True)
        job_link = link['href'] if link else None
    
        # Extract company name
        company_name = row.find('div', class_='mt-1 line-clamp-1')
        company = company_name.text.strip() if company_name else None
    
        # Extract level (e.g., job seniority level)
        level = row.find('p', class_='text-gray-500')
        job_level = level.text.strip() if level else None
    
        # Extract location (assuming it's inside a div with class 'flex flex-wrap items-end gap-2 text-gray-500')
        location_container = row.find('div', class_='flex flex-wrap items-end gap-2 text-gray-500')
        location = location_container.text.strip() if location_container else None
    
        # Extract date posted (assuming it's inside a div with class 'mt-4 flex items-center justify-between')
        date_container = row.find('div', class_='mt-4 flex items-center justify-between')
        date_posted = date_container.find('p').text.strip() if date_container and date_container.find('p') else None

        current_time = datetime.datetime.now()
        
        # Add the extracted data as a dictionary to the rows list
        rows.append({
            'Job Title': job_title,
            'Link': job_link,
            'Company Name': company,
            'Level': job_level,
            'Location': location,
            'Date Posted': date_posted,
            'TimeStamp': current_time
        })
    
    # Convert the list of dictionaries to a DataFrame
    new_data = pd.DataFrame(rows)
    
    # Filter out any rows that are entirely empty (all-NA entries)
    new_data = new_data.dropna(how='all')
    
    # Concatenate the new data with the original DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Print the DataFrame to see the results
    # df.to_csv('CryptoScraper.csv', index = False)
    print(df)
    
# Schedule the job scraper to run daily at a specific time
schedule.every().day.at("07:00").do(job_scraper)

job_scraper()

criteria = {
    'Level': 'Fresher|Intern',
    'Location': '^[Hồ Chí Minh]%'
}
