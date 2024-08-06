import os
import shutil

# Định nghĩa thư mục nguồn và các thư mục đích cho từng loại tệp
thu_muc_nguon = 'D:/Project 3'
thu_muc_dich = {
    'anh': 'D:/Project 3/anh',
    'tai_lieu': 'D:/Project 3/tai_lieu',
    'csv': 'D:/Project 3/csv'
}

# Định nghĩa các phần mở rộng tệp cho từng loại tệp
phan_mo_rong_tep = {
    'anh': ['.jpg', '.jpeg', '.png'],
    'tai_lieu': ['.txt', '.docx'],
    'csv': ['.csv', '.tsv']
}
for duong_dan in thu_muc_dich.values():
    os.makedirs(duong_dan, exist_ok=True)

# Hàm để sắp xếp các tệp vào các thư mục tương ứng
def sap_xep_tep():
    for ten_tep in os.listdir(thu_muc_nguon):
        duong_dan_tep = os.path.join(thu_muc_nguon, ten_tep)
        if os.path.isfile(duong_dan_tep):
            mo_rong = os.path.splitext(ten_tep)[1].lower()
            for loai_tep, mo_rong_danh_sach in phan_mo_rong_tep.items():
                if mo_rong in mo_rong_danh_sach:
                    thu_muc_muc_tieu = thu_muc_dich[loai_tep]
                    shutil.move(duong_dan_tep, os.path.join(thu_muc_muc_tieu, ten_tep))
                    print(f'Đã di chuyển {ten_tep} tới {thu_muc_muc_tieu}')
                    break

# Gọi hàm sap_xep_tep để tổ chức các tệp
sap_xep_tep()
