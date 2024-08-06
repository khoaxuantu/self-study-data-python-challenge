import os
import glob
import shutil
from os import path
filename=glob.glob("C:/Users/trang_phan/Downloads/*")
documents=['.pdf','.docx','.doc','.txt']
media=['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3']
setupFiles=['.exe','.msi']
compressedFiles=['.zip']
files=['.apk']
DocumentsLocation='C:/Users/trang_phan/Downloads/documents'
mediaLocation='C:/Users/trang_phan/Downloads/media'
setupFilesLocation='C:/Users/trang_phan/Downloads/setupFiles'
compressedFilesLocation='C:/Users/trang_phan/Downloads/compressedFiles'
FilesLocation='C:/Users/trang_phan/Downloads/Files'
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