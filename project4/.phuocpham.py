# Nice work on this project! You've successfully scraped the CoinMarketCap website. And it would be better if u can save it in a CSV file. Because you can't see all the columns in the dataframe when print it out in the console. So, I will help you to save it in a CSV file.

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

# GLOBAL VARIABLES
table_slice = slice(1, 9)


# Creating a connection to the website
coin_market_url = "https://coinmarketcap.com/"
market_page = requests.get(coin_market_url)


# Take in the pure html code for the table only
market_soup = BeautifulSoup(market_page.text, "html.parser")
market_table = market_soup.find("table")


# Extract the column titles and move it in the dataframe
column_titles = [title.text for title in market_table.find_all("th")]
column_titles = column_titles[table_slice]
column_titles.append("TimeStamp")
df = pd.DataFrame(columns=column_titles)


# Extracting the rows for the table data
record_rows = market_table.find_all("tr")
for row in record_rows[1:11]:
    row_data = row.find_all("td")
    while len(row_data) < 9:
        row_data.append("<p><span>N/A</span></p>")
    row_data[2] = row_data[2].p

    # Filter out the target coins
    if row_data[2].text not in ["Bitcoin", "Ethereum", "BNB"]:
        continue

    row_data[7] = row_data[7].span.find_next("span")
    row_data[8] = row_data[8].p
    row = [tr.text for tr in row_data]

    # Filter out the target columns
    row = row[table_slice]
    row.append(str(datetime.now()))
    length = len(df)
    df.loc[length] = row

print(df)
