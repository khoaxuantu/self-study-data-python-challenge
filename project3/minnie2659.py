import os
import shutil

# Define the directory of folders containing files to be organized
source = 'Project3'

# Define the directories for different file types
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.tsv'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
    'Compressed_Files': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Audio_Files': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Executable_Files': ['.exe', '.bat', '.sh', '.msi']
}

# Ensure target directories exist
for folder in folders:
    os.makedirs(os.path.join(source, folder), exist_ok=True)

# Function to organize files into folders based on their type
def organize_files():
    for file in os.listdir(source):
        file_path = os.path.join(source, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(source, folder, file))
                    break

# Run
organize_files()
