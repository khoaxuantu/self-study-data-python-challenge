# Bảng chuyển đổi từ mỗi đơn vị sang meter
conversion_to_meter = {
    'meter': 1,
    'kilometer': 1000,
    'mile': 1609.34,
    'yard': 0.9144,
    'inch': 0.0254,
    'foot': 0.3048
}
# in danh sách các đơn vị tính được hỗ trợ chuyển đổi
unit = list(conversion_to_meter.keys())
print("Danh sách các đơn vị tính được hỗ trợ", unit)

# nhập thông tin đơn vị cần chuển đổi
unit1 = input("Nhập đơn vị 1: ").lower()
unit2 = input("Nhập đơn vị 2: ").lower()
value = float(input("Nhập số quy đổi: "))

# kiểm tra thông tin nhập vào
if unit1 not in conversion_to_meter or unit2 not in conversion_to_meter:
    print("Đơn vị không hợp lệ.")

# Chuyển đổi giá trị từ đơn vị 1 sang meter
unit1_value_in_meter = value * conversion_to_meter[unit1]
# Chuyển đổi giá trị từ meter sang đơn vị 2
converted_value = unit1_value_in_meter / conversion_to_meter[unit2]

print(f"{value} {unit1} = {converted_value} {unit2}")


#Good job!
