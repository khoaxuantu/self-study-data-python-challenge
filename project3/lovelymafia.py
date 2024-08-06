import os
import shutil

def organize_files_by_extension(source_folder):
    # Create a dictionary to store the extensions and their corresponding folders
    extensions_folders = {}
    
    # List all files in the source folder
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            # Get the file extension
            file_ext = filename.split('.')[-1]
            
            # Define the destination folder based on the file extension
            dest_folder = os.path.join(source_folder, file_ext.upper() + "_Files")
            
            # Create the folder if it doesn't exist
            if dest_folder not in extensions_folders:
                os.makedirs(dest_folder, exist_ok=True)
                extensions_folders[file_ext] = dest_folder
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_folder, filename), os.path.join(dest_folder, filename))

    print("Files have been organized.")

# Define the source folder
source_folder = 'Project 3'

# Organize the files
organize_files_by_extension(source_folder)
