#!/usr/bin/env python
# coding: utf-8

# Great work

# # Python Project 4: Automated Crypto Web Scraper

# In[2]:


from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import time

url = "https://coinmarketcap.com/"

# Định nghĩa các cột cho DataFrame
columns = ["Crypto Name", "Price", "TimeStamp"]
data = []  # Tạo danh sách rỗng để lưu dữ liệu

for i in range(5):  # Quét trang web 5 lần rồi thôi
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Lấy Crypto Name là Bitcoin
    bitcoin = soup.find("p", class_="sc-71024e3e-0 ehyBa-d")
    crypto_name = bitcoin.text

    # Lấy giá của Bitcoin
    price = soup.find("div", class_="sc-b3fc6b7-0 dzgUIj")
    crypto_price = price.text

    # Lấy thời gian quét dữ liệu
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Thêm dữ liệu vào danh sách
    data.append([crypto_name, crypto_price, current_time])

    # Tạm dừng 1 giây giữa các lần quét
    time.sleep(1)

# Tạo DataFrame
df = pd.DataFrame(data, columns=columns)
print(df)
