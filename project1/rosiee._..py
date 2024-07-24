#Nhập giá trị và đơn vị từ người dùng
value = float(input("Nhập giá trị cần chuyển đổi: "))
from_unit = input("Nhập đơn vị ban đầu (Meter, Kilometer, Mile): ")
to_unit = input("Nhập đơn vị muốn chuyển đổi (Meter, Kilometer, Mile): ")

#Thực hiện chuyển đổi
converted_value = None

#Chuyển đổi từ Meter
if from_unit == 'Meter':
    if to_unit == 'Kilometer':
        converted_value = value / 1000
    elif to_unit == 'Mile':
        converted_value = value / 1609.34

#Chuyển đổi từ Kilometer
elif from_unit == 'Kilometer':
    if to_unit == 'Meter':
        converted_value = value * 1000
    elif to_unit == 'Mile':
        converted_value = value / 1.60934

#Chuyển đổi từ Mile
elif from_unit == 'Mile':
    if to_unit == 'Meter':
        converted_value = value * 1609.34
    elif to_unit == 'Kilometer':
        converted_value = value * 1.60934

#In kết quả
if converted_value is not None:
    print(f'{value} {from_unit} = {converted_value} {to_unit}')
else:
    print("Không thể chuyển đổi giữa các đơn vị này.")

#Good job!