import os, shutil
path= r"C:/Users/HP/PYTHON_PRJ3/"
file_name = os.listdir(path)
folder_names = ['CSV files', 'Video files', 'Images PNG',
                'Executable files', 'Compressed files', 'Audio files']
for loop in range(0, 6):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))
for file in file_name:
    if '.csv' in file and not os.path.exists(path + 'CSV files/' + file):
        shutil.move(path + file, path + 'CSV files/' + file)
    elif '.mp4' in file and not os.path.exists(path + 'Video files/' + file):
        shutil.move(path + file, path + 'Video files/' + file)
    elif '.png' in file and not os.path.exists(path + 'Images PNG/' + file):
        shutil.move(path + file, path + 'Images PNG/' + file)
    elif '.exe' in file and not os.path.exists(path + 'Executable files/' + file):
        shutil.move(path + file, path + 'Executable files/' + file)
    elif '.rar' in file and not os.path.exists(path + 'Compressed files/' + file):
        shutil.move(path + file, path + 'Compressed files/' + file)
    elif '.mp3' in file and not os.path.exists(path + 'Audio files/' + file):
        shutil.move(path + file, path + 'Audio files/' + file)

# You've done well by organizing files into separate folders and ensuring no duplicate moves are made. The code is concise and gets the job done.
# Areas to improve:
# The code currently handles six file types, which is great for maximum bonus points. However, it would be beneficial to consider a more flexible method for handling additional file types.