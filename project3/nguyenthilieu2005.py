# importing required modules 
import os 
from shutil import move 
  
# making the directories
# Use another Username replacing 'admin' 
root_dir = "C:\\Users\\admin\\Downloads"
image_dir = "C:\\Users\\admin\\Downloads\\images"
documents_dir = "C:\\Users\\admin\\Downloads\\documents"
others_dir = "C:\\Users\\admin\\Downloads\\others"
software_dir = "C:\\Users\\admin\\Downloads\\software"
  
# files types of each category 
docs = ('.docx', '.doc',  '.txt', '.pdf', 
        '.xls', '.ppt', '.xlsx', '.pptx') 
images = ('.jpg', '.jpeg', '.png', '.svg', 
          '.tif', '.tiff', '.gif',) 
softwares = ('.exe', '.dmg', '.pkg') 
  
# appending all the files in the root directory to files[] 
files = [] 
for f in os.listdir(root_dir): 
  
    if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__): 
        files.append(f) 
  
  
# moving files to the respective folders, 
# overwriting if needed 
for file in files: 
    if file.endswith(docs): 
        move(file, documents_dir+"/"+file) 
  
    elif file.endswith(images): 
        move(file, image_dir+"/"+file) 
  
    elif file.endswith(softwares): 
        move(file, software_dir+"/"+file) 
  
    else: 
        move(file, others_dir+"/"+file) 
# Before running the script, change the directory to Downloads by typing 'cd Downloads' in the terminal.

# Review:
# Good job on completing this project:
# Here are some points you can look through to improve your code:
'''
File Path Issues: The script assumes the working directory is Downloads. However, in the os.listdir(root_dir) loop, it lists files without full paths. When moving files, it might fail unless the current working directory is set to Downloads. Consider using os.path.join(root_dir, f) to construct the full path.

Error Handling: Add error handling (e.g., using try-except) to manage potential issues like permission errors or non-existing files during the move operation.

Directory Creation: Before moving files, check if the destination directories (documents_dir, image_dir, etc.) exist, and create them if they don't using os.makedirs(destination_dir, exist_ok=True).

String Concatenation: When moving files, instead of using "+", use os.path.join() to construct paths, which makes the code more robust and platform-independent.

File Overwriting: The script currently overwrites files if a file with the same name exists in the destination directory. You might want to add a check to avoid overwriting or rename files if they already exist.
'''