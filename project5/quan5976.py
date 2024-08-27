import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re
import smtplib
import getpass
import schedule
import time

def scrape_jobs():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    # Tạo danh sách để lưu trữ thông tin công việc
    filtered_jobs = []

    # Lặp qua các trang để lấy thông tin công việc
    for page in range(1, 21):  # Lấy thông tin từ 10 trang đầu tiên
        driver.get(f'https://www.vietnamworks.com/viec-lam?q=it&page={page}')
        sleep(3)  #    Đợi 3 giây để trang web tải hoàn toàn

        # Lấy mã nguồn HTML của trang web
        web = driver.page_source
        soup = BeautifulSoup(web, 'html.parser')

        # Tìm container chứa danh sách công việc
        job_data = soup.find('div', class_='block-job-list')
        if job_data:
            # Lấy danh sách các công việc
            job_items = job_data.find_all('div', class_='sc-fwwElh iAsyDt')
            print(f"Found {len(job_items)} job listings on page {page}")

            for job in job_items:
                try:
                    job_title = job.find('h2').text.strip() if job.find('h2') else None
                    company_name = job.find('div', class_='sc-hybRYi iVjhps').text.strip() if job.find('div', class_='sc-hybRYi iVjhps') else None
                    location = job.find('span', class_='sc-evdWiO hRDCRg').text.strip() if job.find('span', class_='sc-evdWiO hRDCRg') else None
                    date_posted = job.find('div', class_='sc-lmJFLr eJkRTg').text.strip() if job.find('div', class_='sc-lmJFLr eJkRTg') else None
                    salary = job.find('span', class_='sc-gQSkpc cXNeHq').text.strip() if job.find('span', class_='sc-gQSkpc cXNeHq') else 'Thương lượng'
                    skills = job.find_all('label', class_='sc-dxcDKg RKGYC sc-ERObt jKzuwy')
                    list_skills = [skill.text for skill in skills]
                    job_link = "https://www.vietnamworks.com" + job.find('a', href=True)['href'] if job.find('a', href=True) else None

                    # Lọc theo ngôn ngữ lập trình
                    required_languages = ['Python', 'JavaScript']
                    found_languages = False
                    languages = job.find_all('label', class_='sc-dxcDKg RKGYC sc-ERObt jKzuwy')
                    for label in languages:
                        for language in required_languages:
                            if re.search(language, label.text, re.IGNORECASE):
                                found_languages = True
                                break

                    if not found_languages:
                        continue  # Bỏ qua nếu không có ngôn ngữ yêu cầu

                    # Lọc theo từ khóa trong tiêu đề
                    # include_keywords = ['remote', 'full-time']
                    # exclude_keywords = ['internship', 'part-time']

                    # if not any(re.search(keyword, job_title, re.IGNORECASE) for keyword in include_keywords):
                    #     continue  # Bỏ qua nếu không có từ khóa mong muốn

                    # if any(re.search(keyword, job_title, re.IGNORECASE) for keyword in exclude_keywords):
                    #     continue  # Bỏ qua nếu có từ khóa không mong muốn

                    filtered_jobs.append({
                        'Job Title': job_title,
                        'Company Name': company_name,
                        'Location': location,
                        'Date Posted': date_posted,
                        'Salary': salary,
                        'Skills': ', '.join(list_skills),  # Chuyển đổi danh sách kỹ năng thành chuỗi
                        'Job Link': job_link
                    })
                except Exception as e:
                    print(f"Error processing job: {e}")
        else:
            print("Could not find job list container")

    # Lưu dữ liệu công việc vào tệp CSV
    csv_file = "vietnamworks_job_listings.csv"
    csv_columns = ['Job Title', 'Company Name', 'Location', 'Date Posted', 'Salary', 'Skills', 'Job Link']

    try:
        with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writeheader()
            for job in filtered_jobs:
                writer.writerow(job)
        print(f'Data has been saved to {csv_file}')
    except IOError:
        print("Error while saving to CSV file")

    # Chuẩn bị nội dung email
    email_content = f"Found {len(filtered_jobs)} new job listings:\n\n"
    for job in filtered_jobs:
        email_content += f"Title: {job['Job Title']}\n"
        email_content += f"Company: {job['Company Name']}\n"
        email_content += f"Location: {job['Location']}\n"
        email_content += f"Posted: {job['Date Posted']}\n"
        email_content += f"Salary: {job['Salary']}\n"
        email_content += f"Skills: {job['Skills']}\n"
        email_content += f"Link: {job['Job Link']}\n\n"

    # Gửi email thông báo
    sender_email = "xxxx@gmail.com" # Don't send me your email bruh
    receiver_email = "xxxx@gmail.com"
    subject = "Latest Job Listings"
    # password = getpass.getpass('Enter your email password: ') #App passwords
    password = "<<PASSWORD_MASK>>" #App passwords
    # Don't send me your password
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()  # Enable security
        session.login(sender_email, password)

        # Gửi email
        message = f'Subject: {subject}\n\n{email_content}'.encode('utf-8')
        session.sendmail(sender_email, receiver_email, message)
        session.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f"Error sending email: {e}")

# Chạy hàm scrape_jobs()
scrape_jobs()
# Mở chú thích để chạy ạ

# Schedule the job to run daily at 10:00 AM
# schedule.every().day.at("10:00").do(scrape_jobs)

# # Keep the script running
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Check every minute
