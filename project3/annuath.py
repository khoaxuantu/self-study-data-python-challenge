import os
import shutil

def organize_files():
    # Get the directory of the current script
    source_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the target directories for different file types
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt','.csv','.tsv'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Compressed': ['.zip', '.rar'],
        'Audio': ['.mp3', '.wav'],
        'Executables': ['.exe', '.bat']
    }

    # Create target directories if they don't exist
    for folder in folders:
        os.makedirs(os.path.join(source_dir, folder), exist_ok=True)

    # Move files to their respective folders
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(source_dir, folder, file_name))
                    break

if __name__ == "__main__":
    organize_files()
