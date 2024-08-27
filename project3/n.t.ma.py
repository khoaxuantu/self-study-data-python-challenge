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

print("Các tệp đã được phân loại!")


# Review:
# Good job on completing this project, here are some points to improve it:
'''
Hidden Files: Ensure that hidden files or files without extensions are handled or reported.
Duplicate Files: Consider handling cases where files with the same name might be moved to the same folder.
Handle Different File Types: Include a category for unrecognized file types to avoid silently ignoring files that do not match any listed extensions.
Exception Handling: Including try-except blocks around critical operations (like moving files) could help gracefully handle unexpected errors such as permission issues or read/write errors.
'''