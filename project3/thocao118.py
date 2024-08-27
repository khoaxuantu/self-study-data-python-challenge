import os 
import shutil

# Bước 1:________________________________________________________________________________________________
# INPUT: đây là đường dẫn Folder, đang chứa những file cần phân loại
# User vui lòng thay đổi trực tiếp đường dẫn Folder trong code để thích ứng với từng máy 
# Link drive chứa các file: https://drive.google.com/drive/folders/11L0ZjZ7h597Hn0cuxrJZ6COGYQwx0gMW?usp=sharing

guide ='''
Xin bạn ít thì giờ đọc HƯỚNG DẪN sau:
   "Để code chạy mượt hơn,
    Bạn vui lòng truy cập code dòng thứ 18.
    Sau đó, bạn thay đổi trực tiếp đường dẫn Folder đang chứa các file cần sắp xếp nhé !"
 
'''
print('\033[34m'+ guide +'\033[0m')

path_from = r'C:\Users\HAN NGA\Downloads\Project 3 file drive'
# Đường dẫn folder trong máy Thỏ Cáo là: C:\Users\HAN NGA\Downloads\Project 3 file drive


lst_file = os.listdir(path_from)
print('Trong folder gốc, đang chứa các file cần được phân loại là:  ')
print('  ', end='')
print(*lst_file, sep='\n  ')


# Bước 2:________________________________________________________________________________________________
# Tạo 6 Folder đích là 6 nơi để phân loại file

# Tạo 1 folder chung chứa 6 folder con, đề phòng chạy lẫn với bài các bạn khác 
if not os.path.exists('thocao118_folder_pj3'):
    os.mkdir('thocao118_folder_pj3')
    
path_taget = r'thocao118_folder_pj3'


# Tạo 6 Folder: văn bản, hình ảnh, video, âm thanh, file nén, file thực thi
# document: txt, md, docx, csv, tsv, xlsx, pdf
# image: jpg, png, jpeg, gif, bmp, tiff
# video: mp4, mov, avi, mkv
# audio: mp3, wav, aac, flac
# compressed: rar, rip
# executable: exe

folder_names = ['document files', 'image files', 'video files', 'audio files', 'compressed files', 'executable files']   

for folder in range(6): 
    if not os.path.exists(path_taget +'\\'+ folder_names[folder]):  
        os.makedirs(path_taget +'\\'+ folder_names[folder])
 
print('\nCác file đang được phân loại vào 6 folder sau:')
for folder in range(6):
	print('  ' + path_taget +'\\'+ folder_names[folder])   
    


# Bước 3:________________________________________________________________________________________________
# Phân loại theo đuôi file
print('\n\u2757 Các file chưa được phân loại là:') 
        
for file in lst_file: 
	name, ext = os.path.splitext(file)

	ext = ext[1:].lower()

	if ext == '': 
		print(f'''  \033[34m"{file}"\033[0m ko được phân loại vì ko có đuôi, mk ko biết đây là file loại gì.\n''')
		continue
	
	elif ext not in ['txt', 'md', 'docx', 'csv', 'tsv', 'xlsx', 'pdf', 
                  	'jpg', 'png', 'jpeg', 'gif', 'bmp', 'tiff',
                   	'mp4', 'mov', 'avi', 'mkv',
                    'mp3', 'wav', 'aac', 'flac',
                    'rar', 'zip',
                    'exe']:
		print(f'''  \033[34m"{file}"\033[0m ko được phân loại. Rất tiếc vì mk chưa xét đến định dạng đuôi {ext} này.\n''')
 
	elif ext in ['txt', 'md', 'docx', 'csv', 'tsv', 'xlsx', 'pdf'] and not os.path.exists(path_taget +'\\document files\\'+file): 
		shutil.move(path_from +'\\'+ file, path_taget +'\\document files\\'+file)
  
	elif ext in ['jpg', 'png', 'jpeg', 'gif', 'bmp', 'tiff'] and not os.path.exists(path_taget +'\\image files\\'+file): 
		shutil.move(path_from +'\\'+ file, path_taget +'\\image files\\'+file)
  
	elif ext in ['mp4', 'mov', 'avi', 'mkv'] and not os.path.exists(path_taget +'\\video files\\'+file): 
		shutil.move(path_from +'\\'+ file, path_taget +'\\video files\\'+file)
  
	elif ext in ['mp3', 'wav', 'aac', 'flac'] and not os.path.exists(path_taget +'\\audio files\\'+file): 
		shutil.move(path_from +'\\'+ file, path_taget +'\\audio files\\'+file)  
  
	elif ext in ['rar', 'zip'] and not os.path.exists(path_taget +'\\compressed files\\'+file): 
		shutil.move(path_from +'\\'+ file, path_taget +'\\compressed files\\'+file) 
  
	elif ext in ['exe'] and not os.path.exists(path_taget +'\\executable files\\'+file): 
		shutil.move(path_from +'\\'+ file, path_taget +'\\executable files\\'+file)
	else:
		print(f'''  \033[34m"{file}"\033[0m trùng với một file đã được phân loại trước đó.\n''')

# Review:
# Gud job on completing this project so! Nice guide for the user btw, however, consider these areas so that you can improve your code:
# Path Handling: Instead of using string concatenation like path_taget +'\\'+ folder_names[folder], consider using os.path.join(path_taget, folder_names[folder]) for better cross-platform compatibility.
# Error Handling: While your script identifies files that don't have extensions or unrecognized extensions, adding error handling for scenarios like permission issues or other unexpected errors during file operations would improve its robustness.
# Optimization: You might consider refactoring the multiple if-elif statements for file extension checking into a dictionary lookup or another data structure for more efficient code.
# You can let the user input their desired path in the input as well, if you want to make it more user-friendly.
# Keep it uppp!!