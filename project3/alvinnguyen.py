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
    
    