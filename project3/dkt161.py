### LINK FOR SAMPLE FOLDER WITH A VARIETY OF FILE TYPES:
### https://drive.google.com/drive/folders/17Uu0ZaxEnImWWbNe9q66ekZ3-oBum03-?usp=sharing
### One unsupported file for testing the warning feature (.ipv)
### After running the code once, you can move "Merc Storia OST2" out of the Audio folder and delete the "2", then test run again to test the renaming feature

def sort_files(dir):
    '''
    Automatically sort files into 6 category folders: Image, Audio, Video, Document, Data, and Executable.
    Argument:
    dir: the directory where the files you want to sort are in. Must be a raw string.
    Use forward slashes "/" instead of backslashes "\". The path must end with a slash.
    Example: r"C:/Users/admin/OneDrive/Documents/Python_practice/Project 3/"
    '''
    # Define file type dictionary
    file_types = {
        'Image/': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.xcf', '.psd'],
        'Audio/': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a'],
        'Video/': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv'],
        'Document/': ['.doc', '.docx', '.pdf', '.txt', '.rtf'],
        'Data/': ['.csv', '.tsv', '.xlsx', '.xls', '.xlsm', '.json', '.xml'],
        'Compressed/': ['.zip', '.rar', '.arc', '.arj', '.gz', '.hqx', '.sit', '.tar'],
        'Executable/': ['.exe', '.bat', '.sh']
    }
    # Retrieve the file names (excluding folders)
    file_names = []
    for item in os.listdir(dir):
        if os.path.isfile(dir + item):
            file_names.append(item)

    # Create folders if they don't exist
    folder_names = ['Image', 'Audio', 'Document', 'Data', 'Executable', 'Video']
    for folder in folder_names:
        if not os.path.exists(dir + folder):
            os.makedirs(dir + folder)
    
    # Check file names and sort
    for file in file_names:
        file_type = os.path.splitext(dir + file)[1].lower()
        found_category = False
        for category, type in file_types.items():
            if file_type in type and not os.path.exists(dir + category + file):
                shutil.move(dir + file, dir + category + file)
                found_category = True
                break
                
            # If a file with the same name already exists, add (i) to file name before moving
            elif file_type in type and os.path.exists(dir + category + file):
                base_name, type = os.path.splitext(file)
                i = 1
                new_name = f'{base_name} ({i}){type}'
                
                while os.path.exists(dir + category + new_name):
                    i += 1
                    new_name = f'{base_name} ({i}){type}'
                    
                shutil.move(dir + file, dir + category + new_name)
                found_category = True
                print(f'File "{file}" already exists. Renamed to "{new_name}"')
                break

        if not found_category:
                print(f'Unsupported file type: {file_type}. File name: {file}')

# Test run. Enter your own source directory
source_dir = r"C:/Users/admin/OneDrive/Documents/Python_practice/Project 3/"
sort_files(source_dir)
