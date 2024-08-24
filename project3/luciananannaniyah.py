import os
import shutil

FILE_TYPES = {
  'Images': ['jpg', 'jpeg', 'png'],
  'Videos': ['mp4', 'mov'],
  'Documents': ['pdf', 'txt', 'docx'],
  'Audio': ['mp3'],
  'Archives': ['zip', 'rar'],
  'Executables': ['exe', 'sh']
}

def get_file_extension(filename):
  if '.' in filename:
    return filename.rsplit('.', 1)[-1].lower()
  return ''

def create_folders(base_folder):
  for category in FILE_TYPES.keys():
    path = os.path.join(base_folder, category)
    if not os.path.exists(path):
      os.makedirs(path)

def sort_files(base_folder):
  for filename in os.listdir(base_folder):
    file_path = os.path.join(base_folder, filename)
    if os.path.isfile(file_path):
      ext = get_file_extension(filename)
      for category, extensions in FILE_TYPES.items():
        if ext in extensions:
          category_folder = os.path.join(base_folder, category)
          shutil.move(file_path, os.path.join(category_folder, filename))
          break

print('This program sorts files into separate folders based on their types.')
print('Supported file extensions: JPG, JPEG, PNG, MP4, MOV, PDF, TXT, DOCX, MP3, ZIP, RAR, EXE, SH')
print('Subfolders within the target directory will be ignored.')
base_folder = input('Enter the path of the folder to sort: ')
if not os.path.isdir(base_folder):
  print('Not a valid directory.')
else:
  try:
    create_folders(base_folder)
    sort_files(base_folder)
    print('Files have been sorted.')
  except Exception as e:
    print(f"An error occurred: {e}")