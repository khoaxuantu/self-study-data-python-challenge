import requests
from bs4 import BeautifulSoup

# URL for the Bitcoin page on CoinMarketCap
url = "https://coinmarketcap.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant HTML elements and extract the data
table = soup.find("table", class_="sc-7b3ac367-3 etbcea cmc-table")
if table:
    headers = [header.text for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)

    print(headers)
    for row in rows[:10]:
        print(row)
else:
    print("Table not found on CoinMarketCap. Website structure might have changed.")
