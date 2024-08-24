from bs4 import BeautifulSoup
import requests
import pandas as pd 
import datetime
import os

url = 'https://coinmarketcap.com'
page = requests.get (url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find ('table')

# Step 1: Get table columns
columns = table.find_all ('th')
table_column = [col.text for col in columns]
table_column.append ('Timestamp')

# Step 2: Get table content
table_content = []
rows = table.find_all ('tr')
for r in rows:
    cells = []
    row_content = r.find_all ('td')
    for row in row_content:
        content = row.text
        cell = ''
        try:
            # Get arrow (up or down) with 1h %, 24h %, 7d % metrics
            nested_span = row.find('span').find('span')
            arrow = nested_span.get('class')[0]
            if arrow == 'icon-Caret-down':
                cell = '-' + content
            elif arrow == 'icon-Caret-up':
                cell = '+' + content
            
        except:     
            try:
                # Get Market Cap metric 
                # first_value = row.find('span', class_='sc-11478e5d-0 chpohi').text
                second_value = row.find('span', class_='sc-11478e5d-1 jfwGHx').text
                cell = second_value

            except: 
                try:
                    # Get Volume (24h) metric
                    first_value = row.find('a').find('p').text
                    second_value = row.find('div', {'data-nosnippet': 'true'}).find('p').text
                    cell = first_value + '\n' + second_value
                except: 
                    cell = content           
        cells.append (cell)
    cells.append (datetime.datetime.now ())
    table_content.append (cells)
table = pd.DataFrame (table_content[1:], columns=table_column)

# Step 3: Filter the desired values
select_column = ['Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume(24h)', 'Timestamp']
result = table [select_column]

select_coin = ['Bitcoin\nBTC', 'Ethereum\nETH', 'BNB\nBNB']
result = result[result['Name'].isin(select_coin)]
print (result)

# Step 4: Store the result to file
file_name = 'coin_data.csv'
file_exists = os.path.isfile(file_name)
result.to_csv(file_name, mode='a', header=not file_exists, index=False)
