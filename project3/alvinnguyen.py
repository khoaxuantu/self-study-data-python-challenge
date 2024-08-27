import os
import shutil

path = r'C:/Users/Admin/Desktop/Project 3/'

folder_name = ['csv files', 'txt files', 'image files', 'xlsx files', 'other files']

for name in folder_name:
    if not os.path.exists(path + "/" + name):
        os.mkdir(path + "/" + name)
       
filename = os.listdir(path)

for file in filename:
    if ".csv" in file:
        shutil.move(path + file, path + 'csv files/'+ file)
    elif ".txt" in file:
        shutil.move(path + file, path + 'txt files/'+ file)
    elif ".jpg" in file or ".png" in file:
        shutil.move(path + file, path + 'image files/'+ file)
    elif ".xlsx" in file:
        shutil.move(path + file, path + 'xlsx files/'+ file)
    elif ".tsv" in file:
        shutil.move(path + file, path + 'other files/'+ file)
    else:
        print("This file type not have it own directory")
    

# Review:
'''
Use os.path.join for Path Construction: This ensures compatibility across different operating systems and avoids potential issues with path separators.
Check File Extension More Robustly: Instead of using in to check for file extensions, use os.path.splitext to handle extensions more reliably.
Avoid Hardcoding Paths: Use variables or configuration files for paths to make the code more flexible and maintainable.
Remove Redundant Directory Creation Check: The directory creation logic is correct but could be simplified by using os.makedirs with exist_ok=True to create directories and avoid a separate check.
Refactor File Type Handling: Use a dictionary to map file extensions to their target directories for cleaner and more scalable code.
'''