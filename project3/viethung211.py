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

