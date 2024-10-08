#!/usr/bin/env python
# coding: utf-8

# # Tự động phân loại các loại tệp: .jpg, .doc, .xlsx, .mp4, .zip

# In[7]:


import os
import shutil


# In[9]:


path = r"C:\\Users\\Administrator\\Desktop\\Phân loại tệp\\"


# In[13]:


file_name = os.listdir(path)

#Tạo thư mục cho từng loại tệp
folder_names = ['JPG Files', 'Doc Files', 'Excel Files', 'MP4 Files', 'Zipped Files']

for loop in range(0,5):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])


# In[15]:


#Phân loại các tệp vào đúng thư mục dựa vào tên đuôi
for file in file_name:
    if ".jpg" in file and not os.path.exists(path + "JPG Files\\" + file):
        shutil.move(path + file, path + "JPG Files\\" + file)
    elif ".doc" in file and not os.path.exists(path + "Doc Files\\" + file):
        shutil.move(path + file, path + "Doc Files\\" + file)
    elif ".xlsx" in file and not os.path.exists(path + "Excel Files\\" + file):
        shutil.move(path + file, path + "Excel Files\\" + file)
    elif ".mp4" in file and not os.path.exists(path + "MP4 Files\\" + file):
        shutil.move(path + file, path + "MP4 Files\\" + file)
    elif ".zip" in file and not os.path.exists(path + "Zipped Files\\" + file):
        shutil.move(path + file, path + "Zipped Files\\" + file)

# Areas to improve:

# Path Concatenation: Using os.path.join for path concatenation is recommended for better cross-platform compatibility and readability. Replace manual concatenation (e.g., path + "JPG Files\\" + file) with os.path.join(path, "JPG Files", file).
# File Extension Handling: The script checks for substrings like .jpg in filenames, which might not correctly handle files with extensions like .jpeg or .docx. Consider using os.path.splitext to accurately extract and match file extensions.
# Error Handling: Adding error handling would make the script more robust. For example, handle cases where moving files might fail due to permissions or other issues.
# In[ ]:




