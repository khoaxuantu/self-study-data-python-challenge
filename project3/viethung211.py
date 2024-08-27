#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil

def organize_files_by_type(main_folder):
    files = [f for f in os.listdir(main_folder) if os.path.isfile(os.path.join(main_folder, f))]
    
    for file in files:
        file_extension = file.split('.')[-1]
        subfolder = os.path.join(main_folder, file_extension)
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        shutil.move(os.path.join(main_folder, file), os.path.join(subfolder, file))
        
main_folder = r'C:\Users\User\Downloads\Main_file'  # my address file main_folder
organize_files_by_type(main_folder)

# Areas to improve:

# Extension Handling: The script assumes that the file extension is always present and separated by a single dot. Files without extensions or with multiple dots (e.g., example.file.txt) might not be handled correctly. Consider using os.path.splitext to handle extensions more reliably.
# Error Handling: Adding error handling for file operations would make the script more robust. For instance, handling exceptions when creating directories or moving files can prevent the script from crashing unexpectedly.

