#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import shutil

def organize_files_by_type_and_extension(main_folder):
    category_types = {
        'Images': ['jpg', 'png'],
        'Documents': ['txt', 'pdf', 'csv', 'tsv'],
        'Videos': ['mp4', 'avi'],
        'Compressed Files': ['zip', 'rar'],
        'Audio Files': ['mp3', 'wav'],
        'Executable Files': ['exe', 'bat']
    }
    
    files = [f for f in os.listdir(main_folder) if os.path.isfile(os.path.join(main_folder, f))]

    for category in category_types:
        category_path = os.path.join(main_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    for file in files:
        file_extension = file.split('.')[-1].lower()
        moved = False
        
        for category, extensions in category_types.items():
            if file_extension in extensions:
                category_folder = os.path.join(main_folder, category)
                specific_folder = os.path.join(category_folder, f"{file_extension.upper()}Folder")
                
                if not os.path.exists(specific_folder):
                    os.makedirs(specific_folder)
                
                shutil.move(os.path.join(main_folder, file), os.path.join(specific_folder, file))
                moved = True
                break
        
        if not moved:
            print(f"Warning: File '{file}' has an unknown extension and will not be moved.")

main_folder = "Project 3" 
organize_files_by_type_and_extension(main_folder)


# In[ ]:




