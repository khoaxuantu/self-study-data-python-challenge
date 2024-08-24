# Nice work on this project! You've successfully scraped the CoinMarketCap website and saved the data to a CSV file.

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://coinmarketcap.com/"
pages = 5
page_size = 50

response = requests.get(base_url)
content = response.content
parsed_content = BeautifulSoup(content, "html.parser")

coin_feature = parsed_content.find_all("p", {"class": "sc-71024e3e-0 fSsxNG"})
coin_feature_name = [name.get_text() for name in coin_feature]
df = pd.DataFrame(columns=coin_feature_name)
df = df.drop(df.columns[-1], axis=1)

for item in parsed_content.find_all("tr", {"style": "cursor:pointer"}):
    coin_data_row = []

    for td in item.find_all("td"):
        coin_data_row = []

    name_tag = item.find("p", {"class": "sc-71024e3e-0 ehyBa-d"})
    name = name_tag.get_text(strip=True) if name_tag else None
    coin_data_row.append(name)

    price_tag = item.find("div", {"class": "sc-b3fc6b7-0 dzgUIj"})
    price = price_tag.get_text(strip=True) if price_tag else None
    coin_data_row.append(price)

    change_1h_tag = item.find("span", {"class": "sc-a59753b0-0 cmnujh"})
    change_1h = change_1h_tag.get_text(strip=True) if change_1h_tag else None
    coin_data_row.append(change_1h)

    change_24h_tag = item.find("span", {"class": "sc-a59753b0-0 cmnujh"})
    change_24h = change_24h_tag.get_text(strip=True) if change_24h_tag else None
    coin_data_row.append(change_24h)

    change_7d_tag = item.find("span", {"class": "sc-a59753b0-0 ivvJzO"})
    change_7d = change_7d_tag.get_text(strip=True) if change_7d_tag else None
    coin_data_row.append(change_7d)

    market_cap_tag = item.find("span", {"class": "sc-11478e5d-1 jfwGHx"})
    market_cap = market_cap_tag.get_text(strip=True) if market_cap_tag else None
    coin_data_row.append(market_cap)

    volumn_tag = item.find("p", {"class": "sc-71024e3e-0 bbHOdE font_weight_500"})
    volumn = volumn_tag.get_text(strip=True) if volumn_tag else None
    coin_data_row.append(volumn)

    length = len(df)
    df.loc[length] = coin_data_row

    df.to_csv("coinmarketcap.csv", index=False)
