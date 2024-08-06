import os, shutil

path = input("Enter the path: ")
files=os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)
    target_folder = os.path.join(path, extension[1:])
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    shutil.move(os.path.join(path, file), os.path.join(target_folder, file))
