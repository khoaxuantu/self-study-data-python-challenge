#create folders 
import os
import shutil

os.mkdir(r'C:\Users\hanne\Project3\PNG_file')
os.mkdir(r'C:\Users\hanne\Project3\JPG_file')
os.mkdir(r'C:\Users\hanne\Project3\TXT_file')
os.mkdir(r'C:\Users\hanne\Project3\CSV_file')


#move 

#png
png_path = r'C:\Users\hanne\Download\Max.png'
png_path2 = r'C:\Users\hanne\Download\Rosie.png'


shutil.move(png_path,r'C:\Users\hanne\Project3\PNG_file\Max.png')
shutil.move(png_path2,r'C:\Users\hanne\Project3\PNG_file\Rosie.png')

#jpg
jpg_path = r'C:\Users\hanne\Download\angrycat.jpg'
shutil.move(jpg_path,r'C:\Users\hanne\Project3\JPG_file\angrycat.jpg')

#txt
txt_path = r'C:\Users\hanne\Download\FakeFile.txt'
txt_path2 = r'C:\Users\hanne\Download\NewFile.txt'

shutil.move(txt_path, r'C:\Users\hanne\Project3\TXT_file\FakeFile.txt')
shutil.move(txt_path2, r'C:\Users\hanne\Project3\TXT_file\NewFile.txt')


# Review:
'''
Handling Directory Creation Dynamically: Instead of hardcoding the creation of directories, you can dynamically create directories based on file types or extensions. This reduces code repetition.
Error Handling: Add error handling to account for scenarios where the source file might not exist or if there's an issue during the move operation.
Avoiding Hardcoding of Paths: Using hardcoded paths makes the code less flexible. Instead, consider creating a function that can handle any type of file, making the code more reusable.
Optimization: Instead of calling shutil.move() separately for each file, you can loop through a list of files to streamline the process.
'''




