
#để file python cùng folder với những file cần sắp xếp

import os
import shutil
for file in os.listdir('.'):
    if os.path.splitext(file)[1] in ['.txt', '.pdf', '.doc', '.docx']:
        path = os.path.join('.', 'document_file')
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(os.path.join('.', file), path)
    elif os.path.splitext(file)[1] in ['.csv', '.tsv']:
        path = os.path.join('.', 'spreadsheet_file')
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(os.path.join('.', file), path)
    elif os.path.splitext(file)[1] in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp']:
        path = os.path.join('.', 'images_file')
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(os.path.join('.', file), path)
    elif os.path.splitext(file)[1] in ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz']:
        path = os.path.join('.', 'compressed_file')
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(os.path.join('.', file), path)
    elif os.path.splitext(file)[1] in ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a']:
        path = os.path.join('.', 'audio_file')
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(os.path.join('.', file), path)
    elif os.path.splitext(file)[1] in ['.exe', '.bat', '.sh', '.bin', '.app', '.msi']:
        path = os.path.join('.', 'executable_file')
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(os.path.join('.', file), path)
    
        
    # if not os.path.exists