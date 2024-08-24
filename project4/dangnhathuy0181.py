import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
date_time = datetime.now()

page = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
heads = table.find('thead')
cols = heads.find_all('th')
world_bitcoin = [col.text for col in cols[1:10]]
df = pd.DataFrame(columns= world_bitcoin)

rows = soup.find('tbody').find_all('tr')
for row in rows[0:10]:
    bitcoin = row.find_all('td')
    individual_bitcoin = [bit.text.strip() for bit in bitcoin[1:10]]
    length = len(df)
    df.loc[length] = individual_bitcoin
df['TimeStamp'] = date_time
