import shutil,os,re

file=input('Input đường dẫn của bạn tại đây: \n')

Images=['.jpg','.jpeg','.png','.gif','.bmp','.tiff','.svg','.webp','psd','psb']
Documents=['.pdf','.doc','.docx','.txt','.odt','.rtf','.html','.xlsx','.xls','.ppt','.pptx','.csv','tsv']
Compressed=['.zip','.rar','.tar','.gz','.7z','.bz2','.xz']
Audio=['.mp3','.wav','.aac','.flac','.ogg','.wma','.m4a']
Videos=['.mp4','.avi','.mov','.wmv','.flv','.mkv','.webm','.mpeg','.mpg']
Executable=['.exe','.bat','.sh','.bin','.msi','.apk','.app']
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
os.mkdir(os.path.join(downloads_folder,'Images'))
os.mkdir(os.path.join(downloads_folder,'Documents'))
os.mkdir(os.path.join(downloads_folder,'Compressed'))
os.mkdir(os.path.join(downloads_folder,'Audio'))
os.mkdir(os.path.join(downloads_folder,'Videos'))
os.mkdir(os.path.join(downloads_folder,'Executable'))
a=''
def Formated(Form):
    global a
    a='|'.join(Form)
    return a
def clarify(text):
    if re.findall(Formated(Images),text)!=[]:
        path=os.path.join(os.path.normpath(file),text)
        shutil.move(path,r'C:\Users\admin\Downloads\Images')
    elif re.findall(Formated(Documents),text)!=[]:
        path=os.path.join(os.path.normpath(file),text)
        shutil.move(path,r'C:\Users\admin\Downloads\Documents')
    elif re.findall(Formated(Compressed),text)!=[]:
        path=os.path.join(os.path.normpath(file),text)
        shutil.move(path,r'C:\Users\admin\Downloads\Compressed')
    elif re.findall(Formated(Audio),text)!=[]:
        path=os.path.join(os.path.normpath(file),text)
        shutil.move(path,r'C:\Users\admin\Downloads\Audio')
    elif re.findall(Formated(Videos),text)!=[]:
        path=os.path.join(os.path.normpath(file),text)
        shutil.move(path,r'C:\Users\admin\Downloads\Videos')
    elif re.findall(Formated(Executable),text)!=[]:
        path=os.path.join(os.path.normpath(file),text)
        shutil.move(path,r'C:\Users\admin\Downloads\Executable')

for i in os.listdir(os.path.normpath(file)):
    clarify(i)

# Review:
# Here are some points you can improve in your code:
'''
Existing Folders: The script does not handle the case where the folders already exist, which will raise a FileExistsError. Using os.makedirs() with the exist_ok=True parameter would prevent this error and make the script more robust.
File/Path Validations: The script assumes that the provided file path and files are valid. Adding checks to ensure that the input path exists and that files are not already in their target locations would prevent potential issues.
File Overwriting: If a file with the same name already exists in the destination folder, the script could potentially overwrite it. Consider implementing logic to handle such cases, perhaps by renaming the file or skipping it.
The use of a global variable (a) in the Formated function is unnecessary and could lead to issues in larger scripts. Instead, return the formatted string directly from the function and use it locally within clarify.
Additionally, since the script relies on re.findall to match file extensions, consider simplifying the logic by directly checking the file extension using string operations like endswith() for more readability and performance.
'''
