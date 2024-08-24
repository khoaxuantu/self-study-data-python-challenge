# Great work! Keep it up!

import pandas as pd
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import time
from datetime import datetime
import os

url = "https://coinmarketcap.com"
headers = {"Cache-Control": "no-cache", "Pragma": "no-cache"}


def fetch_data(cryptocurrencies):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    header = [value.text for value in soup.find("thead").find("tr").find_all("th")]
    exclude_indices = {0, 1, 9, 10}
    header_filtered = [
        value for i, value in enumerate(header) if i not in exclude_indices
    ]
    header_filtered.append("Timestamp")

    body = soup.find("tbody")
    rows = body.find_all("tr")
    table_data = []
    table_data.append(header_filtered)
    for row in rows:
        row_data = []
        cells = row.find_all("td")

        if cells[2].text not in cryptocurrencies:
            continue

        for index, cell in enumerate(cells):
            if index in exclude_indices:
                continue

            p_tag = cell.find("p")
            if p_tag:
                spans = p_tag.find_all("span")
                if len(spans) > 1:
                    cell_text = spans[1].text
                else:
                    cell_text = p_tag.text
            else:
                icon_caret_down = cell.find("span", class_="icon-Caret-down")
                if icon_caret_down:
                    cell_text = "-" + cell.text
                else:
                    cell_text = cell.text

            row_data.append(cell_text)

        table_data.append(row_data)

    return table_data


cryptocurrencies = ["BitcoinBTC", "EthereumETH", "BNBBNB"]

while True:
    table_data = fetch_data(cryptocurrencies)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    table_data_with_timestamp = [table_data[0]] + [
        row + [timestamp] for row in table_data[1:]
    ]
    df = pd.DataFrame(
        table_data_with_timestamp[1:], columns=table_data_with_timestamp[0]
    )

    if os.path.isfile("cryptocurrency_data.csv"):
        df.to_csv("cryptocurrency_data.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("cryptocurrency_data.csv", mode="w", header=True, index=False)

    print(tabulate(table_data_with_timestamp, headers="firstrow", tablefmt="grid"))
    time.sleep(10)
