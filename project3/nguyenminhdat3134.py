import os
import shutil

# Define the file extensions for each category with a dictionary
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Compressed Files": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Audio Files": [".mp3", ".wav", ".aac", ".flac"],
    "Executable Files": [".exe", ".bat", ".sh"],
    "Data Files": [".csv", ".tsv"]
}

# Create the folder for each category
def Create_Folder(direct_path):
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(direct_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

#Organizing the file to each folder with same category
def organize_files(direct_path):
    for filename in os.listdir(direct_path):
        file_path = os.path.join(direct_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    dest_folder = os.path.join(direct_path, category)
                    shutil.move(file_path, dest_folder)
                    moved = True
                    break
            if not moved:
                print(f"File {filename} does not match any category")

if __name__ == "__main__":
    direct_path = input("Enter the path of the directory to organize: ")
    Create_Folder(direct_path)
    organize_files(direct_path)
    print("Files have been organized.")
