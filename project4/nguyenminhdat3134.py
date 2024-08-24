import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

# Define the URL
CoinMarket_URL = "https://coinmarketcap.com/"

# Target cryptocurrency names
target_cryptos = ['Bitcoin', 'Ethereum', 'BNB']

# Create Loop
loop = 0

# Start an infinite loop to update data in real-time
while True:
    # Request the page
    page = requests.get(CoinMarket_URL)
    soup = BeautifulSoup(page.text, "html.parser")

    # Find the table and extract the relevant columns
    table = soup.find("table", "sc-7b3ac367-3 etbcea cmc-table")
    Coin_columns = table.find_all('th')[2:9]
    Coin_columns_title = [columns.text for columns in Coin_columns]

    # Create an empty DataFrame with the extracted columns
    df = pd.DataFrame(columns=Coin_columns_title)
    df['Timestamp'] = datetime.now()

    # Extract the rows from the table
    Coin_rows = table.find('tbody').find_all('tr')[:10]

    # Use for loop to add rows to dataframe
    for rows in Coin_rows:
        crypto_name = rows.find('p', class_="sc-71024e3e-0 ehyBa-d").text
        if crypto_name in target_cryptos:
          market_cap = rows.find('span', class_="sc-11478e5d-1 jfwGHx").text
          volume_24h = rows.find('p', class_="sc-71024e3e-0 bbHOdE font_weight_500").text
          rows_data = rows.find_all('td')[3:7]
          individual_rows_data = [data.text for data in rows_data]

          individual_rows_data.insert(0,crypto_name)
          individual_rows_data.append(market_cap)
          individual_rows_data.append(volume_24h)
          individual_rows_data.append(datetime.now())
          df.loc[len(df)] = individual_rows_data

    # Print the DataFrame to see the updated data
    print(df)
    loop +=1

     # Wait for 15 seconds before the next update
    time.sleep(15)

    if loop == 20:
      break
