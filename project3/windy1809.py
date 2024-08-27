# -*- coding: utf-8 -*-
"""
Project 3 form windy1809
"""

import os
import shutil


directory_path = r"E:\PYTHON CHALLENGE\Example_Folder3"
file_types = {
    "images": [".jpg",".png"],
    "documents": ['.txt', '.csv', '.tsv', '.pdf'],
    "videos": ['.mp4', '.mov'],
    "audio": ['.mp3', '.wav'],
    "compressed": ['.rar', '.zip'],
    "executables": ['.exe', '.dll']
}

images_folder_path = os.path.join(directory_path, 'Images')
videos_folder_path = os.path.join(directory_path, 'Videos')
documents_folder_path = os.path.join(directory_path, 'Documents')
compressed_files_folder_path = os.path.join(directory_path, 'Compressed Files')
audio_files_folder_path = os.path.join(directory_path, 'Audio Files')
executable_files_folder_path = os.path.join(directory_path, 'Executable Files')


for folder in [images_folder_path, videos_folder_path, documents_folder_path, compressed_files_folder_path, audio_files_folder_path, executable_files_folder_path]:
    if not os.path.exists(folder):
        os.makedirs(folder)


for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
        
        _, file_extension = os.path.splitext(item)
        
        
        if file_extension in ['.jpg', '.png']:
            destination_path = os.path.join(images_folder_path, item)
            shutil.move(item_path, destination_path)

        
        elif file_extension in ['.mp4', '.mov']:
            destination_path = os.path.join(videos_folder_path, item)
            shutil.move(item_path, destination_path)
        
       
        elif file_extension in ['.txt', '.csv', '.tsv', '.pdf']:
            destination_path = os.path.join(documents_folder_path, item)
            shutil.move(item_path, destination_path)

        
        elif file_extension in ['.rar', '.zip']:
            destination_path = os.path.join(compressed_files_folder_path, item)
            shutil.move(item_path, destination_path)

        
        elif file_extension in ['.mp3', '.wav']:
            destination_path = os.path.join(audio_files_folder_path, item)
            shutil.move(item_path, destination_path)

        
        elif file_extension in ['.exe', '.dll']:
            destination_path = os.path.join(executable_files_folder_path, item)
            shutil.move(item_path, destination_path)

        else:
            print(f'{item} Invalid file extension.')

print('Files have been sorted successfully')

# Your script is well-structured and efficiently organizes files into their respective folders based on their extensions.

# Areas to improve:

# You might consider adding error handling for the shutil.move operations to manage any potential issues during the file-moving process, such as permission errors or files with the same name.
# Including a way to handle files that don't match any of the predefined categories would make your script more robust and user-friendly.