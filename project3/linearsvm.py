import os
import shutil
import tkinter as tk
from tkinter import filedialog

file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv', '.tsv'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv'],
    'compressed': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'audio': ['.mp3', '.wav', '.aac', '.flac'],
    'executables': ['.exe', '.bat', '.sh'],
}

def browse_directory(title):
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title=title)
    return directory

def sort_files(source_dir, destination_dirs, file_types):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            for file_type, extensions in file_types.items():
                if file_ext in extensions:
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(destination_dirs[file_type], file)
                    shutil.move(source_path, destination_path)
                    print(f'Moved: {file} to {destination_dirs[file_type]}')
                    break

def main():
    # Get source and destination directories from user
    source_dir = browse_directory("Select Source Directory")
    if not source_dir:
        print("No source directory selected. Exiting.")
        return
    
    base_dest_dir = browse_directory("Select Base Destination Directory")
    if not base_dest_dir:
        print("No destination directory selected. Exiting.")
        return
    
    # Define destination directories based on user input
    destination_dirs = {
        'images': os.path.join(base_dest_dir, 'images'),
        'documents': os.path.join(base_dest_dir, 'documents'),
        'videos': os.path.join(base_dest_dir, 'videos'),
        'compressed': os.path.join(base_dest_dir, 'compressed'),
        'audio': os.path.join(base_dest_dir, 'audio'),
        'executables': os.path.join(base_dest_dir, 'executables'),
    }
    
    # Create destination directories if they don't exist
    for dir_path in destination_dirs.values():
        os.makedirs(dir_path, exist_ok=True)
    
    # Sort the files
    sort_files(source_dir, destination_dirs, file_types)

if __name__ == "__main__":
    main()

# Review:
# You overkill this project; only one thing you may want to consider: Wrapped the shutil.move operation in a try-except block to catch any errors during file moves.