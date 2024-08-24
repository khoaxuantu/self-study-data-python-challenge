# Nice work after all, but the code is not working anymore because the website has updated the div classes and the code is not able to find the table anymore.

import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    filename="coinmarketcap.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

url = "https://coinmarketcap.com/"


def fetch_and_write_data():
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.select_one(
        "div.sc-a980d304-1.iSFeyD.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-7b3ac367-2.cFnHu > table"
    )  # hard-coded path, where it can be changed during the website update, thus this code is not working anymore

    try:
        rows = table.find_all("tr")
        crypto_names = ["BitcoinBTC", "EthereumETH", "BNBBNB"]
        data_to_write = []

        for row in rows:
            cells = row.find_all("td")
            if cells:
                name = cells[2].get_text(strip=True)  # Name of the cryptocurrency
                if any(crypto in name for crypto in crypto_names):
                    cell_data = [cell.get_text(strip=True) for cell in cells]
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                    cell_data.append(timestamp)
                    data_to_write.append(cell_data)

        with open("coinmarketcap.csv", "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            for data_row in data_to_write:
                writer.writerow(data_row)

        logging.info("Data fetched and written to file.")

    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    # Write the header to the CSV file
    with open("coinmarketcap.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Rank",
                "Name",
                "Price",
                "1h %",
                "24h %",
                "7d %",
                "Market Cap",
                "Volume (24h)",
                "Circulating Supply",
                "Timestamp",
            ]
        )

    # Loop to fetch data periodically
    count = 0
    while True:
        fetch_and_write_data()
        time.sleep(60)
        count += 1
        logging.info(f"Fetch iteration {count} completed.")
        if count == 10:
            break

    # Read and process the CSV file
    with open("coinmarketcap.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        hd = [header.upper() for header in next(reader)]  # Convert header to uppercase
        next(reader)  # Skip the second row

        count = 0
        for row in reader:
            count += 1
            if count % 3 == 0:
                logging.info(f"{' | '.join(hd)}\n{'='*102}")
            logging.info(f"{' | '.join(row)}")
