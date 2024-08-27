import os
import shutil

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_file(file, target_dir):
    try:
        shutil.move(file, target_dir)
        print(f"Moved {file} to {target_dir}")
    except Exception as e:
        print(f"Error moving file {file}: {e}")

def categorize_files(source_dir):
    categories = {
        'Images': ['.jpg', '.png', '.jpeg', '.gif'],
        'Documents': ['.txt', '.doc', '.docx', '.pdf'],
        'Spreadsheets': ['.csv', '.xls', '.xlsx', '.tsv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Executables': ['.exe', '.bat', '.sh'],
        'Sounds': ['.mp3', '.wav', '.aac', '.flac', '.wma'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
        'Others': []
    }

    for category in categories:
        create_directory(os.path.join(source_dir, category))

    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            moved = False

            for category, extensions in categories.items():
                if file_ext in extensions:
                    target_dir = os.path.join(source_dir, category)
                    move_file(file_path, target_dir)
                    moved = True
                    break
            
            if not moved:
                target_dir = os.path.join(source_dir, 'others')
                move_file(file_path, target_dir)

source_directory = input('Enter the path of the folder to sort: ')
if not os.path.isdir(source_directory):
    print('Not a valid directory.')
else:
    categorize_files(source_directory)

# Review:
# Well-done on this project. You nailed it!!!