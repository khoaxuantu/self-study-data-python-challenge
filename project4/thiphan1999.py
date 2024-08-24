# Great work! But you also need to parse the currencies' names because it currently contains the symbol of the currency.

from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://coinmarketcap.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table")
columns_header = [th.text for tr in table.find("thead").find_all("tr") for th in tr]

tr = soup.find("tbody").find_all("tr")
all_data = []
for td in tr:
    row_data = td.find_all("td")
    data = [data.text for data in row_data]
    all_data.append(data)

df = pd.DataFrame(all_data[:10], columns=columns_header)
print(df.to_string())
