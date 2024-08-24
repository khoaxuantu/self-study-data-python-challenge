import os
import shutil


file_types = {
    "Sound": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Compressed": [".rar", ".zip", ".7z", ".tar"],
    "Text": [".txt", ".md"],
    "Spreadsheet": [".csv", ".tsv", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
}


base_directory = "path/to/your/directory"

for folder in file_types.keys():
    folder_path = os.path.join(base_directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

files = [f for f in os.listdir(base_directory) if os.path.isfile(os.path.join(base_directory, f))]

for file in files:
    file_path = os.path.join(base_directory, file)
    for folder, extensions in file_types.items():
        if any(file.endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(base_directory, folder, file))
            break


def print_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        # Sắp xếp các tệp theo kích thước tăng dần
        files = sorted(files, key=lambda x: os.path.getsize(os.path.join(root, x)))
        for f in files:
            size = os.path.getsize(os.path.join(root, f)) / (1024 * 1024)  # Kích thước tệp tính bằng MB
            print(f"{subindent}{f} {size:.1f}M")


print_tree(base_directory)
