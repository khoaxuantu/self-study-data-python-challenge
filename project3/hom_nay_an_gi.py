import os 
import shutil

def sap_xep(thu_muc_goc, loai_tep):
    for tep in os.listdir(thu_muc_goc):
        link_tep = os.path.join(thu_muc_goc, tep)
        if os.path.isfile(link_tep):
            duoi_tep = os.path.splitext(tep)[1].lower()
            for thu_muc, phan_duoi in loai_tep.items():
                if duoi_tep in phan_duoi:
                    duong_dan_dich = os.path.join(thu_muc_goc, thu_muc)
                    os.makedirs(duong_dan_dich, exist_ok=True)
                    shutil.move(link_tep, duong_dan_dich)
                    break
loai_tep = {
    'thuc_thi' : ['.exe'],
    'nen' : ['.zip', '.7z'],
    'hinh_anh' : ['.jpg', '.gif'], 
    'am_thanh' : ['.mp3', '.wav'], 
    'video' : ['.mp4', '.mov'],
    'tai_lieu' : ['.txt', '.doc', '.pdf'], 
}
thu_muc_goc = r'C:\Folder_goc'
sap_xep(thu_muc_goc, loai_tep) #hay sap xep cac tep vao tung loai thu muc

# Review:
'''
Error Handling: Implement error handling for file operations to handle cases where files cannot be moved due to permission issues or existing files.
Efficiency: Optimize the process by checking for existing folders (os.path.exists()) only once for each file type rather than within the loop.
Case Sensitivity: Ensure the file extension check is case-insensitive by consistently converting the extensions to lowercase.
'''
