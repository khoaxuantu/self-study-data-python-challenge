import os, shutil
path = r"G:/python/Project 3/"
file_name=os.listdir(path)
folder_names = ['videos','image files','documents','compressed files','audio files','executable files']
for loop in range(0,6):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path+folder_names[loop])
for file in file_name:
    if ".txt" in file and not os.path.exists(path + "documents/" + file):
        shutil.move(path + file, path + "documents/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".mp4" in file and not os.path.exists(path + "videos/" + file):
        shutil.move(path + file, path + "videos/" + file)
    elif ".zip" in file and not os.path.exists(path + "compressed files/" + file):
        shutil.move(path + file, path + "compressed files/" + file)
    elif ".mp3" in file and not os.path.exists(path + "audio files/" + file):
        shutil.move(path + file, path + "audio files/" + file)
    elif ".exe" in file and not os.path.exists(path + "executable files/" + file):
        shutil.move(path + file, path + "executable files/" + file)

        
print("All files have been successfully moved.")