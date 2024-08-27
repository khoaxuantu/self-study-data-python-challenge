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

# Review:
# Good job on completing this project!
# Here are some points you can improve your project, keep it up!
'''
1. Handling Non-Matching Files:
If a file's extension doesn't match any in the category dictionary, it won't be moved. You might want to log these or move them to a separate "others" folder.
2. Improved Error Handling:
The current setup handles known file types well, but for unknown file types, it only prints a message. You might want to log these unknown files or handle them differently.
'''