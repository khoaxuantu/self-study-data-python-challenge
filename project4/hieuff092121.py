
from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
import datetime
import time
url = 'https://coinmarketcap.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text,features="html.parser")
table = soup.find('table','sc-7b3ac367-3 etbcea cmc-table')
inf_column_titles =[]
for column in table.find_all('th')[1:-2]:
    columns_data = column.find('p')
    inf_column_titles.append(columns_data.text)
inf_column_titles.append('TimeStamp')
df = pd.DataFrame(columns = inf_column_titles)
row = table.find_all('tr')[1:5]
for tmp in range(5):
    for i in range(len(row)):
        if i == 2:
            continue
        detail_row_data = []
        row_data= row[i].find_all('td')
        for j in row_data[1:3]:
            if len(j.find_all('p'))==0:
                continue
            data = j.find('p')
            detail_row_data.append(data.text)
        for j in row_data[3:-3]:
            if len(j.find_all('span'))==0:
                continue
            data = j.find('span')
            detail_row_data.append(data.text)
        data = row_data[-3].find('p')
        detail_row_data.append(data.text)
        detail_row_data.append(datetime.datetime.now())
        length = len(df)
        df.loc[length] = detail_row_data
    df.loc[length+1] = ['','','','','','','','','']
    time.sleep(10)
print(df)




