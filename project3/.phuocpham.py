import os
import shutil

def sorting_file():
    working_dir = input("Enter the path to the targeting directory: ")
    os.chdir(working_dir)
    file_lst = os.listdir()
    for file_name in file_lst:
        if(not os.path.isfile(file_name)):
            continue
        reverse_name = file_name[::-1]
        pos = reverse_name.find('.')
        type_file = reverse_name[:pos]
        type_file = type_file[::-1]
        type_file += 'Folder'
        if not os.path.exists(type_file):
            os.mkdir(type_file)
        shutil.move(file_name, type_file)

sorting_file()