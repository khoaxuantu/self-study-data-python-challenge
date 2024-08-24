#!/usr/bin/env python
# coding: utf-8

# In[15]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import time
import os

def scrape_crypto_data(crypto_names):
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', class_='sc-7b3ac367-3 etbcea cmc-table')
    
    if not table:
        print("Table not found")
        return
    
    headers = [header.text.strip() for header in table.find_all('th')]
    print("Headers:", headers)
    
    crypto_data = {crypto: {} for crypto in crypto_names}
    
    rows = table.find_all('tr')[1:] 
    
    for row in rows:
        columns = row.find_all('td')
        if len(columns) < 9:
            continue  
        
        name_symbol = columns[2].find('p', class_='coin-item-symbol')
        if name_symbol:
            crypto_name = name_symbol.text.strip()
        else:
            continue  
        
        if crypto_name in crypto_names:
            market_cap = columns[7].text.strip()
            if '$' in market_cap:
                market_cap = '$' + market_cap.split('$')[-1]
            
            crypto_data[crypto_name] = {
                'Name': columns[2].text.strip(),
                'Price': columns[3].text.strip() if columns[3] else 'N/A',
                '1h %': columns[4].text.strip() if columns[4] else 'N/A',
                '24h %': columns[5].text.strip() if columns[5] else 'N/A',
                '7d %': columns[6].text.strip() if columns[6] else 'N/A',
                'Market Cap': market_cap,
                '24h Volume': columns[8].text.strip() if columns[8] else 'N/A',
                'TimeStamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    
    return crypto_data

def save_to_csv(data, filename):
    df = pd.DataFrame.from_dict(data, orient='index')
    if not os.path.isfile(filename):
        df.to_csv(filename, mode='w', header=True, index=True)
    else:
        df.to_csv(filename, mode='a', header=False, index=True)

cryptos = ['BTC', 'ETH', 'BNB']

end_time = time.time() + 30 * 60

while time.time() < end_time:
    data = scrape_crypto_data(cryptos)
    save_to_csv(data, 'crypto_data.csv')
    print("Data saved to 'crypto_data.csv'")
    # Wait for a minute before the next scrape
    time.sleep(60)


# In[ ]:




