from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from datetime import datetime

api_key = 'YOU_MUST_NEVER_PUBLIC_YOUR_API_KEY'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

def fetch_data_from_api():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        currencies = data['data'][:5]

        # Tạo DataFrame chứa thông tin bảng dữ liệu
        df = pd.DataFrame(currencies)
        df['Price'] = df['quote'].apply(lambda x: x['USD']['price'])
        df['1h %'] = df['quote'].apply(lambda x: x['USD']['percent_change_1h'])
        df['24h %'] = df['quote'].apply(lambda x: x['USD']['percent_change_24h'])
        df['7d %'] = df['quote'].apply(lambda x: x['USD']['percent_change_7d'])
        df['Market Cap'] = df['quote'].apply(lambda x: x['USD']['market_cap'])
        df['Volume (24h)'] = df['quote'].apply(lambda x: x['USD']['volume_24h'])
        df.drop(columns=['quote'], inplace=True)

        df['Rank'] = df['cmc_rank'].astype(str)
        df['Name'] = df['name']
        df[['Price', 'Market Cap', 'Volume (24h)']] = df[['Price', 'Market Cap', 'Volume (24h)']].applymap('{:,.2f}'.format)
        df = df[['Rank', 'Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume (24h)']]
        df['Timestamp'] = pd.to_datetime('now').strftime("%Y-%m-%d %H:%M:%S.%f")
        return df

    else:
        print(f'Error fetching data: {response.status_code}')
        return None

while True:
    table_data = fetch_data_from_api()
    if table_data is not None:
        print("Rank\tName\t\tPrice\t1h %\t24h %\t7d %\tMarket Cap\tVolume (24h)\tTimestamp")
        print("-" * 120)
        print(table_data)
    time.sleep(5)
