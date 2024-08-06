import os
import shutil

def sort(path):
    for file in os.listdir(path):#chdir thay đổi folder hiện tại ,listdir Liệt kê các tệp và thư mục trong một thư mục
        file_path=os.path.join(path,file)#link đường link lại ("C:../Project 3"với mấy file txt...)
        name, ext = os.path.splitext(file)# vd:cat.jpg name=cat ext=.jpg

        if ext == ".jpg" or ext==".png" or ext==".gif" or ext==".bmp":
            file_type="image"
        elif  ext==".mp4" or ext==".mkv" or ext==".avi" or ext==".wmv":
            file_type="video"
        elif ext==".zip" or ext==".rar" or ext==".7z":
            file_type="Zipped file"
        elif ext==".mp3" or ext==".wav" or ext==".flac" or ext==".ogg":
            file_type="audio files"
        elif ext==".exe" or ext==".bat" or ext==".sh" or ext==".by":
            file_type="Executable files"
        else:
            file_type="documents"
        folder=os.path.join(path,file_type)#link đường link lại ("C:../Project 3"với mấy tên foler đồ)
        if not os.path.exists(folder):
            os.mkdir(folder)
        shutil.move(file_path, folder)#di chuyển (vt cũ > vt mới)

link="C:/Users/ADMIN/OneDrive/Desktop/Data Analyst/Khóa học Python/Python turtorial/Project 3"
sort(link)
