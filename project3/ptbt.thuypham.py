import os
import shutil
import glob

def organize_files_by_type(directory):
    # Define the categories and their corresponding file extensions
    file_categories = {
        'compressed': ['zip', 'tar', 'gz', 'rar', '7z'],
        'audio': ['mp3', 'wav', 'flac', 'aac', 'ogg'],
        'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
        'documents': ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'csv', 'tsv'],
        'videos': ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv'],
        'scripts': ['py', 'sql'],
        'powerbi': ['pbix', 'pbit'],
        'tableau': ['twb', 'twbx'],
        'jupyter': ['ipynb']
    }

    os.chdir(directory)
    files = glob.glob('*.*')
    
    for filename in files:
        file_extension = filename.split('.')[-1].lower()
        category = None
        
        for cat, extensions in file_categories.items():
            if file_extension in extensions:
                category = cat
                break
        if not category:
            category = file_extension
        
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

# Example usage
directory = 'path/to/your/directory'
#r'D:\NGOC NUOC\DATA\drive-download-20240804T050040Z-001'
organize_files_by_type(directory)
