import os
import shutil

initial_folder = r'D:\Ngọc Hân Princess\Folder_organized' #thu muc chua cac tep can sap xep

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