from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import re

url = 'https://coinmarketcap.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')  # Specify the parser

# Extract table headers
crypto_titles = soup.find_all('th')
crypto_table_titles = [title.text.strip() for title in crypto_titles]

# Exclude unwanted headers
crypto_table_titles.pop()      # 'Circulating Supply'
crypto_table_titles.pop()      # 'Last 7 Days'
crypto_table_titles.reverse()  # Reverse to remove the first empty column
crypto_table_titles.pop()      # Remove the empty column
crypto_table_titles.reverse()  # Revert to original order

# Initialize DataFrame with a 'Timestamp' column
df = pd.DataFrame(columns=crypto_table_titles + ['Timestamp'])

# Define timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

# Extract table rows and append data
column_data = soup.find_all('tr')

def clean_value(value):
    if 'T' in value:
        return f"${float(value.replace('T', '').replace('$', '').replace(',', '')) * 1e12:,.0f}"
    elif 'B' in value:
        return f"${float(value.replace('B', '').replace('$', '').replace(',', '')) * 1e9:,.0f}"
    elif 'M' in value:
        return f"${float(value.replace('M', '').replace('$', '').replace(',', '')) * 1e6:,.0f}"
    else:
        return value

def remove_extra_text(value):
    return re.sub(r'\d+ [A-Z]+$', '', value).strip()

for row in column_data[1:11]:  # Skip the 1st blank row
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Exclude unwanted data
    individual_row_data.pop()  # 'Circulating Supply'
    individual_row_data.pop()  # 'Last 7 Days'
    individual_row_data.reverse()  # Reverse to remove the first empty column
    individual_row_data.pop()  # Remove the empty column
    individual_row_data.reverse()  # Revert to original order
    
    # Clean and format 'Market Cap' and 'Volume(24h)'
    individual_row_data[5] = clean_value(individual_row_data[5])
    individual_row_data[6] = clean_value(remove_extra_text(individual_row_data[6]))
    
    # Append timestamp
    individual_row_data.append(timestamp)

    length = len(df)
    df.loc[length] = individual_row_data

# Export to csv file
df.to_csv(r'C:\Users\Pandal Pan\OneDrive\Desktop\python_work\Crypto_Scraped.csv', index=False)
