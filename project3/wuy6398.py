file_types = {
    'Images': ['.jpg', '.png', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audios': ['.mp3', '.wav', '.aac'],
    'Documents': ['.doc', '.txt', '.pdf'],
    'Compressed Files': ['.zip', '.rar', '.arc'],
    'Executable Files': ['.exe', '.bin', '.cmd']
}

#Tạo các folder để phân loại
for i in file_types.keys():
    if not os.path.exists('/'.join([direc, i])):
        os.mkdir('/'.join([direc, i]))

#Yêu cầu nhập đường dẫn của folder cần phân loại và lấy ra tên của các file trong folder
while True:
    try:
        direc = input(r"Enter the path of the folder to sort: ")
        file_lst = [f for f in os.listdir(direc) if os.path.isfile('/'.join([direc, f]))]
        break
    except:
        print('Invalid folder path! Try again.')

#Phân loại các file
for i in file_lst:
    for key, value in file_types.items():
        if i[i.rfind('.'):] in value:
            shutil.move('/'.join([direc, i]), '/'.join([direc, key, i]))
            
print("Your folder '%s' has been sorted successfully!" % (direc[direc.rfind("\\")+1:]))