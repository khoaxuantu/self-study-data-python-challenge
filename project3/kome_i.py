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




