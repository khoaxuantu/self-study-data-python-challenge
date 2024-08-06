import os
import shutil


def organize_files(folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt', '.md'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Compressed': ['.zip', '.rar', '.tar.gz'],
        'Executable': ['.exe', '.bat', '.com', '.cmd', '.inf', '.ipa', '.osx', '.pif', '.run', '.wsh']
    }
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            file_ext = os.path.splitext(file)[1].lower()
            destination_folder = next((ftype for ftype, exts in file_types.items() if file_ext in exts), 'Others')

            os.makedirs(os.path.join(folder, destination_folder), exist_ok=True)
            shutil.move(os.path.join(folder, file), os.path.join(folder, destination_folder, file))
    print("Files Organized!")


path = 'D://H4TF'  # Replace with the path to your folder
organize_files(path)