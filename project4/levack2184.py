#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

# Function to fetch cryptocurrency data
def fetch_crypto_data(crypto_name, crypto_abbr):
    url = "https://coinmarketcap.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table')

    input = crypto_name + crypto_abbr
    coin_row = table.find_all("tr")

    # Initialize DataFrame
    df = pd.DataFrame(columns=["Crypto Name", "Price", "1h %", "24h %", "7d %", "Market Cap", "Volume(24h)", "Time Retrieve"])

    # Iterate through each row
    for row in coin_row:
        row_data = row.find_all("td")
        individual_row_data = [data.text for data in row_data]
        
        # Slice to avoid IndexError and check if the row contains the desired cryptocurrency
        crypto_name_data = individual_row_data[2:3]
        if crypto_name_data and input.lower() in crypto_name_data[0].lower():
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            market_cap_volume = individual_row_data[7].split("$")
            market_cap = f"${market_cap_volume[1]}" if len(market_cap_volume) > 1 else None
            volume_24h_elements = row.find_all("p", {"class":"sc-71024e3e-0 bbHOdE font_weight_500"})
            volume_24h = volume_24h_elements[0].text

            # Prepare the data to be added to DataFrame
            current_price = individual_row_data[2:7] + [market_cap, volume_24h, timestamp]
            length = len(df)
            # Append the data to the DataFrame
            df.loc[length] = current_price
    
    return df

# Function to fetch data for multiple cryptocurrencies
def loop_fetch_multiple_cryptos(crypto_list, iterations, time_gap=180):
    # Initialize an empty DataFrame to store all the data
    df_all = pd.DataFrame(columns=["Crypto Name", "Price", "1h %", "24h %", "7d %", "Market Cap", "Volume(24h)", "Time Retrieve"])

    for _ in range(iterations):
        for crypto in crypto_list:
            crypto_name, crypto_abbr = crypto['name'], crypto['abbr']
            df = fetch_crypto_data(crypto_name, crypto_abbr)
            df_all = pd.concat([df_all, df], ignore_index=True)  # Append the new data
        print(df_all)
        time.sleep(time_gap)  # Wait for the specified time gap

    return df_all

# Gather user inputs for three cryptocurrencies
first_bitcoin = input("Type your first crypto currency name: ")
first_bitcoin_abbr = input("Type your first crypto currency abbreviation: ")

second_bitcoin = input("Type your second crypto currency name: ")
second_bitcoin_abbr = input("Type your second crypto currency abbreviation: ")

third_bitcoin = input("Type your third crypto currency name: ")
third_bitcoin_abbr = input("Type your third crypto currency abbreviation: ")

iterations = int(input("How many times you want this to loop??, type your number:"))

time_gap = int(input("Type your time gap between loops (seconds):"))
# List of cryptocurrencies to gather data for
crypto_list = [
    {"name": first_bitcoin.strip(), "abbr": first_bitcoin_abbr.strip()},
    {"name": second_bitcoin.strip(), "abbr": second_bitcoin_abbr.strip()},
    {"name": third_bitcoin.strip(), "abbr": third_bitcoin_abbr.strip()}
]

# Example usage: Fetch data for the cryptocurrencies 5 times, with a 3-minute interval
final_df = loop_fetch_multiple_cryptos(crypto_list, iterations, time_gap)
print(final_df)

