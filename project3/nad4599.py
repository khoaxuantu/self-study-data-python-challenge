import os
import shutil

# Define the source directory
source_dir = "./project34"
# Check if the source directory exists
if not os.path.exists(source_dir):
    print(f"Error: The source directory '{source_dir}' does not exist.")
else:
    # Define the file extensions for each file type
    file_types = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "documents": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
            ".tsv",
            ".csv",
        ],
        "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "compressed": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "executables": [".exe", ".bat", ".sh", ".bin"],
    }


# Function to get the file type based on extension
def get_file_type(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for file_type, extensions in file_types.items():
        if ext in extensions:
            return file_type
    return None


# Iterate over files in the source directory and move them to the appropriate target directory
for file_name in os.listdir(source_dir):
    source_file = os.path.join(source_dir, file_name)
    if os.path.isfile(source_file):
        file_type = get_file_type(file_name)
        if file_type:
            target_dir = os.path.join(source_dir, file_type)
            os.makedirs(target_dir, exist_ok=True)
            target_file = os.path.join(target_dir, file_name)
            shutil.move(source_file, target_file)
            print(f"Moved {file_name} to {target_dir}")

print("File sorting completed.")
