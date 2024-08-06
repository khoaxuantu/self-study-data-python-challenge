#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import shutil

def sort_files(source_dir):
    # Define file type categories and their respective folders
    file_categories = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
        'Documents': ['pdf', 'docx', 'doc', 'xlsx', 'xls', 'pptx', 'txt', 'csv','tsv'],
        'Videos': ['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv'],
        'Compressed': ['zip', 'rar', 'tar', 'gz', '7z'],
        'Audio': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma'],
        'Executables': ['exe', 'bat', 'sh', 'msi', 'bin']
    }

    # Check for existing folders and create new ones:
    for folder in file_categories.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over files in the source directory
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension 
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower().lstrip('.')
        
        # Sort files into respective folders based on their extensions
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                dest_folder = category
                dest_path = os.path.join(source_dir, dest_folder, file_name)
                shutil.move(file_path, dest_path)
                print(f'Moved {file_name} to {dest_folder}')
                break

if __name__ == "__main__":
    source_directory = r'C:\Users\Admin\Downloads\Project 3-20240804T055426Z-001\Project 3'
    sort_files(source_directory)

