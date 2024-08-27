import os
import shutil

def organize_files(source_dir):
    """Organizes files in the specified directory based on their extensions.

    Args:
        source_dir: The path to the source directory.
    """

    extension_folder_map = {
        ".doc": "Documents",
        ".docx": "Documents",
        ".pdf": "Documents",
        ".txt": "Text Files",
        ".py": "Python Scripts",
        ".jpg": "Images",
        ".png": "Images",
        ".mp3": "Audio",
        ".mp4": "Videos"
    }

    # Create destination folders upfront
    for folder_name in extension_folder_map.values():
        folder_path = os.path.join(source_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    for root, _, files in os.walk(source_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_name, extension = os.path.splitext(filename)
            extension = extension.lower()

            if extension in extension_folder_map:
                folder_name = extension_folder_map[extension]
                destination_folder = os.path.join(source_dir, folder_name)
                destination_file = os.path.join(destination_folder, filename)

                try:
                    shutil.move(file_path, destination_file)
                    print(f"Moved {filename} to {folder_name}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
            else:
                print(f"Skipping {filename} (unknown extension)")

# Example usage:
source_directory = r"C:\Users\trucdieu\PJ3"
organize_files(source_directory)


# Review:
# Areas to improve:

# File Extension Handling: Ensure that file extensions are consistently converted to lowercase to avoid issues with case sensitivity.
# Error Handling: The script handles errors during file movement, which is excellent. You might consider logging or handling specific exceptions for more detailed error analysis.