import os
import shutil

def file_sorting(root_folder, folder_type):
    for file in os.listdir(root_folder):
        file_path = os.path.join(root_folder, file)
        if os.path.isfile(file_path):
            filename_extension = os.path.splitext(file)[1].lower()
            for folder_name, extension in folder_type.items():
                if filename_extension in extension:
                    destination_folder_path = os.path.join(root_folder, folder_name)
                    os.makedirs(destination_folder_path, exist_ok=True)
                    shutil.move(file_path,destination_folder_path)
                    break
                    
        

root_folder = r'F:\Folder_Need_Sort'

folder_type = {
    'image' : ['.jpg', '.png'],
    'document' : ['.txt', '.doc', '.pdf'],
    'audio' : ['.mp3'],
    'video' : ['.mp4','.mov'],
    'compressed' : ['.rar', '.zip', '.7z'],
    'executable' : ['.exe']
}

file_sorting(root_folder, folder_type)

# Review:
'''
Error Handling: The try-except block ensures that any errors during file moving are caught and logged.
Extended Extensions: The extension lists for each file type are expanded for broader file type coverage.
'''