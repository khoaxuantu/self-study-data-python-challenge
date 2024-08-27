### Import statements
# Basic imports
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import schedule
import time
# Webdriver and fake user-agent
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# For email sending
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

### File path for storing the result csv
file_path = 'C:/Users/admin/OneDrive/Documents/Python_practice/Project 5/'

############################################################################################################################################

### The job scrape function
# Filter criteria: data jobs at Hanoi banks that provide insurance, the position is not intern, and require Excel, Python, SQL or PBI skills
def scrape_pages(page_number, place, driver):
    city_code = {'ho-chi-minh': 8, 'ha-noi': 4, 'quanh-ninh': 33, 'can-tho': 71, 'hai-phong': 31, 'da-nang': 511}

    url = f"https://careerviet.vn/viec-lam/{place}-l{city_code[place]}-trang-{page_number}-vi.html"

    def scrape_details(url, driver):
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            details = driver.page_source
            soup = BeautifulSoup(details, 'html.parser')

            job_title = soup.find('h1', class_='title').text.strip()
            company_name = soup.find('a', class_='employer job-company-name').text.strip()
            
            detail_box = soup.find_all('div', class_='detail-box has-background')
            updated, position, level, salary, deadline = [''] * 5
            for detail in detail_box:
                columns = detail.find_all('li')
                for column in columns:
                    if column.find('strong').text.strip() == 'Ngày cập nhật':
                        updated = column.find('p').text.strip()
                    elif column.find('strong').text.strip() == 'Hình thức':
                        position = column.find('p').text.strip()
                    elif column.find('strong').text.strip() == 'Cấp bậc':
                        level = column.find('p').text.strip()
                    elif column.find('strong').text.strip() == 'Lương':
                        salary = column.find('p').text.strip()
                    elif column.find('strong').text.strip() == 'Hết hạn nộp':
                        deadline = column.find('p').text.strip()
                    else:
                        pass
            if level == 'Sinh viên/ Thực tập sinh' or re.search(r'thực tập', position, flags=re.IGNORECASE):
                return True
            
            welfare_list = [li.text.strip() for li in soup.find('ul', class_='welfare-list').find_all('li')]
            if 'Chế độ bảo hiểm' not in welfare_list:
                return True
            
            header = soup.find('h2', class_='detail-title', string=re.compile('Yêu Cầu Công Việc', re.IGNORECASE))
            paragraphs = header.find_next_siblings()
            job_req = ''
            for paragraph in paragraphs:
                job_req += paragraph.text.strip() + '\n'
    
            if not re.search(r'python|sql|pbi|powerbi|excel', job_req, flags=re.IGNORECASE):
                return True
            
            header = soup.find('h2', class_='detail-title', string=re.compile('Mô tả Công việc', re.IGNORECASE))
            paragraphs = header.find_next_siblings()
            job_des = ''
            for paragraph in paragraphs:
                job_des += paragraph.text.strip() + '\n'
    
            try:
                address = soup.find('i', class_='fa fa-map-marker fa-fw').text.strip()
            except: # If there's no exact addresses, take the city/province as the address instead
                address = soup.find('div', class_='map').text.strip()
            
            job_details_dict = {'updated': updated, 'application deadline': deadline, 'title': job_title, 'company': company_name,
                                'salary': salary, 'position': position, 'level': level, 'address': address, 'welfare': welfare_list,
                                'job description': job_des, 'job requirements': job_req, 'link': url}
            
            df = pd.DataFrame([job_details_dict])
            with open(file_path + 'job_scraped_data.csv', 'a', encoding='utf-8', newline='') as f:
                if os.path.getsize(file_path + 'job_scraped_data.csv') == 0:
                    df.to_csv(f, index=False)
                else:
                    df.to_csv(f, mode='a', header=False, index=False)
        
        except WebDriverException as e:
            print(e)
        
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Handle redirects
        if driver.current_url != url:
            return 'redirected'
            
        # Handle cookies
        cookies = driver.get_cookies()
        for cookie in cookies:
            driver.add_cookie(cookie)
            
        html_content = driver.page_source
        job_items = BeautifulSoup(html_content, 'html.parser').find_all('div', class_=['job-item', 'job-item has-badge'])
        job_links = []
        
        for job_item in job_items:
            job_title = job_item.find('a', class_='job_link').text.strip()
            if not re.search(r'data|dữ liệu|business analyst|financial analyst|machine learning', job_title, flags=re.IGNORECASE) or re.search(r'intern|thực tập|tập sự', job_title, flags=re.IGNORECASE):
                continue
            
            company_name = job_item.find('a', class_='company-name').text.strip()
            if not re.search(r'ngân hàng|bank', company_name, flags=re.IGNORECASE):
                continue
            
            job_link = job_item.find('a', class_='job_link')['href']
            job_links.append(job_link)
            
        for job_link in job_links:
            if scrape_details(job_link, driver):
                continue
                
    except WebDriverException as e:
        print(f"Error fetching page {page_number}: {e}")
        if "410" in str(e):
            print(f"Page {page_number} is gone.")
            return True
    except Exception as e2:
        print(e2)

def job_scrape(max_page, place):
    '''
    A function to scrape job data from CareerViet.
    Args:
        max_page (int or "max"): the maximum number of pages you want to scrape data from.
        If "max": the function will scrape data from all the pages there are.
        
        place (str): the city/province for the job. For now, because the project is time-limited, this function only supports major cities.
        If you want to include places other than these cities, check the website for their codes and add the place to the city_code dict.
        Major cities include: ho-chi-minh, ha-noi, quang-ninh, can-tho, hai-phong, da-nang.
        Please make sure the city name input conforms to the format above (city-name).
    '''
    options = Options()
    options.add_argument(f'user-agent={UserAgent().random}')
    options.add_argument("--disable-geolocation")
    options.add_argument('start-maximized')
    driver = webdriver.Edge(options=options)
    
    page_number = 1
    if max_page == 'max':
        success = True
        while success:
            scrape_results = scrape_pages(page_number, place, driver)
            if scrape_results:
                success = False
            # The website automatically redirects to the job postings of your location, so after the redirect, another load is necessary
            elif scrape_results == 'redirected':
                continue
            else:
                page_number += 1
    else:
        while page_number < max_page + 1:
            scrape_results = scrape_pages(page_number, place, driver)
            if scrape_results == 'redirected':
                continue
            else:
                page_number += 1
    
    result_df = pd.read_csv(file_path + 'job_scraped_data.csv', encoding='utf-8')
    driver.quit()
    return result_df

############################################################################################################################################
### Function for sending email
def send_email(df):
    from_email = "your_from_email@gmail.com"
    to_email = "recipient_email@gmail.com"
    password = "your_app_password" # use app password, your actual password won't work (must be set first in your Google account)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Latest Job Listings"

    latest_jobs = df.tail(5) # Can change the argument to control how many jobs the email will sent info about

    body = "Here are the latest data job listings that match your criteria:\n\n"
    for index, row in latest_jobs.iterrows():
        body += f"Title: {row['title']}\n"
        body += f"Company: {row['company']}\n"
        body += f"Salary: {row['salary']}\n"
        body += f"Application Deadline: {row['application deadline']}\n"
        body += f"Link: {row['link']}\n\n"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

############################################################################################################################################
### Schedule the code to run weekly
def job():
    dataframe = job_scrape(max_page=10, place='ha-noi') # Limit the max_page for test run. In a real use case, it's best to set it to 'max'
    send_email(dataframe)
    
# Schedule the job
# schedule.every().day.at("10:00").do(job)  # Uncomment for daily at 10 am
schedule.every().week.do(job)  # Weekly

while True:
    schedule.run_pending()
    time.sleep(1)