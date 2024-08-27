import requests
from bs4 import BeautifulSoup
import re
import csv
import schedule
import time
import time
from datetime import datetime

def send_email_with_mailgun(subject, body, to_email, file_path):
    api_key = "<<API_KEY_MASK>>" # Don't send me your API key sis -_-
    domain_name = "a_domain.com.vn"
    url = f"https://api.mailgun.net/v3/{domain_name}/messages"

    with open(file_path, 'rb') as attachment:
        files = {
            "attachment": (file_path, attachment.read())
        }

        data = {
            "from": f"Tự động thu thập <mailgun@{domain_name}>",
            "to": to_email,
            "subject": subject,
            "text": body
        }

        response = requests.post(
            url,
            auth=("api", api_key),
            files=files,
            data=data
        )

    if response.status_code == 200:
        print("Email đã được gửi thành công!")
    else:
        print(f"Gửi email không thành công. Mã lỗi: {response.status_code}, Nội dung: {response.text}")

def send_discord_message(message,file_path):
    webhook_url = '<<DISCORD_WEBHOOK_URL_MASK>>' # Don't public your discord app webhook
    with open(file_path, 'rb') as file:
        data = {
            "content": message,
            "username": "Your Bot Name"
        }
        files = {
            "file": (file_path, file.read())
        }
    response = requests.post(webhook_url, data=data, files=files)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def fetch_job(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one('#detailJobHeader h1').get_text()
    JobDescription = soup.select_one('#JobDescription .prose').get_text('').replace("\n", " ").replace("  ", " ")
    General_info = soup.find('h2', string='General information')
    extra = General_info.next_sibling
    items = extra.find_all('div', class_='item-card-info')
    for item in items:
        text = item.find('div').get_text(separator="").strip()
        JobDescription += ' ' +text
    return  ''+JobDescription+''

def fetch_jobs(num_pages, languages, required_keywords, excluded_keywords,to_email):
    job_listings = []
    language_regex = re.compile(r'\b(' + '|'.join(language_keywords) + r')\b', re.IGNORECASE)
    include_keywords_regex = re.compile(r'\b(' + '|'.join(include_keywords) + r')\b', re.IGNORECASE)
    exclude_keywords_regex = re.compile(r'\b(' + '|'.join(exclude_keywords) + r')\b', re.IGNORECASE)
    for page in range(1, num_pages + 1):
        url = f"https://api.topdev.vn/td/v2/jobs?keyword=&region_ids=&skills_id=&industries_ids=&job_levels_ids=&job_types_ids=&contract_types_ids=&salary_range=&experiences_id=&ordering=newest_job&_f=39127&page=2&page_size=15&locale=vi_VN&fields[job]=id,title,salary,slug,company,extra_skills,skills_str,skills_arr,skills_ids,job_types_str,job_levels_str,job_levels_arr,job_levels_ids,addresses,status_display,detail_url,job_url,salary,published,refreshed,applied,candidate,requirements_arr,packages,benefits,content,features,contract_types_ids,is_free,is_basic,is_basic_plus,is_distinction&fields[company]=tagline,addresses,skills_arr,industries_arr,industries_ids,industries_str,image_cover,image_galleries,num_job_openings,company_size,nationalities_str,skills_str,skills_ids,benefits,num_employees"
        # Gửi yêu cầu HTTP đến trang web
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['data']:
                jobs = data['data']
                for job in jobs:
                    soup = BeautifulSoup(job['content'], "html.parser")
                    description = fetch_job("https://topdev.vn/detail-jobs/-" +str(job['id']))
                    description += job['job_levels_str'] + job['skills_str']
                    if (language_regex.search(description) and
                        include_keywords_regex.search(description) and
                        not exclude_keywords_regex.search(description)):
                        print ('Tìm thấy: '+job['title'])
                        # Thêm công việc vào danh sách nếu tất cả tiêu chí đều đạt
                        job_listings.append({
                            'Title': job['title'],
                            'Company': job['company']['display_name'],
                            'Location': job['addresses']['full_addresses'][0],
                            'Description': description,
                            'Date Posted': job['published']['date'],
                            'Link': job['detail_url'],
                        })

    # Lưu thông tin vào file CSV
    file_path = "job_listings.csv"
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Company', 'Location', 'Description', 'Date Posted', 'Link'])
        writer.writeheader()
        for job in job_listings:
            writer.writerow(job)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bodyMail = (
    current_time+ " Tìm kiếm công việc với các tiêu chí: "
    "Có chứa các Ngôn ngữ lập trình: " + ', '.join(language_keywords) +
    " | Chứa các từ khoá: " + ', '.join(include_keywords) +
    " | Và không chứa: " + ', '.join(exclude_keywords)
    )
    send_email_with_mailgun("Thu thập dữ liệu từ website Topcv.vn "+current_time,bodyMail, to_email, file_path)
    time.sleep(0.1)
    send_discord_message(bodyMail,file_path)

# Sử dụng function với các tiêu chí lọc
num_pages = 1
language_keywords = ["Python"]
include_keywords = ["Middle", "fulltime"]
exclude_keywords = ["internship", "parttime"]

#Chuyển data vào email
to_email='<<EMAIL_MASK>>' # Don't send me your email sis -_-
run_time = "23:56"
print(f"Tác vụ sẽ chạy vào lúc: {run_time}")
schedule.every().day.at(run_time).do(lambda: fetch_jobs(num_pages, language_keywords, include_keywords, exclude_keywords, to_email))
while True:
    # Kiểm tra và thực hiện các tác vụ đã lên lịch
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"dang cho chay : {current_time}")
    schedule.run_pending()
    time.sleep(1)
