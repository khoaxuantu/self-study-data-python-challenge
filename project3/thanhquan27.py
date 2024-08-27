#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import 2 thư viện cần thiết để làm việc với system
import os
import shutil

# Khai báo đường dẫn đến folder chứa các file cần di chuyển
source_directory = r"C:\Users\XPS 9650\Desktop\Source"

# Khai báo đường dẫn đến folder chứa các sub_folder mà các file cần di chuyển đến
destination_directory = r"C:\Users\XPS 9650\Desktop\Destination"

# Định nghĩa các sub_folder tương ứng với từng loại file
folders = {
    'Video': os.path.join(destination_directory, 'Video'),
    'Audio': os.path.join(destination_directory, 'Audio'),
    'Photo': os.path.join(destination_directory, 'Photo'),
    'csv': os.path.join(destination_directory, 'csv'),
    'txt': os.path.join(destination_directory, 'txt'),
    'json': os.path.join(destination_directory, 'json'),
    'tsv': os.path.join(destination_directory, 'tsv')
}

# Tạo các folder (nếu chưa tồn tại) để chuyển files vào
for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

# Import "contextmanager" decorator từ thư viện "contextlib" để tạo ra context manager tùy chỉnh
from contextlib import contextmanager

# Context manager này dùng để di chuyển tệp
# Sử dụng @contextmanager để đánh dấu một function như là một context manager.
# Function này là một generator function, sử dụng từ khóa yield.
@contextmanager 
def move_file(file_path, destination_folder):
    try:
        yield
    finally: # di chuyển tệp từ file_path đến destination_folder, đảm bảo rằng hành động này được thực hiện khi khối "with" kết thúc. 
        destination = os.path.join(destination_folder, os.path.basename(file_path))
        shutil.move(file_path, destination)
        print(f"Moved {file_path} to {destination_folder}")

# Tạo hàm phân loại và di chuyển tệp dựa trên phần mở rộng
def move_files_based_on_extension():
    for file_name in os.listdir(source_directory): #Lấy tất tên sub_folders và tên file(bao gồm phần mở rộng) trong source_directory và trả về ở dạng List
        file_path = os.path.join(source_directory, file_name) # Tạo đường dẫn đầy đủ đến tệp trong thư mục nguồn
#VD: nếu source_directory = "C:\Users\XPS 9650\Downloads\Source" và file_name = "CSVFile.csv" thì đường dẫn đầy đủ sẽ join 2 cái này lại thành "C:\Users\XPS 9650\Downloads\Source\CSVFile.csv"
        
        
        if os.path.isfile(file_path): # Lấy file, không phải sub_folders
            ext = os.path.splitext(file_path)[1].lower() #Lấy phần mở rộng của file, lower() để đảm bảo phần mở rộng được đồng nhất
   
 # Xác định thư mục đích dựa trên phần mở rộng của file -> đẩy vào folders tương ứng         
            if ext in ['.mp4', '.avi']:
                folder = folders['Video']
            elif ext in ['.mp3', '.m4a']:
                folder = folders['Audio']
            elif ext in ['.jpg', '.png']:
                folder = folders['Photo']
            elif ext == '.csv':
                folder = folders['csv']
            elif ext == '.txt':
                folder = folders['txt']
            elif ext == '.json':
                folder = folders['json']
            elif ext == '.tsv':
                folder = folders['tsv']
            else:
                print(f"Unknown file type: {file_name}")
                continue
            
            # Sử dụng context manager để di chuyển tệp
            with move_file(file_path, folder):
                pass

# Gọi hàm vừa tạo để di chuyển files tự động dựa trên phần mở rộng của files
move_files_based_on_extension()

# Review: Here are some points you can improve for your code!
'''
1. Context Manager Usage:
You've correctly used a context manager with @contextmanager to move files, ensuring that the file movement operation is performed at the end of the block. This is a good use of context managers for handling file operations safely.
2. Handling Edge Cases:
If a file already exists in the destination folder with the same name, the current code will overwrite it. If this behavior is not desired, you may want to add a check to rename the file before moving it.
3. Improved Error Handling:
The current setup handles known file types well, but for unknown file types, it only prints a message. You might want to log these unknown files or handle them differently.
4. Optimization Tip:
Instead of using multiple if-elif conditions to match file extensions, you could use a dictionary to map extensions to folders, similar to how you map folder names in the folders dictionary. This would make the code more scalable and easier to manage.
5. Code Readability:
Your code is already quite readable, but adding more comments explaining each section (e.g., for less experienced readers) could be beneficial. You might also consider using consistent naming conventions, such as using target_folder instead of just folder for clarity.
'''

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




