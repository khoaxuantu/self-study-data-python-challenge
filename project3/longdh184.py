import os
import shutil

def organize_files_by_type(directory):
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Get the file extension
        _, ext = os.path.splitext(filename)
        # Skip if it's not a file (e.g., it's a directory)
        if not ext:
            continue
        # Remove the dot from the extension
        ext = ext.lstrip('.')
        # Create a subfolder name based on the file extension
        subfolder = os.path.join(directory, ext)
        # Ensure the subfolder exists, create it if it doesn't
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        # Construct full file path
        source_file = os.path.join(directory, filename)
        destination_file = os.path.join(subfolder, filename)
        # Move the file to the subfolder
        shutil.move(source_file, destination_file)
        print(f"Moved: {source_file} to {destination_file}")

if __name__ == "__main__":
    # Call the function to organize files by type
    directory = input('Input source folder path: ')
    organize_files_by_type(directory)
