# -*- coding: utf-8 -*-
"""Project 4_doan09801.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tJtuG60FW0owe9c8KTbcbCWqofzTfwbj
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

def Automated_Crypto_Web_Scraper(url, crypto_cur):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    data_crypto = []

    for row in rows[1:]:
        data = row.find_all(['th','td'])

        name_crypto = data[2].find('p')
        if name_crypto and name_crypto.get_text() in crypto_cur:
            name = name_crypto.get_text()
            price_value = data[3].get_text()
            percent_1h = data[4].get_text()
            percent_24h = data[5].get_text()
            percent_7d = data[6].get_text()
            market_cap = data[7].find_all(['span'])[1].get_text()
            volume_24h = data[8].find_all(['p'])[1].get_text()

            data_crypto.append({
                "crypto_name": name,
                "price_value": price_value,
                "percent_1h": percent_1h,
                "percent_24h": percent_24h,
                "percent_7d": percent_7d,
                "market_cap": market_cap,
                "volume_24h": volume_24h
            })

    if data_crypto:
        df = pd.DataFrame(data_crypto)
        print(df)
    else:
        print("No data found for the specified cryptocurrencies.")

crypto_cur = ['Bitcoin', 'Ethereum', 'BNB']
url = "https://coinmarketcap.com/"
Automated_Crypto_Web_Scraper(url, crypto_cur)

