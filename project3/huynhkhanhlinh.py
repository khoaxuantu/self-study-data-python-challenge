# -*- coding: utf-8 -*-
"""
Project 3 from huynhkhanhlinh
"""

import os
import shutil

path = '/Users/macos/Downloads'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.heic'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv', '.pptx'],
    'Videos': ['.mp4'],
    'Compressed': ['.zip'],
    'Audio': ['.mp3'],
    'SQL': ['.sql'],
    'Python': ['.ipynb']
}

def sort_files():
    if not os.path.exists(path):
        return

    files = os.listdir(path)
    
    for filename in files:
        file_ext = os.path.splitext(filename)[1].lower()  
        folder = next((category for category, extensions in file_types.items() if file_ext in extensions), None)

        if folder:
            folder_path = os.path.join(path, folder)  
            os.makedirs(folder_path, exist_ok=True)  
            shutil.move(os.path.join(path, filename), folder_path)  

if __name__ == '__main__':
    sort_files()