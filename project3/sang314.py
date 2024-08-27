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

#Review:
'''
1. Handling Existing Files:
If a file with the same name already exists in the destination folder, shutil.move will raise an error. You might want to handle this by renaming the file or skipping it.
2. Empty Directory Check:
Consider checking if the source_dir is empty before starting the operation to save processing time.
3. Case Insensitivity:
Extensions are already being normalized to lowercase, which is good for handling case variations.
4. Edge Cases:
Ensure that symbolic links, hidden files, or system files are handled appropriately (if necessary).
5. Performance:
If you're dealing with a large number of files, you might want to look into more efficient file handling techniques, but for moderate use cases, your current approach should work well.
'''