import os
import shutil

directory = input("Please paste your directory path here! ")

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".csv", ".tsv", ".pdf", ".doc", ".docx", ".txt"],
    "videos": [".mp4", ".mov", ".avi"],
    "compressed": [".zip", ".rar", ".tar", ".gz"],
    "audio": [".mp3", ".wav", ".aac"],
    "executables": [".exe", ".bat", ".sh"]
}

for folder in file_types.keys():
    folder_path = os.path.join(directory,folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def get_file_type(tail):
    for file_type, tails in file_types.items():
        if tail.lower() in tails:
            return file_type
    return "others"

for file_name in os.listdir(directory):
    if os.path.isdir(os.path.join(directory,file_name)):
        continue
        
    _,tail = os.path.splitext(file_name)
    
    file_type = get_file_type(tail)
    file_path = os.path.join(directory,file_name)
    if file_type:
        dest_path = os.path.join(directory,file_type,file_name)
        shutil.move(file_path,dest_path)

# Review:
# Here are some ponits you can consider to improve your code:
'''
Handling Unrecognized File Types: The get_file_type function returns "others" for unrecognized file types, but the code doesn't create or move files to an "others" directory. Consider adding this functionality to handle miscellaneous files.
Error Handling: Adding error handling (e.g., try-except blocks) can help manage issues like permission errors or files already existing in the destination folder.
Case Sensitivity: You're already using tail.lower() to handle case sensitivity, which is great. Just ensure that the extension list (file_types) is comprehensive to avoid missing any files.
'''
