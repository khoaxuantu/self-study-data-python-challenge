import os
import shutil
file_types={
    'mp3':'Audios',
    'mp4':'Video',
    'jpg':'Images',
    'doc':'Documents',
    'rar':'Archives',
    'exe':'Executables'}
for folder in file_types.values():
    if not os.path.exists(folder):
        os.makedirs(folder)
source_folder='D:\self-study python'
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        
        extension = filename.split('.')[-1].lower()
        
        if extension in ['doc', 'docx', 'pdf', 'txt']:
            destination = 'Documents'
        elif extension in ['zip', 'rar']:
            destination = 'Archives'
        elif extension in ['mp3', 'wav']:
            destination = 'Audios'
        elif extension in ['mp4', 'avi']:
            destination = 'Videos'
        elif extension in ['jpg', 'png']:
            destination = 'Images'
        elif extension in ['exe']:
            destination = 'Executables'
        else:
            destination = 'Others'
        
        shutil.move(file_path, os.path.join(destination, filename))

#Good job on completing this project:
#However, here are some points you can improve your code:
'''
Consider using os.makedirs(destination, exist_ok=True) directly in the move process to avoid repetition.
Ensure handling of files without extensions or those with uncommon extensions. (You may use try/except)
You might want to move all the files into a designated directory, rather than leaving some in the source directory if they don't match known types.
'''