import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

crypto_name_list = []
crypto_market_cap_list = []
crypto_price_list = []
crypto_circulating_supply_list = []
crypto_symbol_list = []
crypto_volume_24h_list = []
crypto_percentage_1h_list = []
crypto_percentage_24h_list = []
crypto_percentage_7d_list = []

def scrape(date='20240811/'):
    URL = 'https://coinmarketcap.com/historical/' + date
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    tr = soup.find_all('tr', attrs={'class': 'cmc-table-row'})

    count = 0
    for row in tr:
        if count == 4:
            break
        count += 1

        try:
            name_column = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
            crypto_name = name_column.find('a', attrs={'class': 'cmc-table__column-name--name cmc-link'}).text.strip()

            crypto_market_cap = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
            crypto_price = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
            crypto_circulating_supply_and_symbol = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
            crypto_volume_24h = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h'}).text.strip()
            crypto_percentage_1h = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h'}).text.strip()
            crypto_percentage_24h = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h'}).text.strip()
            crypto_percentage_7d = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d'}).text.strip()
            crypto_circulating_supply = crypto_circulating_supply_and_symbol.split(' ')[0]
            crypto_symbol = crypto_circulating_supply_and_symbol.split(' ')[1]

            crypto_name_list.append(crypto_name)
            crypto_market_cap_list.append(crypto_market_cap)
            crypto_price_list.append(crypto_price)
            crypto_circulating_supply_list.append(crypto_circulating_supply)
            crypto_symbol_list.append(crypto_symbol)
            crypto_volume_24h_list.append(crypto_volume_24h)
            crypto_percentage_1h_list.append(crypto_percentage_1h)
            crypto_percentage_24h_list.append(crypto_percentage_24h)
            crypto_percentage_7d_list.append(crypto_percentage_7d)
        except Exception as e:
            print(f"Error processing row {count}: {e}")

scrape(date='20240811/')

df = pd.DataFrame({
    'Name': crypto_name_list,
    'Market Cap': crypto_market_cap_list,
    'Price': crypto_price_list,
    'Circulating Supply': crypto_circulating_supply_list,
    'Symbol': crypto_symbol_list,
    'Volume (24h)': crypto_volume_24h_list,
    '% 1h': crypto_percentage_1h_list,
    '% 24h': crypto_percentage_24h_list,
    '% 7d': crypto_percentage_7d_list,
    'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] * len(crypto_name_list)
})

target_cryptos = ['Bitcoin', 'Ethereum', 'BNB']
filtered_df = df[df['Name'].isin(target_cryptos)]

print(filtered_df) 