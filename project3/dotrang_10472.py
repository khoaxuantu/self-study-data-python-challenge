import os
import shutil

source_dir = '/Users/dotrang/DA_CODE_PYTHON/Project_3/all_files'
destination_dir = '/Users/dotrang/DA_CODE_PYTHON/Project_3/all_files/destination_directory'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav', '.wav'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe', '.msi', '.bat']
}

for folder in file_types.keys():
    os.makedirs(os.path.join(destination_dir, folder), exist_ok=True)

for filename in os.listdir(source_dir):
    file_extension = os.path.splitext(filename)[1].lower()
    moved = False

    for folder, extensions in file_types.items():
        if file_extension in extensions:
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, folder, filename))
            moved = True
            break

    if not moved:
        print(f"File {filename} cannot be moved because it is not of the defined type.")

print("Complete file arrangement.")

# Review:
'''
Avoid Duplicate Extensions: In the file_types dictionary, the 'Audio' key has '.wav' listed twice. Consider removing the duplicate to ensure consistency.
Handle Non-Movable Files: When a file does not match any defined type, instead of just printing a message, you could create an "Others" folder in the destination directory and move unmatched files there.
Add error handling around the shutil.move operation to catch and report issues such as permission errors or if a file is already in use.
'''