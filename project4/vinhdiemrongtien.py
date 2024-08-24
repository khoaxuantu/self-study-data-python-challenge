#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Great work!

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of the CoinMarketCap website
url = "https://coinmarketcap.com/"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


def get_crypto_info(row):
    cols = row.find_all("td")
    name = cols[2].find("p").text.strip()
    price = cols[3].text.strip()
    hourly_change = cols[4].text.strip()
    daily_change = cols[5].text.strip()
    weekly_change = cols[6].text.strip()
    market_cap = cols[7].text.strip()
    volume_24h = cols[8].text.strip()
    return {
        "Name": name,
        "Price": price,
        "1h%": hourly_change,
        "24h%": daily_change,
        "7d%": weekly_change,
        "Market Cap": market_cap,
        "Volume 24H": volume_24h,
        "timestamp": datetime.now(),
    }


table = soup.find("table", {"class": "cmc-table"})

cryptos = table.find("tbody").find_all("tr")[:10]

crypto_data = [get_crypto_info(crypto) for crypto in cryptos]

df = pd.DataFrame(crypto_data)
print(df.to_string())
