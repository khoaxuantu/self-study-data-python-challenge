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