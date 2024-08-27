import os
import shutil

initial_folder = r'D:\Folder_organized' #thu muc chua cac tep can sap xep

def file_organized(initial_folder, TypeOfFolder):
    for file in os.listdir(initial_folder):
        create_file_path = os.path.join(initial_folder, file)
        if os.path.isfile(create_file_path):
            file_extension = os.path.splitext(file)[1].lower()
            for NameOfFolder, extension in TypeOfFolder.items():
                if file_extension in extension:
                    dst_path = os.path.join(initial_folder, NameOfFolder)
                    os.makedirs(dst_path, exist_ok = True)
                    shutil.move(create_file_path,dst_path)
                    break

TypeOfFolder = {
    'audios' : ['.mp3'],              #file am thanh
    'compressed' : ['.zip', '.rar'],  #file nen
    'videos' : ['.mp4'],              #file video
    'executable' : ['.exe', '.msi'],  #file thuc thi
    'images' : ['.jpg'],              #file hinh anh
    'documents' : ['.txt', '.docx', '.pdf'],   #file tai lieu
}

file_organized(initial_folder, TypeOfFolder)
#Review:
# Your script efficiently organizes files into folders based on their extensions, and the use of a dictionary to map file types to extensions is a good approach.

# Areas to improve:

# Folder Creation: While you correctly create folders if they don’t exist, it might be more efficient to ensure folder creation is done outside the loop for better performance, especially if the folder already exists.
# File Extension Handling: Your script uses os.path.splitext to handle file extensions, which is correct. However, you might want to handle cases where files don't have an extension or have multiple dots more gracefully.
# Edge Cases: Consider adding error handling for cases where shutil.move might fail, such as when files cannot be moved due to permissions or if a file with the same name already exists in the destination folder.