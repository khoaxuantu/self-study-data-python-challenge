import os
import shutil

def organize_files(source_dir):
    folder_names = {
        '.jpg': 'images',
        '.png': 'images',
        '.docx': 'documents',
        '.pdf': 'documents',
        '.mp4': 'videos',
        '.txt': 'text_files',
    }

    for folder_name in folder_names.values():
        os.makedirs(folder_name, exist_ok=True)

    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            if ext in folder_names:
                target_folder = folder_names[ext]
                shutil.move(os.path.join(source_dir, filename), os.path.join(target_folder, filename))

if __name__ == '__main__':
    source_directory = 'C:/Users/Admin/Documents/pro3'
    organize_files(source_directory)
    print("Files organized successfully!")
