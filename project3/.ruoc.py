# Automatic file sorter project
import os
import shutil

path = input("Enter the path of the folder you want to sort: ")
os.chdir(path)
files = os.listdir(path)

os.makedirs('sort_file_project', exist_ok=True)
new_path = os.path.join(path, 'sort_file_project')

for file in files:
    try:
        if os.path.isfile(file):
            extension = file.split('.')[-1]
            folder_name = f'{extension}_files'
            folder_name_path = os.path.join(new_path, folder_name)

            if os.path.exists(folder_name_path):
                shutil.move(os.path.join(path,file), folder_name_path)
            else:
                os.makedirs(folder_name_path)
                shutil.move(os.path.join(path,file), folder_name_path)
    except Exception as e:
        print(e)
print("Please check the result in the folder 'sort_file_project'")