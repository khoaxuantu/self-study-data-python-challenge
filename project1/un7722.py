from_unit = input("Nhập đơn vị chiều dài của bạn (km, hm, dam, m, dm, cm, mm): ")
to_unit = input("Đơn vị bạn muốn chuyển thành là (km, hm, dam, m, dm, cm, mm): ")   
value = float(input('Nhập giá trị bạn muốn chuyển nhé: '))

units = {
    'm': 1,
    'km': 1000,
    'hm': 100,
    'dam': 10,
    'dm': 0.1,
    'cm': 0.01,
    'mm': 0.001
}

if from_unit not in units or to_unit not in units:
    print("Đơn vị bạn nhập không có, vui lòng nhập các đơn vị thuộc km, hm, dam, m, dm, cm, mm")
else:
    convert_value_to_meters = value * units[from_unit]
    convert_to_required_unit = convert_value_to_meters / units[to_unit]
    print(f"{value} {from_unit} = {convert_to_required_unit} {to_unit}")


#Gud job -.-!
