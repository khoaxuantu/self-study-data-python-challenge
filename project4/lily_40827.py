# Great work! But remember parsing the currency names more carefully, as it currently includes the ticker symbol.

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os

url = "https://coinmarketcap.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

# Create Table with column titles + TimeStamp
table = soup.find("table", "cmc-table")
table_columns = table.find_all("th")
table_column_titles = [columns.text for columns in table_columns][2:9]
table_column_titles.append("TimeStamp")

df = pd.DataFrame(columns=table_column_titles)

# Find <tr> in table with <a> for each currency, then append data to df
table_rows = table.find_all("tr")

for row in table_rows:
    bitcoin_a_tag = row.find("a", href="/currencies/bitcoin/")
    ethereum_a_tag = row.find("a", href="/currencies/ethereum/")
    bnb_a_tag = row.find("a", href="/currencies/bnb/")
    if bitcoin_a_tag:
        bitcoin_data = [data.text.strip() for data in row.find_all("td")][2:9]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bitcoin_data.append(timestamp)
        df.loc[len(df)] = bitcoin_data
    if ethereum_a_tag:
        ethereum_data = [data.text.strip() for data in row.find_all("td")][2:9]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ethereum_data.append(timestamp)
        df.loc[len(df)] = ethereum_data
    if bnb_a_tag:
        bnb_data = [data.text.strip() for data in row.find_all("td")][2:9]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bnb_data.append(timestamp)
        df.loc[len(df)] = bnb_data
        break

## Add data to a csv, change file_path 'File location' to desired path
file_path = r"C:" "File location" "\Project4.csv"
if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=True, index=False)
else:
    df.to_csv(file_path, mode="w", header=True, index=False)
