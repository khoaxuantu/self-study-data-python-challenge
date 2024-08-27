import os, shutil
path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("\\","/") + '/'
files = os.listdir(path)
list_files = [f for f in files if os.path.isfile(os.path.join(path, f))]
list_folder = [f for f in files if os.path.isdir(os.path.join(path, f))]
for file_name in list_files:
    tmp = file_name.split('.')[1] + ' files'
    if tmp in list_folder :
        if not os.path.exists(path + tmp + file_name):
            shutil.move(path + file_name, path + tmp +'/' + file_name)
        else:
            continue
    else:
        os.mkdir(path+tmp)
        shutil.move(path + file_name, path + tmp + '/' + file_name)
        list_folder.append(tmp)
#Review:
#There are quite a few things you may want to consider for your code:
'''
If a file doesn't have an extension, file_name.split('.')[1] will raise an IndexError. Consider handling files without extensions more gracefully.
Instead of manually splitting the filename, you could use os.path.splitext to separate the name and extension. This is more reliable and handles filenames with multiple dots correctly.
Your code replaces \\ with / to ensure paths are consistent. However, you can directly use os.path.join() and avoid the need for manual path separators.
Your code checks if a file exists before moving it, but it only checks in one destination folder. If you want to avoid overwriting files with the same name, you could add a counter or timestamp to the filename.
'''