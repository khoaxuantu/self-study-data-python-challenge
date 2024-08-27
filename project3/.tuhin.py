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

# Review:
'''
Use pathlib for Path Operations: Since you're already importing pathlib, you can use it to handle paths, which provides a more modern and intuitive interface compared to os.path.
Error Handling: Add error handling to manage cases where file operations might fail, such as permission issues or if the file is already in the destination folder.
And remember that out project would require you to sort files into different file types. E.g: Documents: .pdf, .txt; Audio: .mp3, .av
'''