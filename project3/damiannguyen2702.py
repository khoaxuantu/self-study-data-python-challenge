import os, shutil

path = r"D:/Test proj 3/"

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

# Review:
'''
Avoid Repetitive Code: Instead of repeating the file type checks, use a dictionary to map extensions to folder names, making the code more concise and easier to maintain.
Generalize File Types: Consider normalizing the file extensions by converting them to lowercase to avoid missing files with uppercase extensions.
Efficiency: Instead of checking not os.path.exists before each move, you can move the file and handle any FileExistsError that might occur. This reduces the number of file system checks.
'''