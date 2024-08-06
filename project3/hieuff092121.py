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
