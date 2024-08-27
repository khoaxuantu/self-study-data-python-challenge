import os
import shutil

def sorting_file():
    working_dir = input("Enter the path to the targeting directory: ")
    os.chdir(working_dir)
    file_lst = os.listdir()
    for file_name in file_lst:
        if(not os.path.isfile(file_name)):
            continue
        reverse_name = file_name[::-1]
        pos = reverse_name.find('.')
        type_file = reverse_name[:pos]
        type_file = type_file[::-1]
        type_file += 'Folder'
        if not os.path.exists(type_file):
            os.mkdir(type_file)
        shutil.move(file_name, type_file)

sorting_file()

# Review:
'''
Use os.path.splitext: This function is more reliable for getting file extensions and handles filenames without extensions.
Error Handling: Add exception handling for better robustness.
And remember that out project would require you to sort files into different file types. E.g: Documents: .pdf, .txt; Audio: .mp3, .av rather than sort it based on the file extension
'''