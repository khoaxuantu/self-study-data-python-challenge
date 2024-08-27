import os
import shutil

FILE_TYPES = {
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.bmp': 'Images', '.tiff': 'Images', '.svg': 'Images',
    '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents', '.csv': 'Documents', '.tsv': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents',
    '.xlsx': 'Documents', '.xls': 'Documents', '.rtf': 'Documents',
    '.mp4': 'Videos', '.avi': 'Videos', '.mkv': 'Videos', '.mov': 'Videos', '.wmv': 'Videos', '.flv': 'Videos',
    '.mp3': 'Audio', '.wav': 'Audio', '.aac': 'Audio', '.ogg': 'Audio', '.flac': 'Audio',
    '.zip': 'Compressed', '.rar': 'Compressed', '.tar.gz': 'Compressed', '.7z': 'Compressed', '.gz': 'Compressed', '.bz2': 'Compressed',
    '.exe': 'Executables', '.bat': 'Executables', '.msi': 'Executables', '.sh': 'Executables', '.py': 'Executables'
}

# Day la thu muc chua cac file can sap xep
SOURCE_DIR = r'D:\Test proj 3'

DEST_DIR = r'D:\Test proj 3'
if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

for folder in set(FILE_TYPES.values()):
    dest_folder_path = os.path.join(DEST_DIR, folder)
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)
    if os.path.isfile(file_path):
        name_and_extension = os.path.splitext(filename)
        file_ext = name_and_extension[1]
        dest_folder = FILE_TYPES.get(file_ext, 'Others') 
        dest_folder_path = os.path.join(DEST_DIR, dest_folder)
        if not os.path.exists(dest_folder_path):
            os.makedirs(dest_folder_path)
        shutil.move(file_path, os.path.join(dest_folder_path, filename))

# Review:
# Here are some points you can consider to improve your code:
'''
Error Handling: Consider adding try-except blocks around critical operations like file moving and directory creation. This can help manage unexpected errors, such as permission issues or files that can't be moved.
Handling Case Sensitivity: While file extensions are generally consistent, it's possible to encounter mixed-case extensions. Applying .lower() to file_ext can ensure all cases are handled uniformly.
Handling Duplicate Files: If a file with the same name already exists in the destination folder, the script will raise an error. You might want to check for duplicates and rename the file or skip it to avoid overwriting.
'''

