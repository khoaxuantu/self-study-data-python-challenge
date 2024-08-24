#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
url = 'https://coinmarketcap.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', "sc-7b3ac367-3 etbcea cmc-table")
coin_C = table.find_all('th')
coin_titles = [column.text for column in coin_C[2:9]] + ['timestamp']
#print(coin_column_titles)
#print(page)
df = pd.DataFrame(columns = coin_titles)
#print(df)
rows = table.find_all('tr')
def crypto(coin):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    for row in rows[1:]:
        if coin in row.text:
            data = [td.text.strip() for td in row.find_all('td')[2:9]]
            data.append(timestamp)
            temp_dict = {coin_titles[i]: data[i] for i in range(len(data))}
            df.loc[len(df)] = temp_dict

# List of cryptocurrencies to scrape
cryptos = ['Bitcoin', 'Ethereum', 'BNB']

# Scrape the information for each cryptocurrency
for crypto_name in cryptos:
    crypto(crypto_name)

# Print the scraped data
print(df)


# In[ ]:




