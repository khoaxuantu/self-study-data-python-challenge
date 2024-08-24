# Great work! But you should also parse the currencies' names because it currently contains the symbol of the currency.

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    re_content = response.content
else:
    print("This web cannot access")
soup = BeautifulSoup(re_content, "html.parser")
table = soup.find("table", class_="sc-7b3ac367-3 etbcea cmc-table")
world_columns = table.find_all("th")
first_title = [columns.text for columns in world_columns]
pf = pd.DataFrame(columns=first_title)
row_data = table.find_all("tr")
for rows in row_data[1:10]:
    each_row = rows.find_all("td")
    individual = [i.text for i in each_row]
    if len(first_title) == len(individual):
        length = len(pf)
        pf.loc[length] = individual
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pf["Timestamp"] = current_time
print(pf.to_string())
