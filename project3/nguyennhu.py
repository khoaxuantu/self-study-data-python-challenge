import os

def sort_file (path):
    # Step 1: List all the files
    try:
        list_files = os.listdir(path)
    except:
        print ('Invalid path') 
        return 0
    
    # Step 2: Sort files
    file_types = {
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'heic', 'svg'],
    'Documents': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf', 'txt', 'rtf', 'odt', 'md', 'csv'],
    'Videos': ['mp4', 'avi', 'mov', 'wmv', 'mkv', 'flv', 'webm', 'mpeg', 'mpg'],
    'Compressed Files': ['zip', 'rar', '7z', 'gz', 'tar', 'bz2'],
    'Audio Files': ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'aiff', 'm4a'],
    'Executable Files': ['exe', 'out', 'app', 'bin', 'sh', 'bat', 'cmd', 'jar', 'py']
    }
    no_file = 0
    remain_files = []

    for file_name in list_files:
        if '.' in file_name: #check whether it is a file or a folder
            no_file += 1
            file_type = file_name.split ('.')[-1]
            for category, type in file_types.items():
                if (file_type in type):
                    current_path = f'{path}\\{file_name}'
                    new_path = f'{path}\\{category}\\{file_name}'
                    os.makedirs(os.path.dirname(new_path), exist_ok=True) #create category folder if not exist
                    os.replace(current_path, new_path)
                    result = 'Moved'
                    break
                else:
                    result = 'Not found'
            if result == 'Not found':
                remain_files.append (file_name)
        else:
            continue

            
    # Step 3: Print the result
    if no_file == 0:
        print ('No files found in the path')
        return 1
    elif len (remain_files) == 0:
        print('All files have been successfully sorted.')
        return 1
    elif len (remain_files) > 0:
        print('These files were not sorted because their types are not in my list:', ', '.join(remain_files))
        return 0

sort_file (path = f'C:\\Users\\NguyenThiQuynhNhu\\Documents\\nhunguyen\\Python_Challenge\\project_3\\files')



