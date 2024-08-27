# -*- coding: utf-8 -*-
"""
Project 3 from Zoe
"""
import os
import shutil

# Path dẫn đến folder muốn lọc files
directory_path = r'C:\Users\Admin\Python 35-days Challenge\Project 3'

# Tạo path dẫn đến các folder mới
images_folder_path = os.path.join(directory_path, 'Images')
videos_folder_path = os.path.join(directory_path, 'Videos')
documents_folder_path = os.path.join(directory_path, 'Documents')
compressed_files_folder_path = os.path.join(directory_path, 'Compressed Files')
audio_files_folder_path = os.path.join(directory_path, 'Audio Files')
executable_files_folder_path = os.path.join(directory_path, 'Executable Files')

# Tạo các folders mới 
for folder in [images_folder_path, videos_folder_path, documents_folder_path, compressed_files_folder_path, audio_files_folder_path, executable_files_folder_path]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Duyệt từng phần tử trong folder (bỏ qua folders mới vừa tạo)
for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
        # Lấy phần mở rộng tệp
        _, file_extension = os.path.splitext(item)
        
        # Chuyển file đuôi .jpg & .png vào folder ảnh
        if file_extension in ['.jpg', '.png']:
            destination_path = os.path.join(images_folder_path, item)
            shutil.move(item_path, destination_path)

        # Chuyển file đuôi .mp4 & .mov vào folder video
        elif file_extension in ['.mp4', '.mov']:
            destination_path = os.path.join(videos_folder_path, item)
            shutil.move(item_path, destination_path)
        
        # Chuyển file đuôi .txt, .csv, .tsv, .pdf vào folder Documents
        elif file_extension in ['.txt', '.csv', '.tsv', '.pdf']:
            destination_path = os.path.join(documents_folder_path, item)
            shutil.move(item_path, destination_path)

        # Chuyển file đuôi .rar, .zip vào folder Compressed Files
        elif file_extension in ['.rar', '.zip']:
            destination_path = os.path.join(compressed_files_folder_path, item)
            shutil.move(item_path, destination_path)

        # Chuyển file đuôi .mp3, .wav vào folder Audio Files
        elif file_extension in ['.mp3', '.wav']:
            destination_path = os.path.join(audio_files_folder_path, item)
            shutil.move(item_path, destination_path)

        # Chuyển file đuôi .dll, .exe vào folder Executable Files
        elif file_extension in ['.exe', '.dll']:
            destination_path = os.path.join(executable_files_folder_path, item)
            shutil.move(item_path, destination_path)

        else:
            print(f'{item} không có phần mở rộng hợp lệ.')

print('Đã chuyển các files xong.')

# Great job implementing the file sorting logic! You've successfully handled six different file types, which meets the highest bonus point criteria. The code is well-structured and clear.
# However, there still some areas to improve:
# Consider adding error handling for cases where files cannot be moved or folders cannot be created.
# It might be useful to include sorting for additional file types or create a general folder for unsupported files.