# Nice work! But you should parse the name more carefully, as currently it includes the ticker symbol.

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


# Function to fetch and parse the page
def fetch_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


# Function to get table columns
def get_columns(table):
    return [th.text for th in table.find_all("th")[2:9]] + ["timestamp"]


# Function to extract row data
def extract_row_data(row, timestamp):
    data = [td.text.strip() for td in row.find_all("td")[2:9]]
    return data + [timestamp]


# Function to filter rows by coin names and collect their data
def filter_and_collect_data(coin_rows, coins):
    timestamp = datetime.datetime.now()
    filtered_data = [
        extract_row_data(row, timestamp)
        for row in coin_rows[1:]
        if row.find_all("td")[2].text.replace(" ", "").lower() in coins
    ]
    return filtered_data


# Main function to scrape and organize data into a DataFrame
def scrape_crypto_data(coins, url):
    soup = fetch_page_content(url)
    table = soup.find("table", {"class": "sc-7b3ac367-3 etbcea cmc-table"})
    coin_rows = table.find_all("tr")

    # Preprocess coin names for comparison
    processed_coins = [coin.lower() for coin in coins]

    # Extract data
    data = filter_and_collect_data(coin_rows, processed_coins)

    # Create DataFrame
    columns = get_columns(table)
    return pd.DataFrame(data, columns=columns)


# List of coins to scrape
coins = ["BitcoinBTC", "EthereumETH", "BNBBNB"]

# URL to scrape
url = "https://coinmarketcap.com/"

# Scraping the data and storing it in the DataFrame
df = scrape_crypto_data(coins, url)

# Print the DataFrame
print(df)
