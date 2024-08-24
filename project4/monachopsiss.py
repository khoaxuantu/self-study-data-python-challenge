from bs4 import BeautifulSoup
import requests
import pandas
import datetime
url = 'https://coinmarketcap.com/'
response  = requests.get(url)
soup = BeautifulSoup(response .text, 'html.parser')
table = soup.find('table', "sc-7b3ac367-3 etbcea cmc-table")
coin_column = table.find_all('th')
coin_column_titles = [column.text for column in coin_column[2:9]] + ['timestamp']

df = pandas.DataFrame(columns = coin_column_titles)

coin_rows = table.find_all('tr')
def crypto(coin):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    for row in coin_rows[1:]:
        if coin in row.text:
            data = [td.text.strip() for td in row.find_all('td')[2:9]]
            data.append(timestamp)
            temp_dict = {coin_column_titles[i]: data[i] for i in range(len(data))}
            df.loc[len(df)] = temp_dict


cryptos = ['Bitcoin', 'Ethereum', 'BNB']

for crypto_name in cryptos:
    crypto(crypto_name)


print(df)