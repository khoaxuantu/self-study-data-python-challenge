# Your code is unrunnable due to line 44. Anw, good job!

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

url = "https://coinmarketcap.com/"

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

# Tìm table chứa dữ liệu
table = soup.find("table", "sc-7b3ac367-3 etbcea cmc-table")
col = table.find_all("th")

columns_name = [columns.text for columns in col]

df = pd.DataFrame(columns=columns_name)

rows = table.find_all("tr")

for row in rows[1:10]:
    row_data = row.find_all("td")
    coin_row_data = []
    for data in row_data:
        if data.find("p", "sc-71024e3e-0 ehyBa-d"):
            name = data.find("p", "sc-71024e3e-0 ehyBa-d").text
            coin_row_data.append(name)
        elif data.find("span", "sc-11478e5d-0 chpohi"):
            market_cap_value = data.find("span", "sc-11478e5d-0 chpohi").text.strip()
            coin_row_data.append(market_cap_value)
        elif data.find("p", "sc-71024e3e-0 bbHOdE font_weight_500"):
            vol_24h = data.find(
                "p", "sc-71024e3e-0 bbHOdE font_weight_500"
            ).text.strip()
            coin_row_data.append(vol_24h)
        else:
            coin_row_data.append(data.text.strip())

    length = len(df)
    df.loc[length] = coin_row_data

# Loại bỏ các cột không cần thiết
col_drop = ["#", "Circulating Supply", "Last 7 Days"]
df = df.drop(columns=col_drop)
d
current_time = datetime.datetime.now()
df["Timestamp"] = current_time

df = df[df["Name"].isin(["Bitcoin", "Ethereum", "BNB"])]
df.reset_index(drop=True, inplace=True)
pd.set_option("display.max_columns", None)
print(df)
