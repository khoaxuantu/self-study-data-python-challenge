#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import os
import shutil


# In[35]:


def org_files(dirc):
    file_types = {
        'csv': 'Microsft Excel Comma Separated',
        'tsv': 'TSV_files',
        'pdf': 'PDF_files',
        'jpg': 'Images',
        'png':  'Images',
        "mp3": "Music",
        "mp4": "Videos",
        "zip": "Archives",
        "rar": "Archives",
        "py": "Scripts",
        "docx": "Documents",
        "txt": "Text_files"
    }
    
    for folder in file_types.values():
        folder_path = os.path.join(dirc, folder)
        if not os.path.exists(folder_path):
            folder_type = os.mkdir(folder_path)
            
    for file_name in os.listdir(dirc):
        file_cate = file_name.split('.')[-1].lower()
        if file_cate in file_types:
            new_folder = os.path.join(dirc, file_name)
            sub_folder = os.path.join(folder_type,file_name )
            shutil.move(new_folder,sub_folder)
    print('Done')


# In[ ]:




