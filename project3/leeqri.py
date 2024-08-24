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
