import os, shutil
path = r'C:\Users\thuhang\Python Challenge\Project 3\\'
folder_names = ['Text File', 'Image File', 'Video File', 'Sound File', 'Document File', 'Compressed File' ]
for folder in folder_names:
    if not os.path.exists(path+folder):
        os.makedirs(path+folder)

file_names = os.listdir(path)
#move from path+file to path+'Compressed File\\'+file
# C:\Users\thuhang\Python Challenge\Project 3\
# path+file: C:\Users\thuhang\Python Challenge\Project 3\filemp3.mp3
for file in file_names:
    if '.csv' in file and not os.path.exists(path+'Text File\\'+file):
        shutil.move(path+file, path+'Text File\\'+file)
    elif '.jfif' in file and not os.path.exists(path+'Image File\\'+file):
        shutil.move(path+file, path+'Image File\\'+file)
    elif '.mp4' in file and not os.path.exists(path+'Video File\\'+file):
        shutil.move(path+file, path+'Video File\\'+file)
    elif '.mp3' in file and not os.path.exists(path+'Sound File\\'+file):
        shutil.move(path+file, path+'Sound File\\'+file)
    elif '.txt' in file and not os.path.exists(path+'Document File\\'+file):
        shutil.move(path+file, path+'Document File\\'+file)
    elif '.rar' in file and not os.path.exists(path+'Compressed File\\'+file):
        shutil.move(path+file, path+'Compressed File\\'+file)