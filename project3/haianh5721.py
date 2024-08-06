import os

import shutil



def get_file_type(filename):

    ext = os.path.splitext(filename)[1].lower()

    if ext in ['.png', '.jpg', '.jpeg']:

        return 'Images'

    elif ext == '.txt':

        return 'Text'

    elif ext == '.csv':

        return 'CSV'

    elif ext == '.tsv':

        return 'TSV'

    else:

        return 'Other'



def organize_files(input_dir, output_dir):

    file_types = set()

    

    for filename in os.listdir(input_dir):

        file_path = os.path.join(input_dir, filename)

        if os.path.isfile(file_path):

            file_type = get_file_type(filename)

            file_types.add(file_type)

            

            # Tạo thư mục đích nếu chưa tồn tại

            dest_dir = os.path.join(output_dir, file_type)

            os.makedirs(dest_dir, exist_ok=True)

            

            # Di chuyển file

            shutil.move(file_path, os.path.join(dest_dir, filename))

    

print("done")

# Sử dụng hàm

input_directory = 'link to project 3'

output_directory = 'link to project 3 '

organize_files(input_directory, output_directory)
