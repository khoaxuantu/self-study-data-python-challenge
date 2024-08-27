import os
import glob
import shutil
from os import path
filename=glob.glob("C:/Users/admin/Downloads/*")
documents=['.pdf','.docx','.doc','.txt']
media=['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3']
setupFiles=['.exe','.msi']
compressedFiles=['.zip']
files=['.apk']
DocumentsLocation='C:/Users/admin/Downloads/documents'
mediaLocation='C:/Users/admin/Downloads/media'
setupFilesLocation='C:/Users/admin/Downloads/setupFiles'
compressedFilesLocation='C:/Users/admin/Downloads/compressedFiles'
FilesLocation='C:/Users/admin/Downloads/Files'
for file in filename:
    if os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file,DocumentsLocation)
    if os.path.splitext(file)[1] in media:
        if(path.exists(mediaLocation)):
            shutil.move(file,mediaLocation)
        else:
            os.mkdir(mediaLocation)
            shutil.move(file,mediaLocation)
    if os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file,setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file,compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
    if os.path.splitext(file)[1] in files:
        if(path.exists(FilesLocation)):
            shutil.move(file,FilesLocation)
        else:
            os.mkdir(FilesLocation)
            shutil.move(file,FilesLocation)

# Review:
# Here are some points to improve your code:
'''
1. Folder Existence Check Optimization:
The script repeatedly checks if a folder exists and creates it if necessary for each file type. This could be optimized by checking and creating all necessary folders at the beginning of the script, which would avoid redundant checks and make the code cleaner.
2. The script accounts for both lowercase and some uppercase extensions in the media list, but it could be further improved by converting all file extensions to lowercase before checking. This would ensure consistency and avoid potential issues.
3. The script does not currently handle cases where files with the same name already exist in the destination folder. You might want to add logic to handle such cases, such as appending a number to the file name or skipping the move. (You can use try/ except as well)
4. Consider make it more user-friendly by asking the user the input of the path (?)
'''