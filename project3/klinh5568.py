import os
import shutil

# Định nghĩa thư mục nguồn chứa các tập tin cần tổ chức
source_directory = r'C:\Users\TGDD\OneDrive\Documents\Python\Project 3'

# Định nghĩa các thư mục đích cho các loại tập tin khác nhau
extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.csv', '.tsv', '.ppt', '.pptx', '.xlsx', '.xls', '.rtf'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'Audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac'],
    'Compressed': ['.zip', '.rar', '.tar.gz', '.7z', '.gz', '.bz2'],
    'Executables': ['.exe', '.bat', '.msi', '.sh', '.py'],
}

# Tạo thư mục cho mỗi loại tập tin nếu chúng chưa tồn tại
for category in extensions.keys():
    target_directory = os.path.join(source_directory, category)
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

# Di chuyển các tập tin vào thư mục tương ứng dựa trên phần mở rộng của chúng
for item in os.listdir(source_directory):
    item_path = os.path.join(source_directory, item)
    if os.path.isfile(item_path):
        file_extension = '.' + item.split('.')[-1].lower()
        moved = False
        for category, exts in extensions.items():
            if file_extension in exts:
                destination_folder = os.path.join(source_directory, category)
                shutil.move(item_path, os.path.join(destination_folder, item))
                moved = True
                break
        if not moved:
            print(f"Tập tin không được nhận dạng: {item}")

print("Tập tin đã được tổ chức thành công.")

# Review
# Good job on completing the project, here are some points you may consider to improve your code:
'''
The way you extract the file extension (file_extension = '.' + item.split('.')[-1].lower()) works fine, but os.path.splitext(item)[1].lower() is a more robust method, especially for files with multiple dots in their names.
Instead of just printing a message for unrecognized file types, you might consider moving them to a separate folder (e.g., "Others"). This way, all files are organized, and you can later review which files were not categorized.
'''
