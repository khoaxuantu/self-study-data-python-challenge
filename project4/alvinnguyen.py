import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://coinmarketcap.com/historical/20240804/'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

columns_name = [name.text for name in soup.find('tr')]

df = pd.DataFrame(columns=columns_name)

tr = soup.find_all('tr')

for row_data in tr[3:23]:
    each_row_data = row_data.find_all('td')
    data = [value.text for value in each_row_data]
    
    length = len(df)
    df.loc[length] = data

df

# df.to_csv(r'C:\Users\Admin\Desktop\my_project\Coin_data.csv', index=False)