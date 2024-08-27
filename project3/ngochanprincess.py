import os
import shutil

initial_folder = r'D:\Test proj 3' #thu muc chua cac tep can sap xep

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

# Review:
# Here are some points you can look through to improve your code:
'''
Handling Files Without Extensions:vCurrently, files without extensions or with unknown extensions will not be moved. You might want to add a fallback mechanism to handle these files, possibly moving them to an "Others" or "Unknown" folder.
Overwriting Conflicts: If two files with the same name exist in the same folder, shutil.move will overwrite the existing file. You might consider adding a mechanism to rename files if a conflict is detected.
Exception Handling: Including try-except blocks around critical operations (like moving files) could help gracefully handle unexpected errors such as permission issues or read/write errors.
'''