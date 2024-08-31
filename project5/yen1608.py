# Great work! But seems like u did not implement filter function.

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import re
import schedule
import time


def send_email_with_smtp(subject, body, to_email, file_path):
    print(f"Sending email to {to_email}...")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "xxxx@gmail.com"  # Don't send me your email sis -.-
    sender_password = "<<PASSWORD_MASK>>"  # Don't send me your password

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


def fetch_job_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    description = soup.select_one("#JobDescription .prose").get_text("")
    minimum_experience = (
        soup.find("h3", string="Năm kinh nghiệm tối thiểu").find_next("a").text.strip()
    )
    level = soup.find("h3", string="Cấp bậc").find_next("a").text.strip()
    type_w = soup.find("h3", string="Loại hình").find_next("a").text.strip()
    type_c = soup.find("h3", string="Loại hợp đồng").find_next("a").text.strip()
    skills = soup.find("h3", string="Các công nghệ sử dụng").find_next("a").text.strip()
    return (
        description,
        minimum_experience,
        level,
        type_w,
        type_c,
        skills,
        (
            description
            + " "
            + minimum_experience
            + " "
            + level
            + " "
            + type_w
            + " "
            + type_c
            + " "
            + skills
        ),
    )


def fetch_topdev_jobs(max_pages=5, jobs_per_page=20):
    print("Fetching jobs from TopDev...")
    all_jobs = []

    for page in range(1, max_pages + 1):
        url = f"https://api.topdev.vn/td/v2/jobs?keyword=&region_ids=&skills_id=&industries_ids=&job_levels_ids=&job_types_ids=&contract_types_ids=&salary_range=&experiences_id=&ordering=newest_job&_f=39127&page={page}&page_size={jobs_per_page}&locale=vi_VN&fields[job]=id,title,salary,slug,company,extra_skills,skills_str,skills_arr,skills_ids,job_types_str,job_levels_str,job_levels_arr,job_levels_ids,addresses,status_display,detail_url,job_url,salary,published,refreshed,applied,candidate,requirements_arr,packages,benefits,content,features,contract_types_ids,is_free,is_basic,is_basic_plus,is_distinction&fields[company]=tagline,addresses,skills_arr,industries_arr,industries_ids,industries_str,image_cover,image_galleries,num_job_openings,company_size,nationalities_str,skills_str,skills_ids,benefits,num_employees&locale=vi_VN"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            jobs = data.get("data", [])
            all_jobs.extend(jobs)

            print(f"Fetched page {page} with {len(jobs)} jobs")

            if len(jobs) < jobs_per_page:
                print("Reached the end of available jobs")
                break

        except requests.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break

    return all_jobs


def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(strip=True)


def format_date(date_str, input_format="%Y-%m-%d", output_format="%Y-%m-%d"):
    try:
        return datetime.strptime(date_str, input_format).strftime(output_format)
    except ValueError:
        return datetime.now().strftime(output_format)


def save_jobs_to_csv(jobs, filename):
    language_regex = re.compile(r"\b(" + "|".join(["Python"]) + r")\b", re.IGNORECASE)
    include_keywords_regex = re.compile(
        r"\b(" + "|".join(["Fulltime"]) + r")\b", re.IGNORECASE
    )
    exclude_keywords_regex = re.compile(
        r"\b(" + "|".join(["intern"]) + r")\b", re.IGNORECASE
    )

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Title",
                "Link",
                "Company",
                "Level",
                "Location",
                "Description",
                "Date",
                "Tag",
                "Img",
                "Time Update",
            ]
        )

        for job in jobs:
            title = job.get("title", "")
            job_id = job.get("id", "")

            link = f"https://topdev.vn/viec-lam/{job_id}" if job_id else ""
            company = job.get("company", {}).get("display_name", "")
            addresses = job.get("addresses", {}).get("full_addresses", [])
            location = ", ".join(addresses) if addresses else ""
            (
                description,
                minimum_experience,
                level,
                type_w,
                type_c,
                skills,
                description_regex,
            ) = fetch_job_details(link)
            date = format_date(job.get("published", {}).get("date", ""))
            skills = job.get("skills_str", "")
            img = job.get("company", {}).get("image_logo", "")
            time_update = format_date(
                job.get("refreshed", {}).get("date", ""),
                input_format="%Y-%m-%d %H:%M:%S",
                output_format="%Y-%m-%d %H:%M:%S",
            )
            if (
                language_regex.search(description_regex)
                and include_keywords_regex.search(description_regex)
                and not exclude_keywords_regex.search(description_regex)
            ):
                print("Find job: " + title)
                writer.writerow(
                    [
                        title,
                        link,
                        company,
                        level,
                        location,
                        description,
                        date,
                        skills,
                        img,
                        time_update,
                    ]
                )

        print(f"Saved {len(jobs)} jobs to {filename}")


def job():
    print("Starting job execution...")
    max_pages = 5
    jobs_per_page = 20

    jobs = fetch_topdev_jobs(max_pages, jobs_per_page)
    if jobs:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"topdev_jobs_{current_time}"
        file_path = f"{file_name}.csv"
        save_jobs_to_csv(jobs, file_path)

        # send email
        subject = f"TopDev Jobs Report - {current_time}"
        body = f"Attached is the latest TopDev jobs report. Total jobs: {len(jobs)}"
        to_email = "xxxx@gmail.com"
        send_email_with_smtp(subject, body, to_email, file_path)
    else:
        print("No jobs were fetched. Please check your connection or the API status.")

    print("Job execution completed.")


def run_schedule():
    print("Starting scheduler...")
    schedule.every().day.at("23:25").do(job)  # Chạy job hàng ngày lúc 10:00 AM

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_schedule()
