import os
import shutil

def organize_files(root_directory):
    file_type_categories = {
        'Programming': ['.c', '.cpp', '.py', '.ipynb', '.cs', '.js', '.go', '.java'],
        'Audio': ['.mp3'],
        'Video': ['.mp4'],
        'Image': ['.jpg', '.png', '.gif', '.bmp'],
        'Data': ['.csv', '.txt', '.json', '.xml', '.pdf'],
        'O365': ['.xlsx', '.pptx', '.docx'],
        'Executable': ['.exe'],
        'Archive': ['.zip', '.rar']
    }

    for category in file_type_categories.keys():
        os.makedirs(os.path.join(root_directory, category), exist_ok=True)
    os.makedirs(os.path.join(root_directory, 'Others'), exist_ok=True)
    
    for filename in os.listdir(root_directory):
        file_path = os.path.join(root_directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            file_moved = False
            for category, extensions in file_type_categories.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(root_directory, category, filename))
                    file_moved = True
                    break
            if not file_moved:
                shutil.move(file_path, os.path.join(root_directory, 'Others', filename))

def print_directory_tree(directory, indent_level=0):
    print('    ' * indent_level + os.path.basename(directory) + '/')
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print_directory_tree(item_path, indent_level + 1)
        else:
            print('    ' * (indent_level + 1) + item)

def main():
    root_directory = input("Enter the system path: ")
    if not os.path.exists(root_directory):
        print("Warning: The specified path does not exist.")
        return

    organize_files(root_directory)
    print("Tree structure after organizing:")
    print_directory_tree(root_directory)
    print("\nProgram finished. Files have been organized.")

if __name__ == "__main__":
    main()

# Review:
# Good job on completing this project, however, just some small points you can consider on your future project:
'''
Consider adding error handling for file operations (like shutil.move) to catch and report issues such as permission errors or files that can't be moved.
Adding print statements or logging to inform the user about each file being moved could be helpful for larger directories to track progress.
'''