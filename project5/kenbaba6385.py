# Gerat work! But seems like you did not implement pagination and schedule features.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

url = "https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu"

jobs_data = []

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

for job in soup.find_all("li", "mb-4 last:mb-0"):
    try:
        job_title_tags = job.find_all(
            "a",
            class_=[
                "text-lg font-bold transition-all text-primary",
                "text-lg font-bold transition-all hover:text-primary",
            ],
        )

        # Lấy nội dung văn bản từ các thẻ <a>
        job_title = " ".join([tag.text for tag in job_title_tags])

        company_name = job.find(
            "a", "text-gray-600 transition-all hover:text-primary"
        ).text

        date_posted = job.find("p", "whitespace-nowrap text-sm text-gray-400").text

        locations = job.find("div", "flex flex-wrap items-end gap-2 text-gray-500")

        job_location = locations.find("p").text

        job_link = job.find("a", "block h-[7.5rem] w-[10rem]")["href"]
        job_link = job_link.replace("/vi/viec-lam", "https://topdev.vn/viec-lam")

        page1 = requests.get(job_link)
        soup1 = BeautifulSoup(page1.text, "html.parser")

        links = soup1.find_all(
            "a", class_="text-sm hover:text-primary-300 hover:underline md:text-base"
        )[1:]
        # Tạo một danh sách các giá trị văn bản từ các thẻ <a>
        text_list = [link.text for link in links]
        # Kết hợp các giá trị thành một chuỗi, loại bỏ dấu ngoặc vuông
        experience_level = ", ".join(text_list)

        skills = soup1.find_all("a", "mr-2 inline-block")
        text_list1 = [skill.text for skill in skills]
        tech_stack = ", ".join(text_list1)

        jobs_data.append(
            {
                "Job Title": job_title,
                "Company name": company_name,
                "Job Location": job_location,
                "Job Decription": experience_level,
                "Tech stack": tech_stack,
                "Date Posted": date_posted,
                "Job Link": job_link,
            }
        )

        # Tạo DataFrame
        df = pd.DataFrame(jobs_data)
    except AttributeError:
        continue
print(df)
df.to_csv("job_listings.csv")

# print("Filtered jobs based on the keyword '{}':".format(keyword))
# filtered_df.to_csv('filter_list.csv')
# print(filtered_df)


def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = "<<EMAIL_MASK>>"  # Don't public your email to me bruh
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)  # smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login("<<EMAIL_MASK>>", "Kenbaba!")
    server.sendmail(
        "<<EMAIL_MASK>>", to_email, msg.as_string()
    )  # (sender_email, receiver_email, message.as_string())
    server.quit()


to_email = input("Enter your email address to receive notifications: ")

keyword = input(
    "Enter the one or more keyword to filter jobs (e.g.fulltime tester or junior html): "
)


# keyword.split(): Tách chuỗi keyword thành một danh sách các từ, sử dụng dấu cách (" ") làm dấu phân cách.
# keyword.strip(): Loại bỏ khoảng trắng thừa ở đầu và cuối mỗi từ trong danh sách.
keywords = [keyword.strip() for keyword in keyword.split()]

# Nối các từ trong danh sách keywords lại với nhau
pattern = "|".join(keywords)

# Lọc DataFrame dựa trên từ khóa
filtered_df = df[
    df["Job Decription"].str.contains(pattern, flags=re.I, regex=True)
    | df["Tech stack"].str.contains(pattern, flags=re.I, regex=True)
]

# Kiểm tra xem có việc làm mới phù hợp hay không
if len(filtered_df) > 0:
    # Tạo nội dung email
    subject = "New job postings that match your criteria"
    body = "We found some new job postings that match your criteria:\n\n"
    body += filtered_df.to_string()

    # Gửi email
    send_email(to_email, subject, body)
    print(f"Email notification has been sent to {to_email}")
    filtered_df.to_csv("filter_list.csv")
else:
    print("No new job postings match your criteria.")
