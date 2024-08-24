# Great work!

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import datetime
import time
from tabulate import tabulate


def fetch_data():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    with webdriver.Chrome(options=options) as driver:
        driver.get(
            f"https://coinmarketcap.com/?nocache={datetime.datetime.now().timestamp()}"
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        soup = BeautifulSoup(driver.page_source, "html.parser")
        target_cryptos = ["BitcoinBTC", "EthereumETH", "BNBBNB"]
        data = [
            [get_column_text(column) for column in row.find_all("td")[2:-2]]
            + [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            for row in soup.find("table", {"class": "cmc-table"}).find_all("tr")[1:]
            if row.find_all("td")[2].text in target_cryptos
        ]
    return data


def get_column_text(column):
    if column.find("p"):
        spans = column.find("p").find_all("span")
        return spans[1].text if len(spans) > 1 else column.find("p").text.strip()
    else:
        bearish_trend = column.find("span", class_="icon-Caret-down")
        return "-" + column.text.strip() if bearish_trend else column.text.strip()


headers = [
    "Name",
    "Price",
    "1h %",
    "24h %",
    "7d %",
    "Market Cap",
    "Volume (24h)",
    "Timestamp",
]
while True:
    data = fetch_data()
    print(tabulate(data, headers=headers, tablefmt="grid"))
    if not os.path.exists("coin_data.csv"):
        pd.DataFrame(data, columns=headers).to_csv(
            "coin_data.csv", mode="w", header=True, index=False
        )
    else:
        pd.DataFrame(data, columns=headers).to_csv(
            "coin_data.csv", mode="a", header=False, index=False
        )
    time.sleep(10)
