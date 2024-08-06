import os
from pathlib import Path


def sort_files(path):
    for p in os.listdir(path):
        if os.path.isfile(p):
            filename, file_extension = os.path.splitext(p)
            if len(file_extension) > 0:
                folder_name = file_extension[1:]
            else:
                folder_name = "undefined"
                            
            stored_folder = os.path.join(path, folder_name)
            print(filename, file_extension, stored_folder)

            if not os.path.exists(stored_folder):
                os.makedirs(stored_folder)
            
            os.rename(p, os.path.join(stored_folder, p))
    
path = None
while path is None:
    path = input("Please input path directory: ")
    path = r'{}'.format(path)
    if os.path.exists(path):
        sort_files(path)
    else:
        print("Path does not exist. Please try again")
        path = None