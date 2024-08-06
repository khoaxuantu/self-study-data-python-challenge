import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    file_name,extension = os.path.splitext(file)

    path_is_checked_exist = os.path.join(path,extension)

    if not os.path.exists(path_is_checked_exist):
        os.makedirs(path_is_checked_exist)
    
    path_of_file_moved = os.path.join(path,file)
    shutil.move(path_of_file_moved,os.path.join(path_is_checked_exist,file))
