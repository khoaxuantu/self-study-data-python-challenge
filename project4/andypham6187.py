# Nice work after all, but there can be an error in your code, please check.

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os

# get request
url = "https://coinmarketcap.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("table", "sc-7b3ac367-3 etbcea cmc-table")
# find data.text row by row
data = table.get_text(separator="\n").splitlines()

# take header
header = data[0:10]
# remove header in data list
for x in header:
    data.remove(x)

# take top 10 coins
top_10_coin = []
for i in range(0, 10):
    each_coin = data[0:12]  # 12 value for each coin
    # remove from the data_list
    for x in each_coin:
        data.remove(x)
    top_10_coin.append(each_coin)

# clean elements in each coin to match the header
for coin in top_10_coin:
    # remove the abundant element
    coin.remove(coin[2])
    coin.remove(coin[6])

# arrange element to each header in dictionary
coin_dictionary = {}
for i in range(0, 10):
    dict_header = header[i]
    element = [x[i] for x in top_10_coin]
    coin_dictionary[dict_header] = element

# create DataFrame
df = pd.DataFrame(coin_dictionary)
# clean and edit DataFrame
df["Time"] = datetime.now()
wanted_currency = ["Bitcoin", "Ethereum", "BNB"]
df_coin = df[df["Name"].isin(wanted_currency)][
    ["Name", "Price", "1h %", "24h %", "7d %", "Market Cap", "Volume(24h)", "Time"]
]

# save or append new data to file_path
# this is where ur code can get error, because not everyone has a Desktop folder in their home directory. Thus to make your code always works, create a folder Desktop first if it doesn't exist
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = "." + "/andypham6187_coin_scraping.csv"
if not os.path.exists(file_path):
    df_coin.to_csv(file_path, index=False)
else:
    df_coin.to_csv(file_path, mode="a", index=False, header=False)
