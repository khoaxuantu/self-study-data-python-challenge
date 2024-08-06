import os
import shutil

def sort_files(source_dir, dest_dir):

  # Create destination folders if they don't exist
  file_types = {'images': ['.jpg', '.jpeg', '.png', '.gif'],
                'documents': ['.doc', '.docx', '.pdf', '.txt'],
                'videos': ['.mp4', '.avi', '.mov'],
                'audio': ['.mp3', '.wav', '.flac'],
                'others': []}  # For unknown file types

  for file_type, extensions in file_types.items():
    dest = os.path.join(dest_dir, file_type)
    os.makedirs(dest, exist_ok=True)

  # Iterate through files in the source directory
  for root, _, files in os.walk(source_dir):
    for file in files:
      source_file = os.path.join(root, file)
      file_extension = os.path.splitext(file)[1].lower()

      # Determine destination folder
      found = False
      for file_type, exts in file_types.items():
        if file_extension in exts:
          dest_folder = os.path.join(dest_dir, file_type)
          shutil.move(source_file, dest_folder)
          found = True
          break

      # If file type not found, move to others folder
      if not found:
        dest_folder = os.path.join(dest_dir, 'others')
        shutil.move(source_file, dest_folder)


# Run
source_directory = "path/..."
destination_directory = "path/..."
sort_files(source_directory, destination_directory)