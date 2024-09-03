# Great work, but seems like you didn't implement the filter function as well as bonus point features.

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import datetime
import requests
import time
from datetime import datetime

url = "https://topdev.vn/it-jobs?src=topdev_home&medium=newjobs"

driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

jds = soup.main.find("ul", class_="mt-4").find_all("li", recursive=False)

cols = ["title", "Company", "Location", "Job link", "Description", "Date posted"]
global df
df = pd.DataFrame(columns=cols)
date = datetime.now().strftime("%Y-%m-%d")


def scrawl_data(jds):
    for jd in jds:
        if jd.find("a"):
            if (
                "hours"
                in jd.find("p", class_="whitespace-nowrap text-sm text-gray-400").text
            ):
                new_url = "https://topdev.vn" + jd.find("a")["href"]
                page = requests.get(new_url)
                soup = BeautifulSoup(page.content, "html.parser")
                title = soup.h1.text
                link = new_url
                company = soup.p.text
                location = soup.find(
                    "div", class_="w-3/4 flex flex-initial flex-col"
                ).div.div.div.text.split(", ")[-1]
                description = soup.find("div", id="JobDescription").text.replace(
                    "\n", ". "
                )[30:]
                df.loc[len(df)] = [title, company, location, link, description, date]
            else:
                break


scrawl_data(jds=jds)

for i in range(3):
    driver.execute_script('window.scrollTo({ top: 4000, behavior: "smooth"});')
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

jds = (
    soup.main.find("ul", class_="mt-4")
    .find_all("div", recursive=False)[-1]
    .ul.find_all("li", recursive=False)
)

scrawl_data(jds=jds)

print(df)
