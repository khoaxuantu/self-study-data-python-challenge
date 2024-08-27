import os
import shutil
source_folder = r'C:\Users\ADMIN\Downloads\project3'
folders = {
    'images': ['jpg', 'jpeg', 'png', 'gif'],
    'documents': ['pdf', 'docx', 'txt', 'csv', 'tsv'],
    'videos': ['mp4', 'mkv', 'mov'],
    'audio': ['mp3', 'wav', 'aac'],
    'compressed': ['zip', 'rar', '7z'],
    'executables': ['exe', 'bat']
}
for folder in folders:
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
sorted_files = []
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        file_ext = filename.split('.')[-1].lower()
        for folder, extensions in folders.items():
            if file_ext in extensions:
                destination_path = os.path.join(source_folder, folder, filename)
                shutil.move(file_path, destination_path)
                sorted_files.append(destination_path)
                break
print("Danh sách các thư mục và nội dung:")
for folder in folders.keys():
    folder_path = os.path.join(source_folder, folder)
    if os.path.exists(folder_path):
        print(f"\nThư mục '{folder}':")
        files_in_folder = os.listdir(folder_path)
        if not files_in_folder:
            print("  (Không có tệp)")
        else:
            for filename in files_in_folder:
                print(f"  {filename}")

print("\nHoàn thành sắp xếp các tệp vào các thư mục tương ứng.")

# Review:
'''
File Extension Handling: Consider using os.path.splitext(filename) to extract the file extension instead of filename.split('.')[-1]. This method is more robust, especially for filenames with multiple periods.

Efficiency: Instead of iterating over the folders' keys multiple times, you could use a dictionary that directly maps file extensions to their respective folders, reducing the number of iterations.
'''