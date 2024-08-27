import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://jobsgo.vn/viec-lam.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

def extract_job_data(job_item):
  """Trích xuất một item chứa thông tin 1 job"""
  # Tìm tất cả các phần tử trong item
  job_items = soup.find_all('div', class_='brows-job-position')
  
  # Trích xuất tiêu đề công việc
  job_title = job_item.find('h3').find('a').text.strip()
  job_title = job_title.strip()
  if job_title.startswith('-'):
      job_title = job_title[1:]
  job_title = re.sub(r"\[.*?\]", "", job_title)
  job_title = job_title.replace("_", "")

  # Trích xuất tên công ty
  company = job_item.find('p', class_='font-13').find('a').text.strip()

  # Trích xuất thông tin chi tiết
  details = job_item.find_all('p', class_='font-12')
  location = details[0].find('span', title=True)['title'].split(':')[1].strip()
  salary = details[0].find_all('span')[1]['title'].split(':')[1].strip()
  job_type = details[0].find_all('span')[2]['title'].split(':')[1].strip()
  experience = details[1].find('span', title=True)['title'].split(':')[1].strip()
  posting_time = details[1].find_all('span')[1]['title'].split(':')[1].strip()

  return {
      "Job Title": job_title,
      "Company": company,
      "Location": location,
      "Salary": salary,
      "Job Type": job_type,
      "Experience": experience,
      "Posting Time": posting_time,
  }
def scrape_jobs(starting_url, max_pages=10):
  all_jobs = []
  page_number = 1
  while page_number <= max_pages:
    url = f"{starting_url}?page={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Tìm tất cả các phần tử công việc
    job_items = soup.find_all('div', class_='brows-job-position')

    # Trích xuất thông tin từng công việc
    for job_item in job_items:
      job_data = extract_job_data(job_item)
      all_jobs.append(job_data)
      print(job_data)
      print("-" * 20)

    # Tăng số trang
    page_number += 1

  return all_jobs

# URL trang đầu tiên
starting_url = 'https://jobsgo.vn/viec-lam.html'

# Trích xuất dữ liệu đến trang 10
all_jobs = scrape_jobs(starting_url, max_pages=10)

# Lưu dữ liệu vào file CSV
with open('jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
  fieldnames = ['Job Title', 'Company', 'Location', 'Salary', 'Job Type', 'Experience', 'Posting Time']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(all_jobs)