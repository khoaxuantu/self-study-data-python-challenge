def tinh_toan(bieu_thuc):
    if ' / 0' in bieu_thuc or '/0' in bieu_thuc:
        return "Lỗi! Chia cho số không."
    # Các kiểm tra khác có thể được thêm vào đây
    
    # Thực hiện tính toán
    ket_qua = eval(bieu_thuc)
    return ket_qua

def tinh_toan_lien_tuc():
    print("Máy tính!")
    ket_qua = None

    while True:
        print("\nChọn một tùy chọn:")
        print("1. Nhập biểu thức toán học (tiếp tục với kết quả trước)")
        print("2. Nhập biểu thức toán học mới")
        print("3. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn (1-3): ")

        if lua_chon == '3':
            print("Thoát khỏi máy tính.")
            break

        if lua_chon == '1':
            if ket_qua is not None:
                bieu_thuc = input(f"Kết quả trước: {ket_qua}\nTiếp tục với (VD: + 6): ")
                if bieu_thuc.startswith(('+', '-', '*', '/', '%')):
                    bieu_thuc = str(ket_qua) + bieu_thuc
            else:
                print("Chưa có kết quả trước đó. Vui lòng chọn tùy chọn khác.")
                continue

        elif lua_chon == '2':
            bieu_thuc = input("Nhập biểu thức mới: ")

        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
            continue

        if bieu_thuc.lower() in ['exit', 'quit']:
            print("Thoát khỏi máy tính.")
            break

        ket_qua = tinh_toan(bieu_thuc)
        print(f"Kết quả: {ket_qua}")


tinh_toan_lien_tuc()
