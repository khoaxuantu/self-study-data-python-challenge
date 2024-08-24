import os
import shutil

path = "C:\\Users\\ADMIN\\OneDrive\\Tài liệu\\My_folder"
os.chdir(path)

lst_files = os.listdir()

types = [x.split(".")[-1] for x in lst_files]
unique_type = list(set(types))

for type in unique_type:
    if not os.path.exists(path + "\\" + type):
        os.mkdir(path + "\\" + type)
        
files_and_type = {file_name: file_name.split(".")[-1]  for file_name in lst_files}
print(files_and_type.items())
for f, t in files_and_type.items():
    shutil.move(path + "\\" + f, path + "\\" + t + "\\" + f)