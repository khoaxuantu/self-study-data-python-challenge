import os, shutil


PATH = 'C:\\Users\\Thi\\Downloads\\Documents'
list_file_names = os.listdir(PATH)


for file in list_file_names:
    try:
        if '.pdf' in file and not os.path.exists(PATH + '\\mp4' + '\\' + file):
            path_file = PATH + '\\' + file
            path_pdf = PATH + '\\pdf' + '\\' + file
            shutil.move(path_file, path_pdf)

        elif '.txt' in file and not os.path.exists(PATH + '\\mp4' + '\\' + file):
            path_file = PATH + '\\' + file
            path_pdf = PATH + '\\txt' + '\\' + file
            shutil.move(path_file, path_pdf)

        elif '.png' in file and not os.path.exists(PATH + '\\mp4' + '\\' + file):
            path_file = PATH + '\\' + file
            path_pdf = PATH + '\\png' + '\\' + file
            shutil.move(path_file, path_pdf)

        elif '.tsv' in file and not os.path.exists(PATH + '\\mp4' + '\\' + file):
            path_file = PATH + '\\' + file
            path_pdf = PATH + '\\tsv' + '\\' + file
            shutil.move(path_file, path_pdf)

        elif '.csv' in file and not os.path.exists(PATH + '\\mp4' + '\\' + file):
            path_file = PATH + '\\' + file
            path_pdf = PATH + '\\csv' + '\\' + file
            shutil.move(path_file, path_pdf)

        elif '.mp4' in file and not os.path.exists(PATH + '\\mp4' + '\\' + file):
            path_file = PATH + '\\' + file
            path_pdf = PATH + '\\mp4' + '\\' + file
            shutil.move(path_file, path_pdf)

        else:
            print(f'This {file} can not move. It can be a folder name or the same name as another file.')
    except FileNotFoundError as e:
        print(f'{e}. This {file} needs to be created in a directory.')

# Review:
'''
0. In this project, you are assuming that there are already created folders for each file types. However, we want you to sort a folder with given files into seperated folders with each a different file types
1. Incorrect Directory Check for File Movement:
In your code, you are checking if the file already exists in the mp4 folder before moving it, even for files that are not .mp4. This is not correct because you should check if the file already exists in the respective folder for that file type (e.g., pdf, txt, etc.).
2. Incorrect Variable Names in Path Construction:
You are constructing the target path variable as path_pdf, but this variable name suggests it is only for .pdf files. You should use more descriptive and general variable names like target_path to avoid confusion.
3. String Concatenation Instead of os.path.join:
You are concatenating paths using + '\\' +. This method is not ideal because it can lead to errors in cross-platform environments. Instead, use os.path.join to concatenate paths, which ensures that the correct path separator is used for the operating system.
4. Misleading Error Message:
The error message in your FileNotFoundError exception might be confusing because it mentions that the file needs to be created, which is not typically the issue in this context. The actual issue is more likely to be related to the source file not being found.
5. Repeated Code:
Your code repeats the same block of logic for each file type. This could be refactored to avoid redundancy.
'''