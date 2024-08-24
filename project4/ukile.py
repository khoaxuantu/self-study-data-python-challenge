import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

# URL of the CoinMarketCap page
url = "https://coinmarketcap.com/"

# Function to extract Bitcoin data
def get_bitcoin_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find Bitcoin entry based on current HTML structure
    bitcoin_row = soup.find('a', {'href': '/currencies/bitcoin/'})
    
    if bitcoin_row:
        parent_row = bitcoin_row.find_parent('tr')
        if parent_row:
            columns = parent_row.find_all('td')
            # Print the columns to understand the structure
            print([column.text.strip() for column in columns])
            if len(columns) > 2:
                price = columns[3].text.strip()  # Adjust the index based on structure
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                return {'Crypto Name': 'Bitcoin', 'Price': price, 'TimeStamp': timestamp}
            else:
                print("Columns do not have enough data.")
        else:
            print("Parent row not found for Bitcoin.")
    else:
        print("Bitcoin row not found.")
    
    return None

# List to store data
data_list = []

# Fetch data every few seconds
for _ in range(5):  # Adjust the range for more iterations
    data = get_bitcoin_data()
    if data:
        data_list.append(data)
        print(f"Data fetched: {data}")
    else:
        print("No data fetched.")
    time.sleep(10)  # Wait for 10 seconds

# Create DataFrame
df = pd.DataFrame(data_list)
print(df)