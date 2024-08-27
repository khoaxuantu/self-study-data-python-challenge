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
# Review:
'''
Incorrect File Path Handling: The code is currently checking and working with paths relative to the current working directory rather than the specified path. When using os.listdir(path), the loop variable p only contains the filename, not the full path. This leads to issues when attempting to move files using os.rename() because it doesn't have the correct source path.
os.rename() Usage:The os.rename() function requires both the source and destination paths to be absolute paths, but the code provides only the filename as the source path (p). This causes an error since os.rename() cannot find the file.
Path Handling with os.path.isfile(): The os.path.isfile(p) check is looking for the file in the current working directory instead of the provided directory path. This is because p is just the filename and not the full path to the file.
'''