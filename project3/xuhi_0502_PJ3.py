import os

import shutil

path = r'C:/Users/Pandal Pan/OneDrive/Desktop/Project 3/DataSource/'    # Please change the path to the corresponding directory on your laptop

MoveFile = os.listdir(path)

subfolders_name = ['CSVFiles', 'TXTFiles', 'TSVFiles', 'PNGFiles', 'JPGFiles', 'DOCXFiles', 'EXCELFiles']


# Create different folders, each contains files with different file extensions
for i in range(0,7):   
    if not os.path.exists(path + subfolders_name[i]):
        print(path + subfolders_name[i])    
        os.makedirs((path + subfolders_name[i]))
        


# Move files to corresponding subfolders
for x in MoveFile:
    if '.csv' in x and not os.path.exists(path + 'CSVFiles/' + x):
        shutil.move(path + x, path + 'CSVFiles/' + x) 
    elif '.txt' in x and not os.path.exists(path + 'TXTFiles/' + x):
        shutil.move(path + x, path + 'TXTFiles/' + x)     
    elif '.tsv' in x and not os.path.exists(path + 'TSVFiles/' + x):
        shutil.move(path + x, path + 'TSVFiles/' + x)    
    elif '.png' in x and not os.path.exists(path + 'PNGFiles/' + x):
        shutil.move(path + x, path + 'PNGFiles/' + x)    
    elif '.jpg' in x and not os.path.exists(path + 'JPGFiles/' + x):
        shutil.move(path + x, path + 'JPGFiles/' + x)    
    elif '.docx' in x and not os.path.exists(path + 'DOCXFiles/' + x):
        shutil.move(path + x, path + 'DOCXFiles/' + x)
    elif '.xlsx' in x and not os.path.exists(path + 'EXCELFiles/' + x):
        shutil.move(path + x, path + 'EXCELFiles/' + x)   
    else:
         print("There is an error. Files could not be moved.")
         


# Uncommment the below code and run it to return files in the sub-folders to the main folder (Folder Project 3/ DataSource)
# for a in os.listdir(path + 'CSVFiles'):
#     shutil.move(path + 'CSVFiles/' + a, path + a)

# for a in os.listdir(path + 'TXTFiles'):
#     shutil.move(path + 'TXTFiles/' + a, path + a)
    
# for a in os.listdir(path + 'TSVFiles'):
#     shutil.move(path + 'TSVFiles/' + a, path + a)
    
# for a in os.listdir(path + 'PNGFiles'):
#     shutil.move(path + 'PNGFiles/' + a, path + a)
    
# for a in os.listdir(path + 'JPGFiles'):
#     shutil.move(path + 'JPGFiles/' + a, path + a)
    
# for a in os.listdir(path + 'DOCXFiles'):
#     shutil.move(path + 'DOCXFiles/' + a, path + a)
    
# for a in os.listdir(path + 'EXCELFiles'):
#     shutil.move(path + 'EXCELFiles/' + a, path + a)


#Review:
# Your script successfully categorizes files into specific folders based on their extensions, and it handles seven different file types, which is commendable and qualifies you for the maximum bonus points.
# Areas to improve:
# Adding error handling and a mechanism to deal with unsupported file types would make your script more robust and comprehensive.
