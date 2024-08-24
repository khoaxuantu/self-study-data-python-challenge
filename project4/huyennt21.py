from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

url = 'https://coinmarketcap.com/'

response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')[1:]

crypto_data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 9:
        row_data = [cells[i].get_text(separator=' / ', strip=True) for i in range (1,9)]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row_data.append(timestamp)
        crypto_data.append(row_data)

headers = table.find_all('th')
column_titles = [headers[i].get_text() for i in range (1,10)]
column_titles[8] = 'Timestamp'

df = pd.DataFrame(crypto_data, columns = column_titles)
df.to_csv('crypto_data.csv', index=False)

print("Data has been saved to file crypto_data.csv")
print(df)