import os
import shutil

file_types = {
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images',
    '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
    '.mp4': 'Videos', '.avi': 'Videos', '.mov': 'Videos',
    '.mp3': 'Audio', '.wav': 'Audio',
    '.zip': 'Compressed', '.rar': 'Compressed', '.7z': 'Compressed',
    '.exe': 'Executables', '.bat': 'Executables'
}

def organize_files(source_dir):
    for filename in os.listdir(source_dir):
        extension = os.path.splitext(filename)[1].lower()
        if extension in file_types:
            destination_dir = os.path.join(source_dir, file_types[extension])
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))
    print("Files organized successfully!")

while True:
    source_dir = input(r"Directory path you want to organize: ")
    if os.path.isdir(source_dir):
        organize_files(source_dir)
        break
    else:
        print("ERROR! Invalid directory path.")

# Review:
'''
Error Handling: Add error handling for potential issues during file operations, such as permission errors or files that already exist in the destination folder.
Edge Cases: Consider handling files without extensions or with uncommon extensions not listed in file_types.
User Experience: Enhance the user experience by allowing the program to retry if the directory path is invalid, instead of exiting the loop.
Code Efficiency: The code could be more efficient by checking if the destination folder exists outside the loop, reducing redundant os.path.exists() and os.makedirs() calls.
'''