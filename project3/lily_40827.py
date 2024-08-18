#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sort images, document, video, folders (1)
# compressed files,audio video files, and executable files (3)


# In[2]:


#create folder project 3
import os
if not os.path.exists('Challenge_Project_3'):
    os.mkdir('Challenge_Project_3')


# In[3]:


#create a folder document and input doc files into folder
if not os.path.exists('Challenge_Project_3\Document'):
    os.mkdir('Challenge_Project_3\Document')


# In[4]:


with open(r'Challenge_Project_3\Document\NewFile.doc','w') as doc_file:
    doc_file.write("This is the first file document")


# In[5]:


#create a folder csv and input csv into folder
if not os.path.exists('Challenge_Project_3\CSVFILE'):
    os.mkdir('Challenge_Project_3\CSVFILE')


# In[6]:


import csv
column_name=['Name', 'Age', 'City']
data=[['Alice', '30', 'New York'],['Bob', '25', 'Los Angeles'],['Charlie', '35', 'Chicago']]
with open(r'Challenge_Project_3\CSVFILE\Excel_file_1.csv','w',newline='') as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(column_name)
    csv_writer.writerows(data)


# In[7]:


#create a folder images and input images into folder
if not os.path.exists('Challenge_Project_3\Image'):
    os.mkdir('Challenge_Project_3\Image')


# In[8]:


#types of file: 'jpg','jpeg','png','gif'
#you can use the requests library to fetch the image and then write it to a file
import requests
#URL of the image
image_url='https://khoinguonsangtao.vn/wp-content/uploads/2022/08/hinh-anh-meo-cute-doi-mat-to-tron-den-lay-de-thuong.jpg'
#Fetch the image to the local file
response=requests.get(image_url)
with open(r'Challenge_Project_3\Image\cat.jpg','wb') as image:
    image.write(response.content)
print("Image has been downloaded and saved.")


# In[9]:


#Using urllib module to download an image from a url and save it to a local directory
import urllib.request
image_url='https://sharedigital.vn/storage/2022/11/HH-T11.235.png'
image_path=r'Challenge_Project_3\Image\cat2.png'
urllib.request.urlretrieve(image_url,image_path)


# In[10]:


#create a folder video and input video into folder
if not os.path.exists('Challenge_Project_3\Video'):
    os.mkdir('Challenge_Project_3\Video')


# In[18]:


#'.mp4', '.wav', '.aac', '.flac', '.ogg'
video_url='https://www.youtube.com/watch?v=bkpLhQd6YQM&ab_channel=CoreySchafer'
video_path=r'Challenge_Project_3\Video\videofile.mp4'
response=requests.get(video_url)
with open(video_path,'wb') as file:
    file.write(response.content)


# In[12]:


#create a folder audio and input audio file into this folder
if not os.path.exists('Challenge_Project_3\Audio'):
    os.mkdir('Challenge_Project_3\Audio')


# In[13]:


import requests
audio_url='https://open.spotify.com/track/1on6FVFhfZL9NAuXc5moU3'
audio_path=r'Challenge_Project_3\Audio\audio.mp3'
response=requests.get(audio_url)
with open(audio_path,'wb') as file:
    file.write(response.content)


# In[14]:


#create a folder compressed files and input compressed files into folder
if not os.path.exists('Challenge_Project_3\Compressed_files'):
    os.mkdir('Challenge_Project_3\Compressed_files')


# In[15]:


#'.zip', '.rar', '.tar', '.gz', '.7z'

zip_url='https://drive.google.com/drive/folders/1StlwIEQZH9HQ5_cdTaU3hS1EXchzi0MP'
zip_path=r'Challenge_Project_3\Compressed_files\file_1.zip'
response=requests.get(zip_url)
with open(zip_path,'wb') as file:
    file.write(response.content)


# In[16]:


#create a folder executable files and input executable files into folder
if not os.path.exists('Challenge_Project_3\Executables'):
    os.mkdir('Challenge_Project_3\Excecutables')


# In[17]:


# .exe', '.msi', '.bat', '.sh'
exe_url='https://drive.google.com/drive/folders/1StlwIEQZH9HQ5_cdTaU3hS1EXchzi0MP'
exe_path=r'Challenge_Project_3\Executables\file_2.exe'
os.makedirs(os.path.dirname(exe_path), exist_ok=True)
response=requests.get(exe_url)
with open(exe_path,'wb') as file:
    file.write(response.content)

