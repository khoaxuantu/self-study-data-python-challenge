#Nhập đơn vị ban đầu
from_unit = input("Nhập đơn vị ban đầu (kg, g, mg, ton, lbs, oz): ")
#Nhập đơn vị muốn chuyển đổi
to_unit = input("Nhập đơn vị muốn chuyển đổi (kg, g, mg, ton, lbs, oz): ")
#Nhập giá trị muốn chuyển đổi
value = float(input("Nhập giá trị muốn chuyển đổi: "))
#Gán giá trị cho các hệ số chuyển đổi:
conversion_factors = {
        'kg': 1,
        'g': 1000,
        'mg': 1000000,
        'ton': 0.001,
        'lbs': 2.2046226218,
        'oz': 35.27396195}
#Hệ số chuyển đổi đơn vị:
conversion_rate = conversion_factors[to_unit]/conversion_factors[from_unit]
#Chuyển giá trị sang đơn vị muốn chuyển đổi
converted_value = value * conversion_rate
#In kết quả
print(value, from_unit, "=", converted_value, to_unit)

#Good job!