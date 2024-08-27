
import os
import shutil

def organize_files(directory):
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.pdf','.doc', '.docx', '.txt', '.xlsx', 'xls','.ppt','.pptx','.csv','.tsv'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'compressed': ['.zip', '.rar', '.tar', '.gz'],
        'audio': ['.mp3', '.wav', '.aac'],
        'executables': ['.exe', '.bat', '.sh']
    }

    for folder, extensions in file_types.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) and any(filename.endswith(ext) for ext in extensions):
                shutil.move(file_path, folder_path)


### Replace 'Project directory with an actual directory"
directory = 'Project directory'
organize_files(directory)
print("File organization complete.")

# Review:
# Good job on completing this project:
'''
Add error handling for cases where a file cannot be moved (e.g., due to permissions issues or the file being in use). This would make the script more robust.
Catch-All Folder: If a file does not match any predefined category, it is currently placed in a folder named after its extension. While this is a functional approach, creating a dedicated "Uncategorized" or "Others" folder might provide a clearer structure.
'''