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
    
