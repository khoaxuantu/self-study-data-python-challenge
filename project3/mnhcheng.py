import os
import shutil

file_path = r'C:\Users\Nguyen Thu Trang\OneDrive\Desktop\Project_3'

folders = ['png_file', 'jpg_file', 'txt_file', 'tsv_file', 'csv_file', 'mp4_file']

#Create folders (and check if exist previous one):
for number in range(0,6):
    if not os.path.exists(fr'{path}\{folders[number]}'):
        os.mkdir(fr'{path}\{folders[number]}')

#Sort files into folders:
files = os.listdir(file_path)

for file in files:
    if ".png" in file and not os.path.exists(fr'{path}\png_file\{file}'):
        shutil.move(fr'{path}\{file}',fr'{path}\png_file\{file}')
    elif ".jpg" in file and not os.path.exists(fr'{path}\jpg_file\{file}'):
        shutil.move(fr'{path}\{file}',fr'{path}\jpg_file\{file}')
    elif ".txt" in file and not os.path.exists(fr'{path}\txt_file\{file}'):
        shutil.move(fr'{path}\{file}',fr'{path}\txt_file\{file}')
    elif ".tsv" in file and not os.path.exists(fr'{path}\tsv_file\{file}'):
        shutil.move(fr'{path}\{file}',fr'{path}\tsv_file\{file}')
    elif ".csv" in file and not os.path.exists(fr'{path}\csv_file\{file}'):
        shutil.move(fr'{path}\{file}',fr'{path}\csv_file\{file}')
    elif ".mp4" in file and not os.path.exists(fr'{path}\mp4_file\{file}'):
        shutil.move(fr'{path}\{file}',fr'{path}\mp4_file\{file}')