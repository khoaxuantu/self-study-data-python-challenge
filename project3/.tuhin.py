import os
import shutil
from pathlib import Path

def get_extension(filename):
    return os.path.splitext(filename)[1][1:].lower()

def create_folder(directory, folder_name):
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def sort_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = get_extension(filename)
            if file_ext:
                destination_folder = create_folder(directory, file_ext)
                source_path = os.path.join(directory, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {destination_folder}")

def main():
    directory = input("Enter the directory path to sort: ")
    if os.path.isdir(directory):
        sort_files(directory)
        print("File sorting completed!")
    else:
        print("Invalid directory path. Please try again.")

if __name__ == "__main__":
    main()