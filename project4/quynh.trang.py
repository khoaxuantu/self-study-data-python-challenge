import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL của trang web cần lấy dữ liệu
url = 'https://coinmarketcap.com/'

# Gửi yêu cầu GET đến trang web và lấy nội dung HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm tất cả các thẻ HTML chứa thông tin về các loại tiền ảo
crypto_table = soup.find('table', class_='cmc-table')
crypto_rows = crypto_table.find_all('tr')

data = []

# Lặp qua từng hàng trong bảng để lấy thông tin
for row in crypto_rows[1:]:  # Bỏ qua hàng đầu tiên vì chứa tiêu đề
    cells = row.find_all('td')
    
    # Kiểm tra xem hàng có đủ số cột không trước khi truy cập
    if len(cells) >= 9:  # Ensure the row has enough columns for market cap and 24h volume
        name = cells[2].text
        price = cells[3].text
        one_hour = cells[4].text
        one_day = cells[5].text
        one_week = cells[6].text
        market_cap = cells[7].text
        volume_24h = cells[8].text
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        data.append([timestamp, name, price, one_hour, one_day, one_week, market_cap, volume_24h])

# Tạo DataFrame từ dữ liệu và đặt tên cột
df = pd.DataFrame(data, columns=['Timestamp', 'Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', '24h Volume'])

# In ra DataFrame
print(df)