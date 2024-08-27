import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def Scrape_job_listings():
    """
    Scrapes job listings for Data Analyst positions from the Carrerviet.vn website.
    The function iterates over the first 5 pages of job listings, extracts details,
    filters the listings based on specific conditions and saves the results to a CSV file.
    """

    # Initialize an empty DataFrame to store all pages data
    all_pages_df = pd.DataFrame()

    # Loop through the first 5 pages of the job listings
    for page in range(1,6):
        # Construct the URL for the current page
        url = f"https://careerviet.vn/viec-lam/Data-Analyst-k-trang-{page}-vi.html"

        # Define the headers to simulate a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

        # Send a GET request to the page
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError if the status is 4xx, 5xx
        except requests.exceptions.RequestException as e:
            print(f"ERROR: Failed to retrieve data from {url} - {e}")
            continue  # Skip to the next page

        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all elements that contain company names
        company_elements = soup.find_all('a', class_='company-name')
        job_listings = []

        # Iterate through each company element to extract job details
        for company in company_elements:
            job_item = company.find_parent('div', class_='job-item')

            # Extract relevant job details
            if job_item:
                row_data = []
                job_title = job_item.find('a', class_='job_link').get('title')
                company_name = company.get_text(strip=True)
                salary = job_item.find('div', class_='salary').get_text(strip=True)
                location = job_item.find('div', class_='location').get_text(strip=True)
                welfare_tags = job_item.find_all('ul', class_='welfare')
                welfare = ', '.join([item.get_text(strip=True) for item in welfare_tags[0].find_all('li')] if welfare_tags else [])
                expire_date = job_item.find('div', class_='expire-date').get_text(strip=True)
                job_url = job_item.find('a', class_='job_link').get('href')
                page_number = f'Page {page}'

                # Append the extracted data to the row
                row_data.extend([job_title, company_name, salary, location, welfare, expire_date, job_url, page_number])
                job_listings.append(row_data)
            else:
                print("ERROR: Job item not found.")
                continue  # Skip to the next company

        # Create a DataFrame from the job listings
        df = pd.DataFrame(job_listings, columns = ['Job Title', 'Company Name', 'Salary', 'Location', 'Welfare', 'Expire date', 'Job Link', 'Page Number'])

        # Define filtering functions
        def check_location(location):
            return bool(re.search(r'Hà Nội|Hồ Chí Minh', location, re.IGNORECASE))

        def check_job_title(job_title):
            return not bool(re.search(r'.*Nhân viên.*', job_title, re.IGNORECASE))

        def check_welfare(welfare):
            return bool(re.search(r'.*Bảo hiểm.*|.*Phụ cấp.*', welfare, re.IGNORECASE))

        # Apply filters to the DataFrame
        condition_location = df['Location'].apply(check_location)
        condition_job_title = df['Job Title'].apply(check_job_title)
        condition_welfare = df['Welfare'].apply(check_welfare)

        # Filter the DataFrame based on all conditions
        filtered_df = df[condition_location & condition_job_title & condition_welfare]

        # Concatenate the filtered data to the overall DataFrame
        all_pages_df = pd.concat([all_pages_df, filtered_df], ignore_index=True)

    # Save the final DataFrame to a CSV file
    print(all_pages_df)
    try:
        all_pages_df.to_csv('job_listings.csv', index=False, encoding='utf-8-sig')
        print("Data has been saved to file job_listings.csv")
    except Exception as e:
        print(f"ERROR: Failed to save data to CSV - {e}")

def Scheduling():
    """
    Schedules the 'Scrape_job_listings' function to run daily at 9:00 AM.
    """

    import schedule
    import time

    # Schedule the scraping function to run daily at 9:00 AM
    schedule.every().day.at("09:00").do(Scrape_job_listings)
    print("Data retrieval has been scheduled automatically for 9:00 AM daily!")

    # Keep the script running to ensure the scheduling works
    while True:
        schedule.run_pending()
        time.sleep(1)

def Send_email(recipient_email):
    """
    Sends an email with the job listings CSV file attached to the specified recipient email.
    """

    import win32com.client as win32
    import os

    # Email content setup
    subject = "Job listings from Carreviet.vn"
    body = "Job listings in the attached file!"
    recipient_email = recipient_email
    attachment_path = os.path.join(os.getcwd(), 'job_listings.csv')

    # Initialize the Outlook application
    try:
        outlook = win32.Dispatch('Outlook.application')
    except Exception as e:
        print(f"ERROR: Failed to initialize Outlook application - {e}")
        return

    # Create a new Outlook email
    mail = outlook.CreateItem(0)
    mail.To = recipient_email
    mail.Subject = subject
    mail.Body = body

    # Attach the CSV file if it exists
    if os.path.isfile(attachment_path):
        mail.Attachments.Add(attachment_path)
    else:
        print(f"ERROR: File {attachment_path} not exist.")
        return

    # Send the email
    mail.Send()
    print("Email sent successfully!")

if __name__ == '__main__':
    """
    Main script execution to select options and perform actions based on user input.
    """

    # User interface for selecting the desired operation
    print("Select the options corresponding to the following requirements:")
    print("1. Retrieve job listings data from the website Carrerviet.vn and save it to a CSV file.")
    print("2. Retrieve data and schedule daily data retrieval")
    print("3. Retrieve data and send an email")

    while True:
        requirement = input("Chose option 1 or 2 or 3: ")
        if requirement == '1':
            Scrape_job_listings()
            break
        elif requirement == '2':
            Scrape_job_listings()
            Scheduling()
            break
        elif requirement == '3':
            recipient_email = input("Enter recipient email: ")
            Scrape_job_listings()
            Send_email(recipient_email)
            break
        else:
            print("ERROR: Invalid input!")