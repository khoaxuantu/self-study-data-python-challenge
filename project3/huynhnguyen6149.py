import os
import shutil

#Hàm tạo folder và thêm file vào folder
def create_append(folder_name, entry_path):

    # Kiểm tra xem thư mục đã tồn tại chưa và thêm file vào
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        new_folder_path = os.path.join(os.getcwd(), folder_name)
        shutil.move(entry_path, new_folder_path)

    # Nếu tồn tại thì thêm các file tương ứng vào
    else:
        new_folder_path = os.path.join(os.getcwd(), folder_name)
        shutil.move(entry_path, new_folder_path)

#Hàm phân loại file
def categorize_files_by_type(directory):
    
    document = {'.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.csv', '.log', '.xlr'
                '.ppt', '.pptx', '.odt', '.ods', '.odp', '.tsv', '.pps', '.rtf', '.wpd', '.wps' }
    image = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.svg', '.cur', '.ico', '.raw'}
    video = {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'}
    audio = {'.aif', '.m3u', '.mp3', '.ra', '.wav', '.wma'}
    compressed = {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.lz'}
    executable = {'.exe', '.bat', '.cmd', '.sh', '.bin', '.app', '.jar', '.run'}
    

    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry) 

        if os.path.isfile(entry_path):
            ext = os.path.splitext(entry)[1].lower()
            
            if ext in document:
                create_append('Document', entry_path)
            elif ext in image:
                create_append('Image', entry_path)
            elif ext in video:
                create_append('Video', entry_path)
            elif ext in audio:
                create_append('Audio', entry_path)
            elif ext in compressed:
                create_append('Compressed', entry_path)
            elif ext in executable:
                create_append('Executable', entry_path)
            else:
                create_append('Other', entry_path)

if __name__ == '__main__':
    # Thư mục cần xử lý
    directory_path = r'D:\Python Challenge\Day 24'
    categorized_files = categorize_files_by_type(directory_path)
