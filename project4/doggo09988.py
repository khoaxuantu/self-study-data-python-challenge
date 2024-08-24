from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://coinmarketcap.com./'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table')

cols = [col.text for col in table.tr.find_all('th')]
cols.append('TimeStamp')
df = pd.DataFrame(columns=cols)

rows = table.tbody.find_all('tr')

bitcoinRow = [col.text for col in rows[0].find_all('td')]
bitcoinRow.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
df.loc[len(df)] = bitcoinRow

ethRow = [col.text for col in rows[1].find_all('td')]
ethRow.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
df.loc[len(df)] = ethRow

bnbRow = [col.text for col in rows[3].find_all('td')]
bnbRow.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
df.loc[len(df)] = bnbRow

df.drop(['Last 7 Days', '#'], axis=1, inplace=True)

print(df)