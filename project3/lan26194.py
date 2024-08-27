import os, shutil

path = input("Enter the path: ")
files=os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)
    target_folder = os.path.join(path, extension[1:])
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    shutil.move(os.path.join(path, file), os.path.join(target_folder, file))

# Review:
# Here are some points to improve your code:
'''
Be aware that our project is to sort to different file types based on the extension. E.g: Documents (.doc, .pdf), Audio (.mp3), etc
If two files have the same name and extension, the second file will overwrite the first in the target directory. To prevent this, consider renaming the file if a duplicate is found, or skip moving it.
Your script currently places files without extensions into a folder with an empty name. You might want to add a check to handle these cases differently, such as moving them to a folder named "no_extension" or similar.
'''