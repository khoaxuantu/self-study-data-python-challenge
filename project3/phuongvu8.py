import os
import shutil

word_dest = r'/Users/phuongminh/Desktop/Word_File'
excel_dest = r'/Users/phuongminh/Desktop/Excel_File'
csv_dest = r'/Users/phuongminh/Desktop/CSV_File'
image_dest = r'/Users/phuongminh/Desktop/Image_File'
video_dest = r'/Users/phuongminh/Desktop/Video_File'
sql_dest = r'/Users/phuongminh/Desktop/SQL_File'

word_file = []
excel_file = []
csv_file = []
image_file = []
video_file = []
sql_file = []

desktop_path = '/Users/phuongminh/Desktop/'
for file in os.listdir(desktop_path): 
    file_path = os.path.join(desktop_path, file)
    if os.path.isfile(file_path):
        if file.endswith('.csv'):
            csv_file.append(file_path)
        
        if file.endswith('.mp4') or file.endswith('.MOV'):
            video_file.append(file_path)
        
        if file.endswith('.xls') or file.endswith('.xlsx'):
            excel_file.append(file_path)
        
        if file.endswith('.sql'):
            sql_file.append(file_path)
        
        if file.endswith('.jpg') or file.lower().endswith('.png') or file.endswith('.HEIC'):
            image_file.append(file_path)
        
        if file.endswith('.doc') or file.endswith('.docx') :
            word_file.append(file_path)

for files in word_file:
    if not os.path.exists(word_dest): 
        os.makedirs(word_dest)
    shutil.move(files,word_dest) 
    
for files in image_file:
    if not os.path.exists(image_dest): 
        os.makedirs(image_dest)
    shutil.move(files,image_dest) 

for files in sql_file:
    if not os.path.exists(sql_dest): 
        os.makedirs(sql_dest)
    shutil.move(files,sql_dest) 

for files in excel_file:
    if not os.path.exists(excel_dest): 
        os.makedirs(excel_dest)
    shutil.move(files,excel_dest) 

for files in video_file:
    if not os.path.exists(video_dest): 
        os.makedirs(video_dest)
    shutil.move(files,video_dest) 

for files in csv_file:
    if not os.path.exists(csv_dest): 
        os.makedirs(csv_dest)
    shutil.move(files,csv_dest) 
 