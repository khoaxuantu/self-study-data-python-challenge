# Nice work!

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

url = "https://coinmarketcap.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("table", "sc-7b3ac367-3 etbcea cmc-table")
bitcoin_column_title = table.find_all("th")
bitcoin_title = [column.text for column in bitcoin_column_title][1:-1]
bitcoin_title.append("Timestamp")
bitcoin_rows = table.find_all("tr")[1:]  # skip header
all_data = []
for row in bitcoin_rows:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bitcoin_data = row.find_all("td")
    data = [data.text for data in bitcoin_data][1:-1]
    data.append(current_time)
    all_data.append(data)
    df = pd.DataFrame(all_data, columns=bitcoin_title)
print(df)
