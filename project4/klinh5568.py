import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to scrape data for a single cryptocurrency
def scrape_crypto_data(crypto):
    base_url = 'https://coinmarketcap.com/currencies/'
    url = f'{base_url}{crypto}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

        # get all the table rows
    table_rows = soup.find_all('tr')

    # iterate through all the table rows and get the required data
    for table_row in table_rows:
        # Extracting the cryptocurrency name
        name_element = soup.find("span", class_='sc-65e7f566-0 lsTl')
        name = name_element.text if name_element else "N/A"
        name = name.replace(' price', '')
        
        # Extracting the price
        price_element = soup.find("span", class_='sc-65e7f566-0 clvjgF base-text')
        price = price_element.text if price_element else "N/A"
        
        # Find the relevant 'dd' element
        dd_element = soup.find('dd', class_='sc-65e7f566-0 dzgtSD base-text')
        
        # Extract only the text following the div/p/svg, which is the market cap
        market_cap = dd_element.contents[-1].strip()

        #volume 24h
        volume = soup.find_all('dd', class_ = 'sc-65e7f566-0 dzgtSD base-text')
        volume = volume[1].text.strip()
        volume = volume.split('%')[-1].strip()
        
        
    # Returning basic data
    return name, price, market_cap,volume

def percentage_change(crypto):
    base_url = 'https://coinmarketcap.com/'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # get all the table rows
    table_rows = soup.find_all('tr')

    # iterate through all the table rows and get the required data
    for table_row in table_rows:
        name_element = table_row.find("p", class_='sc-71024e3e-0 ehyBa-d')  # Replace with correct class if needed
        if name_element and name_element.text.strip().lower() == crypto.lower():
            percentage_changes = table_row.find_all('span', class_=['sc-a59753b0-0 cmnujh', 'sc-a59753b0-0 ivvJzO'])
        
            def extract_change_with_symbol(element):
                symbol = '▲' if 'cmnujh' in element['class'] else '▼'
                return f"{symbol} {element.text.strip()}"
        
            if len(percentage_changes) >= 3:  # Ensure there are at least 3 changes
                one_hour_change = extract_change_with_symbol(percentage_changes[0])
                twenty_four_hour_change = extract_change_with_symbol(percentage_changes[1])
                seven_day_change = extract_change_with_symbol(percentage_changes[2])
                return one_hour_change, twenty_four_hour_change, seven_day_change
            else:
                return "Unable to find all percentage changes."
    
    return "Cryptocurrency not found."


# List of cryptocurrencies to scrape
cryptos = ['bitcoin', 'ethereum', 'bnb']

# Collecting data for each cryptocurrency
crypto_data = []
for crypto in cryptos:
    name, price, market_cap,volume = scrape_crypto_data(crypto)
    one_hour_change, twenty_four_hour_change, seven_day_change = percentage_change(crypto)
    data = {
        "Name": name,
        "Price": price,
        "Market Cap": market_cap,
        "1h %": one_hour_change,
        "24h %": twenty_four_hour_change,
        "7d %": seven_day_change,
        "Volume(24h)": volume,
        "Timestamp": datetime.now()
    }
    crypto_data.append(data)

# Creating a DataFrame and displaying the data in the desired order
df = pd.DataFrame(crypto_data, columns=["Name", "Price", "Market Cap", "1h %", "24h %", "7d %", "Volume(24h)", "Timestamp"])
print(df)

# Optionally, save the data to a CSV file
df.to_csv('crypto_data.csv', index=False)
