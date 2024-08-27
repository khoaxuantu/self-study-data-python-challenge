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

# Review:
'''
Expand Folder Mapping: Consider adding more file types to the folder_names dictionary to handle a wider variety of files.
Handle Unmapped Extensions: If a file's extension isn't in folder_names, you could add it to an "Others" folder, ensuring that no files are left unorganized.
Error Handling: Implement error handling to manage any potential issues (e.g., permission errors) that might occur during file operations.
Print Feedback: Add feedback for files that are moved, so the user knows exactly what is being organized.
'''
