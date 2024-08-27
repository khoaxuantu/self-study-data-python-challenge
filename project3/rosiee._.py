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

# Review:
# Here are some points you can improve your project, keep it up!!
'''
1. Handling Non-Matching Files:
If a file's extension doesn't match any in the category dictionary, it won't be moved. You might want to log these or move them to a separate "others" folder.
2. Duplicate File Names:
If a file with the same name already exists in the destination folder, shutil.move will overwrite it. Consider adding a check for this scenario and perhaps renaming the file before moving it.
3. Folder Name Consistency:
Ensure the keys in the category and folder dictionaries are consistent to avoid misclassification.
4. Edge Cases:
The code doesn't currently handle symbolic links, hidden files, or files without extensions. Depending on your needs, you might want to include or exclude these from classification.
5. Optimization:
For larger projects or directories with many files, consider adding logging or tracking to identify how many files were moved and where.
'''
