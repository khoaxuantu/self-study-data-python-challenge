# Nice work there, but it would be better if you can save the dataframe to a csv file. Also you should parse the name of crypto more carefully, because your code is currently printing out Name + Symbol.

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def parse_column_names(table):
    headers = table.find_all("th")
    columns = [headers[i].text for i in range(2, 9)]
    columns.append("Timestamp")
    return columns


def is_coin_of_interest(row, target_coins):
    coin_name = row.find_all("td")[2].text.replace(" ", "").lower()
    return coin_name in target_coins


def clean_text(value):
    parts = value.split("$")
    if len(parts) > 2:
        value = parts[-1].strip()
    else:
        value = parts[0].strip()
    value = f"${value}"
    return value.strip()


def clean_volume(value):
    value = value.split(" ")[0]
    return value.strip()


def extract_coin_data(row):
    cells = row.find_all("td")
    data = [cells[i].text.strip() for i in range(2, 9)]
    data[5] = clean_text(data[5])
    data[6] = clean_volume(data[6])
    return data


def scrape_coin_data(target_coins, url):
    target_coins_set = {coin.lower() for coin in target_coins}
    soup = get_page_content(url)
    table = soup.find("table", class_="sc-7b3ac367-3 etbcea cmc-table")
    rows = table.find_all("tr")[1:]
    extracted_data = []
    timestamp = datetime.now()
    for row in rows:
        if is_coin_of_interest(row, target_coins_set):
            coin_data = extract_coin_data(row)
            coin_data.append(timestamp)
            extracted_data.append(coin_data)
    df = pd.DataFrame(extracted_data, columns=parse_column_names(table))
    return df


coins = ["BitcoinBTC", "EthereumETH", "BNBBNB"]

url = "https://coinmarketcap.com/"

df = scrape_coin_data(coins, url)

print(df)
