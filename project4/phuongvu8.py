import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = 'https://coinmarketcap.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')

table = soup.find('thead')
table2 = soup.find('tbody')

world_column = table.find_all('th')
world_column_title = [columns.text for columns in world_column[1:9]]
world_column_title.append('TimeStamp')

df = pd.DataFrame(columns = world_column_title)

world_row = table2.find_all('tr',limit = 4)

current_time = datetime.datetime.now()
for row in world_row:
    row_data = row.find_all('td')
    world_data = [data.text for data in row_data[1:9]]
    world_data.append(str(current_time))
    print(world_data)
    
    length = len(df) 
    df.loc[length] =  world_data

df.to_csv('Crypto.csv', index = False)

