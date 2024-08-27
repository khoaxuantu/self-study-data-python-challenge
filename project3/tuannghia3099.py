import os
import shutil
import csv
import json

os.mkdir(r'D:/Day24Pro3')
path = r'D:/Day24Pro3/'

with open(r'D:/Day24Pro3/CSVfile.csv','w') as write_file:
    write_file.write('First')
with open(r'D:/Day24Pro3/TXTfile.txt','w') as write_file:
    write_file.write('I am doing Project 3')
with open(r'D:/Day24Pro3/TSVfile.tsv','w') as write_file:
    write_file.write('Hi there')
with open(r'D:/Day24Pro3/JSONfile.json','w') as write_file:
    write_file.write('Second')
open(r'D:/Day24Pro3/PNGfile.png','x')
open(r'D:/Day24Pro3/JPGfile.jpg','x')

files = os.listdir(path)

folders_name = ['CSV_fol','TXT_fol','TSV_fol','JSON_fol','PNG_fol','JPG_fol']
for fol in range(0,6):
    if not os.path.exists(path + folders_name[fol]):
        os.makedirs(path + folders_name[fol])

for file in files:
    if '.csv' in file and not os.path.exists(path + 'CSV_fol/' + file):
        shutil.move(path + file, path + 'CSV_fol/' + file )
    elif '.txt' in file and not os.path.exists(path + 'TXT_fol/' + file):
        shutil.move(path + file, path + 'TXT_fol/' + file )
    elif '.tsv' in file and not os.path.exists(path + 'TSV_fol/' + file):
        shutil.move(path + file, path + 'TSV_fol/' + file )
    elif '.json' in file and not os.path.exists(path + 'JSON_fol/' + file):
        shutil.move(path + file, path + 'JSON_fol/' + file )
    elif '.png' in file and not os.path.exists(path + 'PNG_fol/' + file):
        shutil.move(path + file, path + 'PNG_fol/' + file )
    elif '.jpg' in file and not os.path.exists(path + 'JPG_fol/' + file):
        shutil.move(path + file, path + 'JPG_fol/' + file )

# Review:
# Your script effectively creates files and sorts them into appropriate folders, demonstrating a clear understanding of file operations and folder management.
# Areas to improve:
# Path Concatenation: Use os.path.join to handle path concatenation. This improves readability and ensures compatibility across different operating systems. For example:
# os.path.join(path, 'CSV_fol', file)
# File Creation Mode: Using mode 'x' with open raises an error if the file already exists. If your intention is to create new files, consider using mode 'w', which will create the file if it doesn’t exist or overwrite it if it does.
# Check for Existing Files: In the file movement section, the check not os.path.exists(path + 'CSV_fol/' + file) is redundant because the shutil.move function will handle files that are already in the destination. You can simplify this by directly moving the files.