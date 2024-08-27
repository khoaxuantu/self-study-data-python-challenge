
import os
import shutil
from pathlib import Path

def organize_files(source_dir):
    # Create destination folders
    folders = {
        'Documents': ['.txt', '.doc', '.docx', '.pdf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Others': []
    }
    
    for folder in folders:
        Path(os.path.join(source_dir, folder)).mkdir(exist_ok=True)
    
    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Determine the destination folder
            dest_folder = 'Others'
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    dest_folder = folder
                    break
            
            # Move the file
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(source_dir, dest_folder, filename)
            shutil.move(source_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")

# Usage
source_directory = '/path/to/your/directory'
organize_files(source_directory)

#Review:
'''
Here are some points you can improve your code:
- Pathlib Usage: Since you imported Path from the pathlib module, you might consider using it more extensively throughout the script for consistency.
- Handling Name Conflicts: If a file with the same name already exists in the destination folder, the current script will overwrite it. You might want to handle such conflicts by renaming the file or skipping it.
- Error Handling: While the script is robust, adding some basic error handling (e.g., try-except blocks) could make it more resilient, especially when dealing with file operations that might fail.
'''