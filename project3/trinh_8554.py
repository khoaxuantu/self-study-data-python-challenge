# -*- coding: utf-8 -*-
"""Project3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pV_6GPw6xlsgPPIPjgAwCerki9OX6WQq
"""

import os
import shutil

list_file = ['angrycat.jpg', 'CSVFile.csv', 'CSVFile.zip',
             'FakeFile.txt', 'Max.PNG', 'Rosie.PNG',
             'NewFile.tsv']

os.mkdir(r'CSV_FILE_FILE')
os.mkdir(r'IMAGE_FILE')
os.mkdir(r'ZIP_FILE')
os.mkdir(r'TXT_FILE')

directories = {
    'jpg': 'IMAGE',
    'png': 'IMAGE',
    'txt': 'TXT_file',
    'csv': 'CSV_file',
    'zip': 'TXT_file'
}

for dir in directories.values():
    os.makedirs(dir, exist_ok=True)

for file in list_file:
    extension = file.split('.')[-1].lower()

    if extension in directories:
        target_dir = directories[extension]
        try:
            shutil.move(file, os.path.join(target_dir, file))
            print(f"Moved {file} to {target_dir} folder")
        except FileNotFoundError:
            print(f"File {file} not found. Skipping.")
        except Exception as e:
            print(f"Error moving {file}: {e}")

print("All files have been processed.")