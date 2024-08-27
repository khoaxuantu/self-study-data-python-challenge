import os
import shutil
if not os.path.exists(r"D:\sortfile\textfile"):
    os.mkdir(r"D:\sortfile\textfile")

if not os.path.exists(r"D:\sortfile\imaginefile"):
    os.mkdir(r"D:\sortfile\imaginefile")

if not os.path.exists(r"D:\sortfile\audiofile"):
    os.mkdir(r"D:\sortfile\audiofile")

if not os.path.exists(r"D:\sortfile\compressed file"):
    os.mkdir(r"D:\sortfile\compressedfile")

# Đường dẫn tới thư mục chứa các tệp
directory = "D:/sortfile"
        
# Duyệt qua tất cả các tệp trong thư mục
for filename in os.listdir(directory):
    # Lấy phần mở rộng của tệp
    _, ext = os.path.splitext(filename)
    
    # Phân loại tệp theo phần mở rộng
    if ext.lower() == ".csv" or ext.lower() == ".txt"or ext.lower() == ".tsv":
        shutil.copy(f"D:/sortfile/{filename}",f"D:/sortfile/textfile/{filename}")
    elif ext.lower() == ".jng" or ext.lower() == ".png":
        shutil.copy(f"D:/sortfile/{filename}",f"D:/sortfile/imaginefile/{filename}")
    elif ext.lower() == ".mp3":
       shutil.copy(f"D:/sortfile/{filename}",f"D:/sortfile/audiofile/{filename}")
    elif ext.lower() == ".zip" or ext.lower() == ".rar" or ext.lower() == "..gz" or ext.lower() == ".tar":
       shutil.copy(f"D:/sortfile/{filename}",f"D:/sortfile/compressedfile/{filename}")

# Review:
# Good job on completing this project but here are some points you can take a look to improve it:
'''
Redundant Folder Creation: You could create a list or dictionary to store folder paths and iterate through them to reduce repetition in your folder creation logic.
File Extensions Typo: There's a typo in the extension ".jng" (likely intended to be ".jpg"). Also, double periods in "..gz" might cause issues. Ensure that the extensions are correct.
File Overwriting: Since you are copying files, if a file with the same name already exists in the destination, it will be overwritten. Consider handling this by renaming files or checking before copying.
Improving Path Construction: Using os.path.join(directory, filename) instead of hardcoding paths like f"D:/sortfile/{filename}" would make your script more flexible and robust against changes in directory paths.
'''