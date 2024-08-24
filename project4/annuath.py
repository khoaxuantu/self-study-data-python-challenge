import requests
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import sys

# Try to import tabulate, install it if it's not available
try:
    from tabulate import tabulate
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
    from tabulate import tabulate

def get_crypto_prices():
    url = 'https://coinmarketcap.com'
    response_text = requests.get(url).text
    
    soup = BeautifulSoup(response_text, 'html.parser')
    
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get all the table rows
    table_rows = soup.findAll('tr')
    
    # Prepare data for table
    data = []
    
    # Iterate through all the table rows and get the required data
    for table_row in table_rows:
        crypto_name = table_row.find('p', class_='sc-71024e3e-0 ehyBa-d')
        shortened_crypto_name = table_row.find('p', class_='sc-71024e3e-0 OqPKt coin-item-symbol')
        crypto_price = table_row.find('div', class_='sc-b3fc6b7-0 dzgUIj')
        
        # Ensure these selectors match the current website's structure
        price_changes = table_row.find_all('span', class_='sc-a59753b0-0')
        market_cap = table_row.find('span', class_='sc-11478e5d-1 jfwGHx')
        volume_24h = table_row.find('p', class_='sc-71024e3e-0 bbHOdE font_weight_500')

        # Check if the price_changes list has enough elements
        if len(price_changes) >= 3:
            onehour_price_percent = price_changes[0].text
            day_price_percent = price_changes[1].text
            week_price_percent = price_changes[2].text
        else:
            onehour_price_percent = "N/A"
            day_price_percent = "N/A"
            week_price_percent = "N/A"
        
        if crypto_name and shortened_crypto_name and crypto_price and market_cap and volume_24h:
            data.append([
                crypto_name.text,
                shortened_crypto_name.text,
                crypto_price.text,
                onehour_price_percent,
                day_price_percent,
                week_price_percent,
                market_cap.text,
                volume_24h.text
            ])
    
    # Print the timestamp
    print(f"Timestamp: {timestamp}\n")
    
    # Print the data as a table
    headers = ["Name", "Symbol", "Price", "1H%", "24H%", "7D%", "Market Cap", "24h Volume"]
    print(tabulate(data, headers=headers, tablefmt='grid'))

if __name__ == "__main__":
    get_crypto_prices()
    input("Press Enter to exit...")
