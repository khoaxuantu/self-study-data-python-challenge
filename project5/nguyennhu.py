# Great work! But seems like u did not implement the filter, schedule and mail features.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re


def crawl_page(page_url, page_number, retries=3, backoff_factor=2):
    # Step 1: Crawl all jobs in the page
    # 1.1. Get html data
    try:
        page = requests.get(page_url)
        page.raise_for_status()
    except:
        return "Error"
    soup = BeautifulSoup(page.text, "html.parser")

    job = []
    title_blocks = soup.find_all("div", class_="title-block")

    for block in title_blocks:
        # 1.2. Extract job infomation from the listing title (Job title, Company name, Salary, Job location, Date posted, Job link)
        job_link = block.find("a")["href"]
        job_title = block.find("a").text.strip()
        salary = block.find("label", class_="title-salary").text.strip()
        company = block.find_next("a", class_="company").text.strip()
        address = block.find_next("label", class_="address").text.strip()
        date_post = block.find_next("label", class_="deadline").text.strip()

        # 1.3. Extract job information from the listing detail (Job description, Requirement, Benefit, Address, Working time, Employment type)
        job_detail = {
            "Job description": "Mô tả công việc",
            "Requirement": "Yêu cầu ứng viên",
            "Benefit": "Quyền lợi",
            "Address": "Địa điểm làm việc",
            "Working time": "Thời gian làm việc",
        }

        for attempt in range(retries):
            try:
                detail_job = requests.get(job_link)
                detail_job.raise_for_status()

                detail_job_content = BeautifulSoup(detail_job.text, "html.parser")
                for key, value in job_detail.items():
                    section = detail_job_content.find("h3", text=value)
                    if section == None:
                        if value == "Quyền lợi":
                            value = "Quyền lợi được hưởng"
                        try:
                            section_h2 = detail_job_content.find(
                                "h2", class_="title", text=value
                            )
                            content = section_h2.find_next(
                                "div"
                            )  # , class_='content-tab'
                            job_detail[key] = content.get_text(
                                separator="\n", strip=True
                            )
                        except:
                            job_detail[key] = "None"
                    else:
                        content = section.find_next(
                            "div", class_="job-description__item--content"
                        )
                        job_detail[key] = content.get_text(separator="\n", strip=True)
                try:
                    employment_type_tmp = detail_job_content.find(
                        "strong", text="Hình thức làm việc "
                    )
                    employment_type = employment_type_tmp.find_next("span").get_text(
                        strip=True
                    )
                except:
                    employment_type_tmp = detail_job_content.find(
                        "div",
                        class_="box-general-group-info-title",
                        text="Hình thức làm việc",
                    )
                    employment_type = employment_type_tmp.find_next_sibling(
                        "div", class_="box-general-group-info-value"
                    ).get_text(strip=True)
                job_detail.update({"Employment type": employment_type})
            except requests.exceptions.RequestException as e:
                if attempt < retries - 1:
                    wait_time = backoff_factor * (2**attempt)  # Exponential backoff
                    print(
                        f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds..."
                    )
                    time.sleep(wait_time)
                else:
                    print(
                        f"Failed to fetch job details for {job_link} after {retries} attempts: {e}"
                    )
                    continue
        # 1.4. Add job items to job list
        try:
            job_item = {
                "Job title": job_title,
                "Company name": company,
                "Salary": salary,
                "Job location": address,
                "Date posted": date_post,
                "Job link": job_link,
            }
        except:
            print(job_link)
        job_item.update(job_detail)
        job.append(job_item)

    # Step 2: Add/ Update job to csv file
    df = pd.DataFrame(job)
    df["Job id"] = df["Job link"].apply(
        lambda x: re.search(r"(\d+)\.html?", x).group(1)
    )
    if page_number == 1:
        df.to_csv("job.csv", index=False, quoting=1)
    else:
        df.to_csv("job.csv", mode="a", index=False, quoting=1, header=False)


def check_call_page(url):
    try:
        page = requests.get(url)
        page.raise_for_status()
        return "Success"
    except:
        return "Error"


# Multiple page
original_board_page = "https://www.topcv.vn/viec-lam-it?sort=&skill_id=&skill_id_other=&keyword=&company_field=&position=&salary="
i = 1
board_page = original_board_page
while check_call_page(board_page) != "Error":
    crawl_page(page_url=board_page, retries=3, backoff_factor=2, page_number=i)
    i += 1
    board_page = original_board_page + f"&page={i}"
