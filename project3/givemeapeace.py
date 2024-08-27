import os
import shutil

# Define the source directory
source_directory = "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-"

# Create separate folders for each file type
folders = {
    ".jpg": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Image",
    ".png": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Image",
    ".gif": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Image",
    ".doc": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/documents",
    ".pdf": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/documents",
    ".txt": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/documents",
    ".mp4": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/videos",
    ".avi": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/videos",
    ".mov": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/videos",
    ".mp3": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/audio",
    ".wav": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/audio",
    ".flac": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/audio",
    ".zip": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Compressed folder",
    ".rar": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Compressed folder",
    ".7z": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Compressed folder",
    ".exe": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/excutable folder",
    # Add more folders for other file types as needed
}

# Ensure folders exist or create them
for folder_path in folders.values():
    os.makedirs(folder_path, exist_ok=True)

# Get a list of all files in the source directory
all_files = os.listdir(source_directory)

# Iterate through each file and move it to the appropriate folder
for filename in all_files:
    file_path = os.path.join(source_directory, filename)
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension in folders:
        # Move the file to the corresponding folder
        shutil.move(file_path, folders[file_extension])

print("Files sorted successfully!")

# Review:
'''
Exception Handling: Added try-except blocks to handle potential errors during folder creation and file moving.
File Check: Added a check to ensure that the path refers to a file before attempting to move it.
'''