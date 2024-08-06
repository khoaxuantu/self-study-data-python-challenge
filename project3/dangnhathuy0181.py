import os, shutil
folder_path = input('Enter folder for sorting: ')
os.chdir(folder_path)

for file in os.listdir(folder_path):
    old_path = os.path.join(folder_path, file)
    file_tail = file.split('.')[-1]
    if not os.path.exists(f'{file_tail} folder'):
        os.makedirs(f'{file_tail} folder')
    new_folder = f'{file_tail} folder'
    
    new_path = os.path.join(folder_path, new_folder)
    shutil.move( old_path , new_path)
print("Sorting process is done, reload your folder to check")
