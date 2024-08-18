#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
from pathlib import Path

def is_valid_directory(path):
    return os.path.exists(path) and os.path.isdir(path)

def get_valid_directory():
    while True:
        source_directory = input("Nhập đường dẫn đến thư mục chứa các tệp cần sắp xếp: ")
        if is_valid_directory(source_directory):
            return source_directory
        else:
            print("Đường dẫn không hợp lệ. Vui lòng nhập lại.")
            print("Ví dụ đường dẫn hợp lệ:")
            print("- Windows: C:\\Users\\TenNguoiDung\\Documents")
            print("- macOS/Linux: /home/TenNguoiDung/Documents")

def sort_files(source_dir):
    # Định nghĩa các loại tệp tin và thư mục tương ứng
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Audio': ['.mp3', '.wav', '.ogg', '.flac'],
        'Executables': ['.exe', '.msi', '.bat']
    }

    # Tạo thư mục cho mỗi loại tệp tin
    for folder in file_types:
        Path(os.path.join(source_dir, folder)).mkdir(exist_ok=True)

    # Duyệt qua tất cả các tệp trong thư mục nguồn
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        if os.path.isfile(file_path):
            # Lấy phần mở rộng của tệp
            file_ext = os.path.splitext(file)[1].lower()
            
            # Tìm thư mục phù hợp cho tệp
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    # Di chuyển tệp vào thư mục tương ứng
                    dest_path = os.path.join(source_dir, folder, file)
                    shutil.move(file_path, dest_path)
                    print(f"Đã di chuyển {file} vào thư mục {folder}")
                    break
            else:
                print(f"Không thể phân loại tệp: {file}")

# Sử dụng hàm
source_directory = get_valid_directory()
sort_files(source_directory)

print("Quá trình sắp xếp đã hoàn tất.")


# In[ ]:




