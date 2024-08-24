import os
import shutil
project3 = 'E:\\BK\\Challenge Python\\Project3'
folder = {'image': 'E:\\BK\\Challenge Python\\Project3\\image',
    'document': 'E:\\BK\\Challenge Python\\Project3\\document',
    'csv': 'E:\\BK\\Challenge Python\\Project3\\csv'}

category = {'image': ['.jpg', '.png'],
    'document': '.txt',
    'csv': ['.csv', '.tsv']}

for link in folder.values () :
    os.makedirs(link, exist_ok = True)

def classify () :
    for namefile in os.listdir(project3):
        filelink = os.path.join(project3, namefile)
        if os.path.isfile(filelink):
            expand = os.path.splitext(namefile)[1].lower()
            for filetype, expandlist in category.items():
                if expand in expandlist:
                    result = folder[filetype]
                    shutil.move(filelink, os.path.join(result, namefile))
                    break
classify ()    
