# Very great work!

import requests
from bs4 import BeautifulSoup
import re
import csv
import schedule
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email_with_smtp(subject, body, to_email, file_path):
    print(f"Sending email to {to_email}...")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "abc@xyz.com"
    sender_password = "MASK_PASSWORD"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=file_path)
    part["Content-Disposition"] = f'attachment; filename="{file_path}"'
    message.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Hàm thu thập thông tin chi tiết của công việc
def fetch_job_details(job_id):
    job_url = f"https://topdev.vn/detail-jobs/-{job_id}"
    response = requests.get(job_url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one("#detailJobHeader h1").get_text()
    job_description = (
        soup.select_one("#JobDescription .prose")
        .get_text(separator=" ")
        .replace("  ", " ")
    )

    general_info = soup.find("h2", string="General information")
    extra_info = general_info.find_next_sibling("div") if general_info else None

    if extra_info:
        items = extra_info.find_all("div", class_="item-card-info")
        for item in items:
            job_description += " " + item.get_text(separator=" ").strip()

    return job_description


# Hàm tìm kiếm công việc và lọc kết quả
def fetch_jobs(num_pages, language_keywords, include_keywords, exclude_keywords):
    job_listings = []
    language_regex = re.compile(
        r"\b(" + "|".join(language_keywords) + r")\b", re.IGNORECASE
    )
    include_keywords_regex = re.compile(
        r"\b(" + "|".join(include_keywords) + r")\b", re.IGNORECASE
    )
    exclude_keywords_regex = re.compile(
        r"\b(" + "|".join(exclude_keywords) + r")\b", re.IGNORECASE
    )

    for page in range(1, num_pages + 1):
        url = f"https://api.topdev.vn/td/v2/jobs?keyword=&region_ids=&skills_id=&industries_ids=&job_levels_ids=&job_types_ids=&contract_types_ids=&salary_range=&experiences_id=&ordering=newest_job&_f=39127&page={page}&page_size=15&locale=vi_VN&fields[job]=id,title,salary,slug,company,extra_skills,skills_str,skills_arr,skills_ids,job_types_str,job_levels_str,job_levels_arr,job_levels_ids,addresses,status_display,detail_url,job_url,salary,published,refreshed,applied,candidate,requirements_arr,packages,benefits,content,features,contract_types_ids,is_free,is_basic,is_basic_plus,is_distinction&fields[company]=tagline,addresses,skills_arr,industries_arr,industries_ids,industries_str,image_cover,image_galleries,num_job_openings,company_size,nationalities_str,skills_str,skills_ids,benefits,num_employees&locale=vi_VN"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and data["data"]:
                jobs = data["data"]
                for job in jobs:
                    job_id = job.get(
                        "id"
                    )  # Sử dụng get() để lấy giá trị id an toàn hơn
                    if job_id:
                        description = fetch_job_details(job_id)
                        description += job.get("job_levels_str", "") + job.get(
                            "skills_str", ""
                        )

                        if (
                            language_regex.search(description)
                            and include_keywords_regex.search(description)
                            and not exclude_keywords_regex.search(description)
                        ):
                            print(f"Tìm thấy: {job.get('title', 'No Title')}")
                            job_listings.append(
                                {
                                    "Title": job.get("title", "No Title"),
                                    "Company": job.get("company", {}).get(
                                        "display_name", "Unknown"
                                    ),
                                    "Location": job.get("addresses", {}).get(
                                        "full_addresses", ["Unknown"]
                                    )[0],
                                    "Description": description,
                                    "Date Posted": job.get("published", {}).get(
                                        "date", "Unknown"
                                    ),
                                    "Link": job.get("detail_url", "#"),
                                }
                            )

    return job_listings


# Hàm lưu công việc vào file CSV
def save_jobs_to_csv(job_listings, file_path):
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Title",
                "Company",
                "Location",
                "Description",
                "Date Posted",
                "Link",
            ],
        )
        writer.writeheader()
        for job in job_listings:
            writer.writerow(job)
    print(f"Đã lưu {len(job_listings)} công việc vào {file_path}")


# Hàm tổng hợp và chạy toàn bộ quy trình
def run_job_search(
    num_pages, language_keywords, include_keywords, exclude_keywords, to_email
):
    print("Start running")
    job_listings = fetch_jobs(
        num_pages, language_keywords, include_keywords, exclude_keywords
    )
    if job_listings:
        file_path = "job_listings_test.csv"
        save_jobs_to_csv(job_listings, file_path)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bodyMail = (
            f"{current_time} Tìm kiếm công việc với các tiêu chí:\n"
            f"Có chứa các Ngôn ngữ lập trình: {', '.join(language_keywords)}\n"
            f"Chứa các từ khoá: {', '.join(include_keywords)}\n"
            f"Và không chứa: {', '.join(exclude_keywords)}"
        )
        send_email_with_smtp(
            f"Thu thập dữ liệu từ website Topcv.vn {current_time}",
            bodyMail,
            to_email,
            file_path,
        )


# Thiết lập lịch trình chạy
num_pages = 1
language_keywords = ["Python"]
include_keywords = ["Middle", "fulltime"]
exclude_keywords = ["internship", "parttime"]
to_email = "abc@xyz.com"  # Bruh don't send me your email -_-
run_time = "22:50"
print(f"Tác vụ sẽ chạy vào lúc: {run_time}")
schedule.every().day.at(run_time).do(
    lambda: run_job_search(
        num_pages, language_keywords, include_keywords, exclude_keywords, to_email
    )
)
while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Đang chờ chạy tác vụ: {current_time}")
    schedule.run_pending()
    time.sleep(1)
