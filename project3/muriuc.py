
import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

# Review:
# Here are some points for you to improve your code:
'''
Path Construction: Replaced manual path concatenation with os.path.join for better cross-platform compatibility.
Extension Handling: Added handling for files without extensions, moving them to a "No Extension" folder.
Error Handling: Added a check to validate if the provided path exists before proceeding. (try/except)
Remember our project is to sort to different file types based on the extension. E.g: Documents (.doc, .pdf), Audio (.mp3), etc
'''