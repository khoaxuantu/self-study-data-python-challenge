import os
import sys

print ('This program will create 6 folders to store relevant files (.txt, .csv, .jpg, .mp3, .mp4, .zip)')
print (
""".txt files represent Text files.
.jpg files represent Image files.
.csv files represent Comma-Separated Values files
.mp3 files represent Audio files.
.mp4 files represent Video files.
.zip files represent Compressed files.
""")

# Create 6 folders to store 6 types of files
try:
    where = input('Enter the path where you want to create folder: ')
    name_of_folder = str(input('Enter the folder name containning those 6 folders: '))
    parent_folder = os.path.join(where.strip(), name_of_folder.strip())
    child_folders = ['Document', 'Image', 'Comma-Separated Values', 'Audio', 'Video', 'Compressed']
    
    # Create parent folder if it doesn't exist
    os.makedirs(parent_folder, exist_ok = False)  # Create parent folder and its subfolders if not exist
    
     # Create child folders
    for child_folder in child_folders:
        folder_path = os.path.join(parent_folder, child_folder)
        os.makedirs(folder_path)
    
    print(f"Folders created successfully in {parent_folder}\n")

        
except Exception as e:
    print (f"Error: {e}")
    sys.exit()  # Exit the program if the folder already exists

    
folder_file = {'Document': '.txt', 
               'Image': '.jpg', 
               'Comma-Separated Values': '.csv', 
               'Audio': '.mp3', 
               'Video': '.mp4', 
               'Compressed': '.zip'}

def get_key(dic, target_extension): # Get the key from the dictionary based on the value.
    for key, value in dic.items():
        if value == target_extension:
            return key
    return None
        
while True:
    try:
        print ('Note: Enter "exit" when you do not want to add any files to appropriate folder!')
        file_name_with_extension = str(input('Enter the name of the file with an extension (ex: code.txt, girlfriend.jpg, etc.): '))   
        
        if file_name_with_extension.lower().strip() == 'exit':
            break
        
        name_file, target_extension = os.path.splitext(file_name_with_extension)
        folder_key = get_key(folder_file, target_extension)
        
        if folder_key:
            create_file_to_folder = os.path.join(parent_folder, folder_key.strip(), file_name_with_extension)
            try:
                with open (create_file_to_folder, 'x') as f:
                    pass
                print (f"\nFile '{file_name_with_extension}' created in {folder_key} folder.\n")
            except FileExistsError:
                 print('\nError: The file already exists. Please try again!\n')
        else:
            print(f"\nNo corresponding folder found for the extension '{target_extension}'.\n")
            
    except Exception as er:
        print (f"\nError: {er}. Please try again!\n")

# Review:
'''
0. In this project, you did create a sorting files script. However, we want you to sort a folder with given files into seperated folders with each a different file types.
Therefore, we have to minus you 1 points for not aligning with the projects requiremnt. Sorry for that. Here are other things you can improve your code:
1. Extension Mapping:
The folder_file dictionary is static, which is fine, but you could consider allowing the user to define additional file types and their corresponding folders dynamically, making the script more flexible.
Also, to handle extensions more robustly, you can store extensions in lowercase and use .lower() when comparing them to avoid case sensitivity issues.
2. Error Handling:
Improve error handling for cases where the user might input invalid paths, non-existent directories, or unsupported file types. Consider adding custom error messages or even try-except blocks around critical sections of the code.
'''

        
    

    


