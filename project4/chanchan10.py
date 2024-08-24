# Nice work there, but it would be better if you can save the dataframe to a csv file. Also you should parse the name of crypto more carefully, because your code is currently printing out Name + Symbol.

from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from datetime import datetime

url = "https://coinmarketcap.com/"

try:
    # Gửi yêu cầu và phân tích trang web
    raw = requests.get(url)
    raw.raise_for_status()  # Kiểm tra lỗi HTTP
    soup = BeautifulSoup(raw.text, "html.parser")

    # Tìm bảng dữ liệu
    table = soup.find("table", {"class": "sc-7b3ac367-3 etbcea cmc-table"})
    if table is None:
        raise ValueError("Không tìm thấy bảng dữ liệu trên trang web")

    # Lấy tiêu đề
    titles = table.find_all("p", {"class": "sc-71024e3e-0 fSsxNG"})
    title_list = [title.text for title in titles]
    print("Title:", title_list)

    # Lấy dữ liệu
    rows = []
    for tr in table.tbody.find_all("tr"):
        if tr.td.text == "No data was found for the selected time period.":
            break
        rows.append([x.text for x in tr.find_all("td")])

    cleaned_data = [row[2:-1] for row in rows if len(row) == 11]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame(cleaned_data, columns=title_list)
    df["Timestamp"] = timestamp
    print(df)

    # Lưu dữ liệu vào file CSV
    df.to_csv("C:\\Users\\admin\\Documents\\Learn_Python\\data.csv", index=False)

except requests.RequestException as e:
    print(f"Lỗi khi gửi yêu cầu đến trang web: {e}")
except ValueError as e:
    print(f"Lỗi giá trị: {e}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
