exchange_rates = {
    'Kilometer': 1000,
    'Meter': 1,
    'Centimeter': 0.01, 
    'Millimeter': 0.001,
    'Micrometer': 0.000001,
    'Nanometer': 0.000000001
    }

source_unit = input(f'Nhập đơn vị cần chuyển đổi ({', '.join(exchange_rates.keys())}): ')
dest_unit = input(f'Nhập đơn vị muốn chuyển đổi ({', '.join(exchange_rates.keys())}): ')
original_value = float(input(f'Nhập giá trị muốn chuyển đổi (từ {source_unit} thành {dest_unit}): '))

converted_value = original_value*exchange_rates[source_unit]/exchange_rates[dest_unit]
    
print(f'Kết quả {original_value} {source_unit} = {converted_value} {dest_unit}')

#Good job!