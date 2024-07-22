# Bảng đơn vị tính bằng mét
bang_don_vi = {
    'meters': 1.0,
    'kilometers': 1000.0,
    'centimeters': 0.01,
    'millimeters': 0.001,
    'miles': 1609.34,
    'yards': 0.9144,
    'feet': 0.3048,
    'inches': 0.0254
}

print("Chuyển đổi đơn vị độ dài")

# Kiểm tra và nhập giá trị
while True:
    gia_tri = float(input("Nhập giá trị cần chuyển đổi: "))
    if gia_tri >= 0:
        break
    print("Giá trị phải là số dương. Vui lòng nhập lại.")
    

# Kiểm tra và nhập đơn vị gốc
while True:
    don_vi_goc = input("Nhập đơn vị gốc (meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ").lower()
    if don_vi_goc in bang_don_vi:
        break
    else:
        print("Đơn vị gốc không hợp lệ. Vui lòng nhập lại.")

# Kiểm tra và nhập đơn vị đích
while True:
    don_vi_dich = input("Nhập đơn vị đích (meters, kilometers, centimeters, millimeters, miles, yards, feet, inches): ").lower()
    if don_vi_dich in bang_don_vi:
        break
    else:
        print("Đơn vị đích không hợp lệ. Vui lòng nhập lại.")

# Chuyển đổi giá trị về mét
gia_tri_met = gia_tri * bang_don_vi[don_vi_goc]

# Chuyển đổi từ mét sang đơn vị đích
ket_qua = gia_tri_met / bang_don_vi[don_vi_dich]

print(f"{gia_tri} {don_vi_goc} = {ket_qua} {don_vi_dich}")

# :)

