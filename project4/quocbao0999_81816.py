from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
web_page = requests.get(url)
# print (type(web_page))
soup = BeautifulSoup(web_page.text, 'html.parser')
# print (soup)
table = soup.find('table')
# print (type (table))
table_column = table.find_all('th')
# print (table_title)
table_column_title = [column_title.text for column_title in table_column]
# print (table_column_title)

import pandas as pd

df = pd.DataFrame(columns = table_column_title)
# print (df)
table_content = table.find_all('tr')
# print (table_content)
for row in table_content:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # Padding row data if it has fewer items than the number of columns
    while len(individual_row_data) < len(df.columns):
        individual_row_data.append('')
    
    # Check if the number of columns matches
    if len(individual_row_data) == len(df.columns):
        df.loc[len(df)] = individual_row_data
    else:
        print(f"Skipping row due to column mismatch: {individual_row_data}")
print (df)
