# Great work!

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import pandas as pd


class InputError(Exception):
    "Raised when time length is shorter than interval or interval is shorter than 1 second."
    pass


def data_append(row):
    """
    This function creates a list of data needed to append to the data frame after searching for all the strings in the row and adding the timestamp.
    """
    datas = [data for data in row.stripped_strings] + [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    ]
    append_data = [datas[i] for i in data_index.values()]
    return append_data


print(
    "Collect data on Bitcoin, Ethereum, and BNB from CoinMarketCap in a desired time length with desired intervals."
)

# Nhập đầu vào tổng khoảng thời gian và khoảng cách giữa các đợt lấy data theo mong muốn
while True:
    try:
        length = float(
            input("Input the time length you want to scrape the data (in minutes):")
        )
        interval = float(
            input("Input the interval between the data collected (in seconds)(>= 1):")
        )
        if length * 60 <= interval or interval < 1:
            raise InputError(
                "Invalid input! Try again.\nMake sure your time length in seconds is longer than your interval and your interval is larger than 1 second!\n"
            )
        break
    except InputError as e:
        print(e)
    except Exception as e:
        print(e)
        print("Try again!\n")

url = "https://coinmarketcap.com/"

# Tạo dataframe của 3 coin với header để sau này gắn dữ liệu vào
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.body.find("table")
column_heads = [head.text for head in table.find_all("th")][2:9] + ["TimeStamp"]

df_BTC = pd.DataFrame(columns=column_heads)
df_ETH = pd.DataFrame(columns=column_heads)
df_BNB = pd.DataFrame(columns=column_heads)

crypto_dict = {"Bitcoin": df_BTC, "Ethereum": df_ETH, "BNB": df_BNB}

data_index = {
    "Name": 1,
    "Price": 3,
    "1h %": 4,
    "24h %": 5,
    "7d %": 6,
    "Market Cap": 8,
    "Volume(24h)": 9,
    "TimeStamp": 12,
}

# Bắt đầu scrape dữ liệu
try:
    start = time.perf_counter()
    end = start + length * 60

    print(f"\nWe are collecting your data. Please wait {length} minutes...")

    while start <= end:
        tic = time.perf_counter()
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.body.find("table")
        coin_rows = table.find_all("tr")
        count = 0

        for row in coin_rows[1:]:
            if row.find_all("p")[1].text == "Bitcoin":
                df_BTC.loc[len(df_BTC)] = data_append(row)
                count += 1
            elif row.find_all("p")[1].text == "Ethereum":
                df_ETH.loc[len(df_ETH)] = data_append(row)
                count += 1
            elif row.find_all("p")[1].text == "BNB":
                df_BNB.loc[len(df_BNB)] = data_append(row)
                count += 1

            if count == 3:
                toc = time.perf_counter()
                time.sleep(interval - (toc - tic))
                start = time.perf_counter()
                break
except Exception as e:
    print(e)
else:
    print("\nData collected successfully! Here is your data!")

# In kết quả
for key, value in crypto_dict.items():
    print("--------------------------------------------------------------")
    print("Cryto Name:", key)
    print(value)
