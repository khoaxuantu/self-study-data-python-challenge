from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

url = 'https://coinmarketcap.com/'
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', "sc-7b3ac367-3 etbcea cmc-table")

coin_column = table.find_all('th')
coin_column_titles = [column.text for column in coin_column[2:9]] + ['timestamp']

#create dataframe
df = pd.DataFrame(columns = coin_column_titles)

coin_rows = table.find_all('tr')
def crypto(coin):
    for row in coin_rows[1:]:
        row_data = row.find_all('td')

        if row_data[2].text == f'{coin}':
            #get timestamp
            timestamp = datetime.datetime.now()
            individual = [data.text for data in row_data[2:9]] + [timestamp]

            lenght = len(df)
            df.loc[lenght] = individual

coins = ['BitcoinBTC', 'EthereumETH', 'BNBBNB']

for coin in coins:
    crypto(coin)

print(df)