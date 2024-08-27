#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil


# In[3]:


path = os.getcwd()


# In[7]:


if not os.path.exists(path + r"\animal"):
    os.mkdir(path + r"\animal")


# In[8]:


if not os.path.exists(path + r"\animal\cat"):
    os.mkdir(path + r"\animal\cat")


# In[9]:


if not os.path.exists(path + r"\animal\dog"):
    os.mkdir(path + r"\animal\dog")


# In[10]:


if not os.path.exists(path + r"\text"):
    os.mkdir(path + r"\text")


# In[11]:


if not os.path.exists(path + r"\text\written"):
    os.mkdir(path + r"\text\written")


# In[12]:


if not os.path.exists(path + r"\text\empty"):
    os.mkdir(path + r"\text\empty")


# In[13]:


if not os.path.exists(path + r"\text\written\csv"):
    os.mkdir(path + r"\text\written\csv")


# In[14]:


if not os.path.exists(path + r"\text\written\txt"):
    os.mkdir(path + r"\text\written\txt")


# In[15]:


if not os.path.exists(path + r"\text\written\tsv"):
    os.mkdir(path + r"\text\written\tsv")


# In[16]:


shutil.move(path + r"\Rosie.png", path + r"\animal\dog")


# In[17]:


shutil.move(path + r"\Max.png", path + r"\animal\dog")


# In[18]:


shutil.move(path + r"\angrycat.jpg", path + r"\animal\cat")


# In[19]:


shutil.move(path + r"\CSVFile.csv", path + r"\text\written\csv")


# In[20]:


shutil.move(path + r"\NewFile.txt", path + r"\text\written\txt")


# In[21]:


shutil.move(path + r"\FakeFile.txt", path + r"\text\written\txt")


# In[22]:


shutil.move(path + r"\NewFile.tsv", path + r"\text\written\tsv")


# In[23]:


shutil.move(path + r"\FakeFile.csv", path + r"\text\empty")

 
# In[ ]:

# Review:
# Here are some points you may consider to improve your code next time:
'''
Next project, consider making them parameters or reading them from a configuration file. This will increase flexibility and reduce the need to modify the code directly.
You use path + r"\folder" to construct paths. It's better to use os.path.join() to create paths as it ensures compatibility across different operating systems (e.g., Windows vs. Unix-based).
Add error handling to manage cases where the file to be moved doesn't exist or when there are permission issues. This will make your script more robust.
Instead of manually creating directories for each category, consider defining a structure in a dictionary and using a loop to create directories. This approach reduces redundancy and makes it easier to adjust the folder structure in the future.
'''


