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
# Review:
# Good job on completing this project, but here are some points you can look through to improve it:
'''
Currently, your script might fail or create an empty folder if it encounters files without extensions. To handle this, you could add a check for files with no extensions and place them in an "Others" folder.
The script reads the list of files and splits their extensions twice, once when generating the list of unique types and again when building the dictionary. You can optimize this by generating the dictionary first and then creating folders based on its keys.
Only suggestion but I think spliting into different types of file may make the code more organized and stick to the requirement more! E.g: Documents, Audio, Compressed, etc
'''