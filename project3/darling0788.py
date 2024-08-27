import os
import shutil

# Đường dẫn tới thư mục chứa các file
source_dir = r'C:\Users\ASUS\Desktop\Project 3'

# Tạo các sub-folder tương ứng với từng loại file
directories = {
    "Documents": [".txt", ".doc", ".docx", ".pdf",".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Compressed_Files": [".zip", ".rar", ".7z"],
    "Audio_Files": [".mp3", ".wav", ".aac"],
    "Executables": [".exe", ".bat"]
}

for folder in directories:
    path = os.path.join(source_dir, folder)
    if not os.path.exists(path):
        os.makedirs(path)

# Lấy danh sách các file trong folder gốc
files = os.listdir(source_dir)

# Phân loại file vào các sub-folder
for file in files:
    file_path = os.path.join(source_dir, file)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file)[1].lower() # Lấy phần mở rộng để định dạng file
        
        # Di chuyển file vào các sub-folder tương ứng
        for folder, types in directories.items():
            if file_extension in types:
                dest_path = os.path.join(source_dir, folder, file)
                shutil.move(file_path, dest_path)
                print('Moved', file, 'to', folder)
                break
# Review:
'''
Handling Unrecognized File Types: Add an "Others" category for files that don't match any predefined extensions.
Use of exist_ok=True: When creating directories, you can simplify the check by using os.makedirs(path, exist_ok=True).
Avoid Hardcoding Paths: Consider allowing users to input the source_dir or using a command-line argument to make the script more flexible.
'''