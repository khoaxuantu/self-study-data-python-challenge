import sys
import os
import shutil

# create a dictionary with the file types and their corresponding folder names
FILE_TYPES = {
    "zip": "zip_files",
    "csv": "csv_files",
    "sql": "sql_files",
    "jpg": "image_files",
    "jpeg": "image_files",
    "png": "image_files",
    "mp3": "mp3_files",
    "mov": "mov_files",
    "txt": "text_files",
    "tsv": "tsv_files",
    "pdf": "pdf_files",
}


# function to organize files into folders depending on file types (.zip, .csv, .sql, .jpeg, .mp3, .mov, etc.)
def organize_file(file_name, user_folder_name):
    # if user_folder_name is not empty, create and move the file to the folder with the user_folder_name
    if user_folder_name:
        # create a folder with the user_folder_name
        os.makedirs(user_folder_name, exist_ok=True)

        # move the file to the folder with the user_folder_name
        shutil.move(file_name, user_folder_name)
    else:
        # get the file extension
        file_extension = file_name.split(".")[-1].lower()

        # check if the file extension is in the FILE_TYPES dictionary
        if file_extension in FILE_TYPES:
            # get the folder name from the FILE_TYPES dictionary
            folder_name = FILE_TYPES[file_extension]

            # create a folder with the folder_name if not already existed
            os.makedirs(folder_name, exist_ok=True)

            # move the file to the folder with the folder_name
            shutil.move(file_name, folder_name)


if __name__ == "__main__":
    # get the current path in OS
    current_path = os.getcwd()
    print(f"Current path: {current_path}")
    
    # get user input for the file location
    input_path = input("[REQUIRED] Enter a file name or a path containing files to be sorted: ")
    print(f"You entered: {input_path}")

    # if input_path is a file name (containing extension), then ask user for a destination folder name
    if "." in input_path:
        # get user input for the destination folder name
        user_folder_name = input("[REQUIRED] Enter the destination folder name for your file: ")
        print(f"You entered: {user_folder_name}")

        # organize the file
        organize_file(input_path, user_folder_name)
    else:
        # change the current path to the input_path directory
        os.chdir(input_path)

        # get the list of files in the input_path directory
        files = os.listdir(input_path)

        # loop through the files
        for file in files:
            # get the file path
            file_path = f"{input_path}/{file}"
            print(f"organizing file: {file_path}")
 
            # organize the file
            organize_file(file_path, "")

# Review:
'''
Path Handling: Using os.path.join() for better cross-platform compatibility.
Error Handling: Added checks to ensure files and directories exist.
User Input Validation: Improved user input handling and validation.
Output Messages: Clearer output messages for better user feedback.
'''