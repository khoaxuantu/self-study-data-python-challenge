# Great work! Keep it up!

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_html_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page: Status code {response.status_code}")
        return None


def parse_nft_data(html_data):
    result = []
    parser = BeautifulSoup(html_data, "html.parser")

    # Find the row for Bitcoin, assuming Bitcoin is the first row in the table
    # This might need adjustment if the structure of the page changes
    table = parser.find("table", class_="cmc-table")

    if table is None:
        return None

    names = table.find("tr")
    names = names.find_all("th")
    names = [name.get_text(strip=True) for name in names]
    names.append("TimeStamp")

    result.append(names)

    # Body
    data = table.find("tbody")
    if data is None:
        return None

    rows = data.find_all("tr", style="cursor:pointer")

    for row in rows:
        col = row.find_all("td")

        data = []
        for i, c in enumerate(col):
            name = names[i]
            text = c.get_text("|", strip=True)

            if name == "Market Cap" or name == "Volume(24h)":
                texts = text.split("|")
                text = f"{texts[0]} ({texts[1]})"

            data.append(text)
        data.append(datetime.now().__str__())

        result.append(data)
    return result


def print_result(result):
    max_lengths = [max(len(str(item)) for item in column) for column in zip(*result)]

    sep = "-".join(["-" * l for l in max_lengths])

    for no, r in enumerate(result):
        if no in [0, 1]:
            sep = "-".join(["-" * l for l in max_lengths])
            print(sep)
        for i, item in enumerate(r):
            print(item.ljust(max_lengths[i]), end="|")
        print()
    print(sep)


def __main__():
    html_data = get_html_data("https://coinmarketcap.com/")
    # Open data from html file
    # with open('bitcoin_table.html', 'r') as file:
    #     html_data = file.read()

    result = parse_nft_data(html_data)
    if result is None:
        print("Failed to parse the data")
        exit()

    print_result(result)


__main__()
