import os
import shutil

def sort_oldfile (file_path):
  ### prefix (WHERE you want sorted folder place) ###
  path_of_file = os.path.dirname(file_path)
  prefix = path_of_file + '/'
  #split file
  path_ext = os.path.splitext (file_path)
  #take file_name (WITHOUT extention)
  file_name = os.path.basename(file_path)
  #take file extension
  file_extension = path_ext [1]
  #make folder
  folder_path = prefix  + 'file_' + file_extension.replace ('.','') + '/'
  if not os.path.exists (folder_path):
    os.makedirs (folder_path)
  ## move file to folder
  new_folder_file_path = folder_path + file_name
  i = 1
  #if the file_name already exist in that folder
  while os.path.exists (new_folder_file_path):
    new_folder_file_path = os.path.splitext (new_folder_file_path)
    new_folder_file_path = new_folder_file_path[0] + '(' + str(i) + ')' + new_folder_file_path[1]
    #check if new_file_path exist or not
    if os.path.exists (new_folder_file_path):
      i += 1
    else: 
      new_file_path = path_ext[0] + '(' + str(i) + ')' + path_ext [1]
      os.rename(file_path,new_file_path)
      shutil.move (new_file_path, new_folder_file_path)
      print (f"\nOriginal file {file_path} has renamed as {new_file_path} located in folder {new_folder_file_path} due to name duplication. \n")
      break
  else:
    shutil.move (file_path, new_folder_file_path)
    print (f"\nFile {file_path} has moved to folder {new_folder_file_path} \n")

#MAIN
while True:
  user_input = input ("Enter your file path ('q' to quit): ")
  if user_input.lower() == 'q':
    break
  try:
    sort_oldfile (user_input.strip ())
  except:
    print ("Please enter correct file path.\n")

# Review:
'''
Good job on completing the project. However, there's some improvement you can look through to improve your code:
Here, you let the user decide which file to sort, but our project would recommend to sort a whole folder instead of file by file. Therefore you need some functions to check the extensions and organize the
files based on their extension. E.g: Documents: .pdf, .txt, etc
'''
