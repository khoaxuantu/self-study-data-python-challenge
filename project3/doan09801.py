# -*- coding: utf-8 -*-
"""Project3_doan09801.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16tx5t1X1SLGDkTVHAJV_Q6jN6rlj3Bus
"""

import os
import shutil

path = '/Users/donlancy/Library/CloudStorage/OneDrive-Personal/Project_3'

list_ = os.listdir(path)

for file_ in list_:
	name, ext = os.path.splitext(file_)

	ext = ext[1:]

	if ext == '':
		continue

	if os.path.exists(path+'/'+ext):
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
	else:
		os.makedirs(path+'/'+ext)
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)