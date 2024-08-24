# Nice work! But instead of printing the df out, you should save it to a csv file.

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL for CoinMarketCap
url = "https://coinmarketcap.com/"

# Send a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# List of cryptocurrencies to scrape
cryptos = ["Bitcoin", "Ethereum", "BNB"]

data = []

# Loop through each cryptocurrency name
for crypto in cryptos:
    try:
        # Find the row containing the cryptocurrency name
        row = soup.find("p", string=crypto).find_parent("tr")

        if row:
            print(f"Found row for {crypto}: {row}")

            # Extract the price
            price = row.find("div", class_="sc-b3fc6b7-0 dzgUIj")
            if price:
                price = price.text.strip()
            else:
                print(f"Price not found for {crypto}")

            # Extract the percentage changes
            changes = row.find_all("span", class_="sc-a59753b0-0")
            if len(changes) >= 3:
                hour_change = changes[0].text.strip()
                day_change = changes[1].text.strip()
                week_change = changes[2].text.strip()
            else:
                hour_change = day_change = week_change = None
                print(f"Changes not found for {crypto}")

            # Extract the market cap
            market_cap = row.find("span", class_="sc-11478e5d-0 chpohi")
            if market_cap:
                market_cap = market_cap.text.strip()
            else:
                print(f"Market Cap not found for {crypto}")

            # Extract the volume
            volume = row.find("p", class_="sc-71024e3e-0 bbHOdE font_weight_500")
            if volume:
                volume = volume.text.strip()
            else:
                print(f"Volume not found for {crypto}")

            timestamp = datetime.now()

            data.append(
                [
                    crypto,
                    price,
                    hour_change,
                    day_change,
                    week_change,
                    market_cap,
                    volume,
                    timestamp,
                ]
            )
        else:
            print(f"Data for {crypto} not found")

    except Exception as e:
        print(f"Error retrieving data for {crypto}: {e}")

# Create a DataFrame from the data
df = pd.DataFrame(
    data,
    columns=[
        "Crypto Name",
        "Price",
        "1h %",
        "24h %",
        "7d %",
        "Market Cap",
        "Volume(24h)",
        "TimeStamp",
    ],
)

# Display the DataFrame
print(df)
