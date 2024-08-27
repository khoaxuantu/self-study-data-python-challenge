import os
import shutil

    # Choose file types:
extensions_to_folders = {
    '.txt': 'TextFiles',
    '.png': 'Images',
    '.pdf': 'PDFs',
    '.docx': 'Documents',
    '.xlsx': 'Excel Sheets',
    '.pbix': 'Power BI'}

def organize_files(source_folder, target_folder):
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()  # Normalize extension to lowercase
            if ext in extensions_to_folders:
                target_subfolder = os.path.join(target_folder, extensions_to_folders[ext])
                os.makedirs(target_subfolder, exist_ok=True)
                shutil.move(os.path.join(source_folder, filename), os.path.join(target_subfolder, filename))

# Choose source_folder & target folder:
target_folder = 'D:/Learning/Data Science Practice/Materials'
source_folder = 'C:/Users/Dell Latitude E7390/OneDrive/Desktop/Data Materials/Sources'

organize_files(source_folder, target_folder)
print('Successfully organized!')

# Review:

# Error Handling: Consider adding error handling for cases where files might be in use or permissions issues arise during the move operation. This will make your script more robust and user-friendly.
# Path Concatenation: Ensure that the paths provided (e.g., target_folder, source_folder) are valid and accessible, as this is crucial for the script to run successfully. Testing the script with various paths could help catch potential issues.