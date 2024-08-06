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