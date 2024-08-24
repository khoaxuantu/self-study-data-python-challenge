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