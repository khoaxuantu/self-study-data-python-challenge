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

# Review:
# Here are some points you can consider to improve your code:
'''
Be aware that our project is to sort to different file types based on the extension. E.g: Documents (.doc, .pdf), Audio (.mp3), etc
If a file with the same name already exists in the destination folder, shutil.move will raise an error. Consider handling such conflicts by renaming the file or skipping it.
Consider adding a check for files without an extension. You can move these files into a folder named No_Extension_Files or something similar.
Rather than splitting the filename by '.', consider using os.path.splitext() to get the extension. This method is more reliable, especially for files with multiple dots in their names.
'''
