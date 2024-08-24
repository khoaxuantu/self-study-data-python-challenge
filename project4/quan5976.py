# Great work!

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def get_crypto_data(crypto_name):
    url = "https://coinmarketcap.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    row = soup.find("a", href=f"/currencies/{crypto_name}/")
    if row:
        parent = row.find_parent("tr")
        if parent:
            # Lấy thông tin tiền điện tử
            price = (
                parent.find("div", class_="sc-b3fc6b7-0 dzgUIj")
                .find("span")
                .text.strip()
            )
            changes = parent.find_all("span", class_="sc-a59753b0-0")
            change_1h = changes[0].text.strip() if len(changes) > 0 else "N/A"
            change_24h = changes[1].text.strip() if len(changes) > 1 else "N/A"
            change_7d = changes[2].text.strip() if len(changes) > 2 else "N/A"
            market_cap = parent.find("span", class_="sc-11478e5d-0 chpohi").text.strip()
            volume_24h = (
                parent.find("div", class_="sc-4c05d6ef-0 sc-97d9abce-0 dlQYLv bJRjhz")
                .find("p")
                .text.strip()
            )
            timestamp = datetime.now()

            return {
                "STT": None,
                "Crypto Name": crypto_name.capitalize(),
                "Price": price,
                "1h %": change_1h,
                "24h %": change_24h,
                "7d %": change_7d,
                "Market Cap": market_cap,
                "24h Volume": volume_24h,
                "Timestamp": timestamp,
            }
    return None


# Danh sách tiền điện tử
crypto_list = ["bitcoin", "ethereum", "bnb"]

# Tạo bảng
data = []
for stt, crypto_name in enumerate(crypto_list, start=1):
    result = get_crypto_data(crypto_name)
    if result:
        result["STT"] = stt
        data.append(result)

df = pd.DataFrame(data)
print(df.to_string(index=False))
