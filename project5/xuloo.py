# Great work! WHERE IS PAGINATION????????????????????????

import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import logging
import schedule
import json
import csv
import re
from typing import Final

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GetInformation:
    def __init__(self, URL: str, level: str, typeJob: str, COOKIE: str):
        self.URL = URL
        self.level = level
        self.typeJob = typeJob
        self.COOKIE = COOKIE
        self.allJob = self.getJobContainer()

    def getJobContainer(self):
        try:
            res = requests.get(f"{self.URL}/{self.typeJob}+{self.level}-k", cookies={'Cookie': self.COOKIE})
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup.find_all('div', class_='flex items-start justify-between gap-6 p-4')
        except Exception as e:
            logging.error(f"Failed to retrieve job container for level {self.level}: {e}")
            return []

    def get_Job(self):
        jobs = []
        links = []
        companys = []
        levelInfor = []
        locations = []
        descriptions = []
        dates = []
        tags = []
        imgs = []

        for container in self.allJob:
            title = container.find('h3', class_='line-clamp-1')
            if title:
                jobs.append(title.text.strip())
                link = "https://topdev.vn/" + title.find('a')['href']
                links.append(link)
            # ---------------------

            company = container.find('a', class_='text-gray-600 transition-all hover:text-primary')
            companys.append(company.text.strip() if company else 'N/A')
            # ---------------------

            level = container.find('div', class_='mt-2 flex items-center justify-start gap-5')
            levelInfor.append(level.text.strip() if level else 'N/A')
            # ---------------------

            location = container.find('div', class_='flex flex-wrap items-end gap-2 text-gray-500')
            locations.append(location.text.strip() if location else 'N/A')
            # ---------------------

            description_div = container.find('ul', class_='ml-6 list-disc text-gray-600')
            if description_div:
                descriptions_list = tuple(li.text.strip() for li in description_div.find_all('li'))
                descriptions.append(descriptions_list)
            else:
                descriptions.append('N/A')
            # ---------------------

            date = container.find('p', class_='whitespace-nowrap text-sm text-gray-400')
            dates.append(date.text.strip() if date else time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # ---------------------

            tag = container.find_all('div', class_='line-clamp-1')
            if tag and len(tag) > 1:
                tags.append(tuple(a.text.strip() for a in tag[1].find_all('a')))
            else:
                tags.append(())
            
            img = container.find('img')
            imgs.append(img['src'] if img else '')

        return jobs, links, companys, levelInfor, locations, descriptions, dates, tags, imgs

    def moveToCSV(self):
        title, link, company, level, location, description, date, tag, img = self.get_Job()

        try:
            try:
                df_exist = pd.read_csv('data.csv')
                exittings_job = df_exist['Title'].values
            except FileNotFoundError:
                df_exist = pd.DataFrame()
                exittings_job = set()

            data = {
                "Title": title,
                "Link": link,
                "Company": company,
                "Level": level,
                "Location": location,
                "Description": description,
                "Date": date,
                "Tag": tag,
                "Img": img,
                "Check Discord": [False] * len(title),
                "Check Spreadsheet": [False] * len(title)
            }

            df_new = pd.DataFrame(data)
            df_new = df_new[~df_new['Title'].isin(exittings_job)]

            if not df_new.empty:
                df_update = pd.concat([df_exist, df_new], ignore_index=True)
                df_update.to_csv('data.csv', index=False)
                logging.info(f"{len(df_new)} new jobs added to data.csv")
                return True
            else:
                logging.info("No new jobs found")
                return False

        except Exception as e:
            logging.error(f"Error moving data to CSV: {e}")
            return False

class NotiDiscord:
    def __init__(self, webhook, config_path, URL_WEB_TOPDEV) -> None:
        self.webhook = webhook
        self.config = self.load_config(config_path)
        self.URL_WEB_TOPDEV = URL_WEB_TOPDEV

    def load_config(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def filter_data(self, data):
        filtered_data = []
        location_pattern = self.config['Location']
        level_pattern = self.config['Level']

        for row in data:
            if re.search(location_pattern, row['Location'], re.IGNORECASE) and \
               re.search(level_pattern, row['Level'], re.IGNORECASE):
                filtered_data.append(row)
        
        return filtered_data

    def send_msg(self, title, message, img_url, role_tag=None):
        data = {
            "username": "Job Bot",
            "content": f"{role_tag}" if role_tag else title,
            "embeds": [
                {
                    "title": title,
                    "description": message,
                    "color": 16711680,
                    "thumbnail": {
                        "url": img_url
                    }
                }
            ]
        }
        try:
            res = requests.post(self.webhook, json=data)
            res.raise_for_status()
            logging.info(f"Message sent successfully: {res.text}")
        except Exception as err:
            logging.error(f"Failed to send message: {err}")

    def notify_from_csv(self, csv_path):
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            filtered_data = self.filter_data(reader)
            
            for row in filtered_data:
                title = row['Title']
                message = (
                        f"**Company:** [{row['Company']}]({self.URL_WEB_TOPDEV}{row['Link']})\n"
                        f"**Level:** {row['Level']}\n"
                        f"**Location:** {row['Location']}\n"
                        f"**Date Posted:** {row["Date"]}\n"
                        f"**Tags:** {row['Tag']}\n\n"
                        f"**Description:**\n{row['Description']}"
                    )
                # tag = row.get('Tag', None)
                # tag = row['Tag']
                img_url = row.get('Img', None)
                self.send_msg(title, message, img_url, role_tag=None)

                # Mark the job as sent in the CSV file
                logging.info(f"Notification sent for: {title}")


def load_config(path):
    with open(path, 'r') as file:
        config = json.load(file)
    return config.get('typeJob', 'data')  # Mặc định là 'data' nếu không tìm thấy

def job():
    URL = "https://topdev.vn/viec-lam-it"
    COOKIE: Final = ''  # Không cần thiết
    WEBHOOK: Final = ''  # Bắt buộc
    CONFIG_PATH: Final = 'config.json' '''tạo file config.json: {"typeJob": "data", "Location": "Hà Nội", "Level": "junior"}'''
    URL_WEB_TOPDEV: Final = "https://topdev.vn"

    listLevel = [
        "internship", "fresher", "junior", "senior", "truong-nhom", "truong-phong"]
    # typeJob = input("Keyword for JOBS: ")
    typeJob = load_config(CONFIG_PATH)

    for lv in listLevel:
        logging.info(f"Processing jobs for level: {lv}")
        try:
            getInfor = GetInformation(URL, lv, typeJob, COOKIE)
            getInfor.moveToCSV()
        except Exception as e:
            logging.error(f"Error in processing level {lv}: {e}")

    try:
        discord = NotiDiscord(WEBHOOK, CONFIG_PATH, URL_WEB_TOPDEV)
        discord.notify_from_csv('data.csv')
    except Exception as e:
        logging.error(f"Error sending Discord notifications: {e}")

if __name__ == '__main__':
    print("Running the job...")
    schedule.every(1).hours.do(job)
    # set 24h
    # schedule.every().day.at("06:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

