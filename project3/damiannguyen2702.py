import os, shutil

path = r"C:/Users/Admin/Downloads/Jupyter Notebook/.ipynb_checkpoints/Project 3/"

file_name = os.listdir(path)

folder_names = ['images file','documents file','videos file','audio file','compressed file','executables file']

for loop in range(0,6):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".png" in file and not os.path.exists(path + "images file/" + file):
        shutil.move(path + file, path + "images file/" + file)
    elif ".txt" in file and not os.path.exists(path + "documents file/" + file):
        shutil.move(path + file, path + "documents file/" + file)
    elif ".mp4" in file and not os.path.exists(path + "videos file/" + file):
        shutil.move(path + file, path + "videos file/" + file)
    elif ".mp3" in file and not os.path.exists(path + "audio file/" + file):
        shutil.move(path + file, path + "audio file/" + file)
    elif ".zip" in file and not os.path.exists(path + "compressed file/" + file):
        shutil.move(path + file, path + "compressed file/" + file)
    elif ".py" in file and not os.path.exists(path + "executables file/" + file):
        shutil.move(path + file, path + "executables file/" + file)