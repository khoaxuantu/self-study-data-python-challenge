import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    file_name,extension = os.path.splitext(file)

    path_is_checked_exist = os.path.join(path,extension)

    if not os.path.exists(path_is_checked_exist):
        os.makedirs(path_is_checked_exist)
    
    path_of_file_moved = os.path.join(path,file)
    shutil.move(path_of_file_moved,os.path.join(path_is_checked_exist,file))

# Review:
'''
Handle Files Without Extensions: If a file has no extension, os.path.splitext(file) will return an empty string as the extension, which could result in creating a folder with no name. Consider adding a check to handle such cases.
Lowercase Extension Handling: To avoid creating multiple folders for the same extension (e.g., ".TXT" and ".txt"), you could convert the extension to lowercase.
Error Handling: Adding error handling, such as try-except blocks around the file operations, can make your script more robust in case of issues like file locks or permission errors.
And remember that out project would require you to sort files into different file types. E.g: Documents: .pdf, .txt; Audio: .mp3, .av
'''