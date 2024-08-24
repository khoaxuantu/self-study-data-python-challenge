#!/usr/bin/env python
# coding: utf-8

# In[110]:


# Set up cơ bản và import các thư viện cần thiết

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = r"https://coinmarketcap.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[111]:


table = soup.find('table') # Get tag <table> trong HTML -> từ đây có thể lấy data -> đưa vào dataframe


# In[112]:


table_headers = table.find_all('th') # Get <th> trong table để làm headers trong dataFrame


# In[113]:


column_names = [columns.text for columns in table_headers][1:-1] # Không lấy cột đầu và cột cuối trong table của Website

column_names


# In[114]:


# Chuyển column_names thành các headers trong DataFrame

df = pd.DataFrame(columns = column_names)
df


# In[115]:


from datetime import datetime

# Thêm cột 'TimeStamp' vào cuối DataFrame với giá trị là thời gian hiện tại -> dùng để track khi nào data được thu thập
df['TimeStamp'] = datetime.now()


# In[116]:


df


# In[117]:


# Sau khi inspect HTML thì ta thấy dữ liệu các dòng của table của nằm trong <tr>:

table_rows = soup.find_all('tr') # Get <tr>

# Extract dữ liệu từ table_rows để đẩy vào dataframe đã được tạo bên trên:

for row in table_rows[1:]:  # Bỏ qua tiêu đề bảng, lấy từ dòng thứ 2 trở đi trong table trên website
    row_data = row.find_all('td')
    
    if len(row_data) >= 9:  # Nếu số lượng cột >= 9, thực hiện xử lý
        values_in_each_cell = []

        for i in range(1, 10):  # Duyệt qua các cột từ 1 đến 9 (đã loại bỏ cột số thứ tự)
            cell_data = row_data[i].text.strip()

            # Xử lý các cột phần trăm với class "icon-Caret-down"
            if i in [3, 4, 5]:  # Các cột 1h%, 24h%, 7d%
                icon = row_data[i].find('span', class_='icon-Caret-down')
                if icon:
                    cell_data = '-' + cell_data  # Thêm dấu trừ (negative numbers) nếu có icon-Caret-down

            values_in_each_cell.append(cell_data)
        
        # Thêm TimeStamp
        values_in_each_cell.append(datetime.now())

        # Thêm hàng vào DataFrame
        df.loc[len(df)] = values_in_each_cell

    else:  # Nếu số lượng cột < 9 -> điền dữ liệu tương ứng, nếu cột nào không có dữ liệu -> N/A
        values_in_each_cell = [row_data[i].text.strip() if i < len(row_data) else 'N/A' for i in range(1, 10)]
        
        # Thêm TimeStamp
        values_in_each_cell.append(datetime.now())
        
        # Thêm hàng vào DataFrame
        df.loc[len(df)] = values_in_each_cell
        
df[:10] # Lấy 10 Coins đầu tiên trong table


# In[121]:


# Export ra file CSV, bỏ cột Index

df.to_csv(r"C:\Users\XPS 9650\Desktop\Excel\coin_marketcap.csv", index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




