# Great work, but your code is not very clean.

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# create empty lists to store the data
crypto_name_list = []
crypto_symbol_list = []
crypto_market_cap_list = []
crypto_price_list = []
crypto_1h_list = []
crypto_24h_list = []
crypto_7d_list = []
crypto_24hvolume_list = []
timestamp_list = []

# create an empty dataframe to organize the data
df = pd.DataFrame()


# create a function to scrape the data
# Example: https://coinmarketcap.com/historical/20240811/
def scrape(date="20240811/"):
    # Get the URL of the website that we wanna scrape
    url = "https://coinmarketcap.com/historical/" + date
    # make a request to the website
    webpage = requests.get(url)
    # Parse the text from the website
    soup = BeautifulSoup(webpage.text, "html.parser")

    # get the table row element
    tr = soup.find_all("tr", attrs={"class": "cmc-table-row"})
    # create a count variable to count the number of crypto currencies that we wanna scrape
    count = 0
    # Loop through every row to gather the data
    for row in tr:
        # check if the count is reached then break out of the loop
        if count == 10:
            break
        count = count + 1  # increment count by 1

        # Store the name of the cryptocurrency into a variable
        # Find the td element (column) to later get the cryptocurrency name and symbol
        name_column = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"
            },
        )
        crypto_name = name_column.find(
            "a", attrs={"class": "cmc-table__column-name--name cmc-link"}
        ).text.strip()
        # Store the coin market cap of the cryptocurrency or coin into a variable
        crypto_symbol = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol"
            },
        ).text.strip()
        crypto_market_cap = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap"
            },
        ).text.strip()
        crypto_price = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"
            },
        ).text.strip()
        crypto_1h_percent_change = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h"
            },
        ).text.strip()
        crypto_24h_percent_change = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h"
            },
        ).text.strip()
        crypto_7d_percent_change = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d"
            },
        ).text.strip()
        crypto_24hvolume = row.find(
            "td",
            attrs={
                "class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h"
            },
        ).text.strip()

        # Append the data to the list
        crypto_name_list.append(crypto_name)
        crypto_symbol_list.append(crypto_symbol)
        crypto_market_cap_list.append(crypto_market_cap)
        crypto_price_list.append(crypto_price)
        crypto_1h_list.append(crypto_1h_percent_change)
        crypto_24h_list.append(crypto_24h_percent_change)
        crypto_7d_list.append(crypto_7d_percent_change)
        crypto_24hvolume_list.append(crypto_24hvolume)
        timestamp_list.append(datetime.now())


# Run the scrape function
scrape(date="20240811/")

# Store the data into a dataframe
df["Crypto Name"] = crypto_name_list
df["Symbol"] = crypto_symbol_list
df["Market Cap"] = crypto_market_cap_list
df["Price"] = crypto_price_list
df["Volume 24h"] = crypto_24hvolume_list
df["% 1h"] = crypto_1h_list
df["% 24h"] = crypto_24h_list
df["% 7d"] = crypto_7d_list
df["Timestamp"] = timestamp_list

# Show the data
df.to_csv("crypto_data.csv", index=False)
