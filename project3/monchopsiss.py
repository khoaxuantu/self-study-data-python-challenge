import os
import shutil

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def get_file_type(extension):
    for file_type, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return file_type
    return 'Others'

def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            file_type = get_file_type(extension)
            target_dir = os.path.join(directory, file_type)

            if not os.path.isdir(target_dir):
                os.mkdir(target_dir)

            shutil.move(file_path, target_dir)
            print(f"Moved {filename} to {file_type}/")

if __name__ == "__main__":
    directory = input("Enter the path to the folder to sort:")
    organize_files(directory)
    print("Complete file sorting.")
