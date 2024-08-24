#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


# In[ ]:


df = pd.DataFrame(columns=["Crypto Name", "Price", "Timestamp"]
def fetch_bitcoin_price():
    url = 'https://coinmarketcap.com/'
    bitcoin_data = requests.get(url)
    bitcoin_html = BeautifulSoup(bitcoin_data.text, 'html.parser')
    
    # Locate the table with Bitcoin data
    table = bitcoin_html.find('table', {'class': 'sc-7b3ac367-3 etbcea cmc-table'})
    # Find the first row that should correspond to Bitcoin
    bitcoin_row = table.find('tr', {'style': 'cursor:pointer'})
    # Get the Bitcoin price from the relevant cell
    bitcoin_price = bitcoin_row.find('td', {'style': 'text-align:end'}).text
    return bitcoin_price

previous_price = None

while True:
    current_price = fetch_bitcoin_price()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    if current_price != previous_price:
        new_row = ["Bitcoin", current_price, timestamp]
        length = len(df)
        df.loc[length] = new_row
        print("\033[H\033[J") 
        print(df)
        previous_price = current_price
    time.sleep(15)


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:




