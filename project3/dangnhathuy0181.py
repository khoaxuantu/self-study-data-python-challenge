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

# Review:
'''
Handle Files Without Extensions: Ensure the code can manage files without extensions by adding a condition to check for file_tail. In other sense, our project require you to sort files into different file types. E.g: Documents: .pdf, .txt; Audio: .mp3, .av
Avoid Conflicts with Existing Folders: If a folder already exists with a similar name, there might be conflicts. Consider adding a prefix like _ or sorted_ to avoid naming collisions.
Case Sensitivity: Normalize the extension to lowercase (file_tail.lower()) to avoid case-sensitivity issues.
'''