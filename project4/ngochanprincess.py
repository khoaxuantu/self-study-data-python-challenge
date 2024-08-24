# Great work! But you should also parse the currencies' names because it currently contains the symbol of the currency.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

url = "https://coinmarketcap.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

table = soup.find("table")
coin_columns = table.find_all("th")
coin_columns_titles = [columns.text for columns in coin_columns[2:9]] + ["TimeStamp"]

# print(coin_columns_titles)

df = pd.DataFrame(columns=coin_columns_titles)

coin_rows = table.find_all("tr")


def coin_data(coin):
    for row in coin_rows[1:]:
        row_data = row.find_all("td")

        if row_data[2].text == coin:

            TimeStamp = datetime.datetime.now()
            individual_row_data = [data.text for data in row_data[2:9]] + [TimeStamp]
            length = len(df)
            df.loc[length] = individual_row_data


coin_list = ["BitcoinBTC", "EthereumETH", "BNBBNB"]
for crypto in coin_list:
    coin_data(crypto)

print(df)
