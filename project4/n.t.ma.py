import os

while True:
    path = input("Nhập đường dẫn đến thư mục chứa các tệp bạn cần phân loại: ").strip()
    if os.path.exists(path):
        break
    print("Đường dẫn bạn nhập không chính xác, vui lòng nhập lại!")

lst_file = os.listdir(path)

map_file_to_folder = {
    ".csv": "Data",
    ".tsv": "Data",
    ".doc": "Document",
    ".docx": "Document",
    ".pdf": "Document",
    ".xls": "Excel",
    ".xlsx": "Excel",
    ".jpg": "Image",
    ".jpeg": "Image",
    ".png": "Image",
    ".mp3": "Audio",
    ".mpeg": "Audio",
    ".mp4": "Video",
}

for file_name in lst_file:
    old_path = os.path.join(path, file_name)
    if os.path.isfile(old_path):
        name, ext = os.path.splitext(file_name)
        if ext in map_file_to_folder:
            folder_name = map_file_to_folder[ext]
            folder_path = os.path.join(path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            new_path = os.path.join(folder_path, file_name)
            os.rename(old_path, new_path)

print("Các tệp đã được phân loại, vui lòng kiểm tra!")


