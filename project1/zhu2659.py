#Good work. However, you can try take one unit as the base and change other units based on it. For example:
'''
conversion_factors = {
    'meter': 1,
    'kilometer': 1e3,
    'nanometer': 1e9
}
...
value = measurement / conversion_factors[start_unit]
result = value * conversion_factors[target_unit]
'''

conversion_factors = {
    'inches': {'feet': 1/12, 'yards': 1/36, 'meters': 0.0254, 'kilometers': 0.0000254, 'centimeters': 2.54, 'millimeters': 25.4, 'micrometers': 25400, 'nanometers': 25400000, 'miles': 1/63360},
    'feet': {'inches': 12, 'yards': 1/3, 'meters': 0.3048, 'kilometers': 0.0003048, 'centimeters': 30.48, 'millimeters': 304.8, 'micrometers': 304800, 'nanometers': 304800000, 'miles': 1/5280},
    'yards': {'inches': 36, 'feet': 3, 'meters': 0.9144, 'kilometers': 0.0009144, 'centimeters': 91.44, 'millimeters': 914.4, 'micrometers': 914400, 'nanometers': 914400000, 'miles': 1/1760},
    'meters': {'inches': 39.3701, 'feet': 3.28084, 'yards': 1.09361, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'micrometers': 1000000, 'nanometers': 1000000000, 'miles': 0.000621371},
    'kilometers': {'inches': 39370.1, 'feet': 3280.84, 'yards': 1093.61, 'meters': 1000, 'centimeters': 100000, 'millimeters': 1000000, 'micrometers': 1000000000, 'nanometers': 1000000000000, 'miles': 0.621371},
    'centimeters': {'inches': 0.393701, 'feet': 0.0328084, 'yards': 0.0109361, 'meters': 0.01, 'kilometers': 0.00001, 'millimeters': 10, 'micrometers': 10000, 'nanometers': 10000000, 'miles': 0.0000062137},
    'millimeters': {'inches': 0.0393701, 'feet': 0.00328084, 'yards': 0.00109361, 'meters': 0.001, 'kilometers': 0.000001, 'centimeters': 0.1, 'micrometers': 1000, 'nanometers': 1000000, 'miles': 0.000000621371},
    'micrometers': {'inches': 0.0000393701, 'feet': 0.00000328084, 'yards': 0.00000109361, 'meters': 0.000001, 'kilometers': 0.000000001, 'centimeters': 0.0001, 'millimeters': 0.001, 'nanometers': 1000, 'miles': 0.000000000621371},
    'nanometers': {'inches': 0.0000000393701, 'feet': 0.00000000328084, 'yards': 0.00000000109361, 'meters': 0.000000001, 'kilometers': 0.000000000001, 'centimeters': 0.0000001, 'millimeters': 0.000001, 'micrometers': 0.001, 'miles': 0.000000000000621371},
    'miles': {'inches': 63360, 'feet': 5280, 'yards': 1760, 'meters': 1609.34, 'kilometers': 1.60934, 'centimeters': 160934, 'millimeters': 1609340, 'micrometers': 1609340000, 'nanometers': 1609340000000},
}

def convert_units(start_unit, target_unit, measurement):
    if start_unit == target_unit:
        return measurement
    if start_unit in conversion_factors and target_unit in conversion_factors[start_unit]:
        return measurement * conversion_factors[start_unit][target_unit]
    error_message = f"Không thể chuyển đổi từ {start_unit} sang {target_unit}."
    raise ValueError(error_message)

def main():
    start_unit = input("Nhập đơn vị bắt đầu (inches, feet, yards): ") #Why don't you write all the available converted units?
    target_unit = input("Nhập đơn vị đích (inches, feet, yards): ")
    measurement = float(input(f"Nhập giá trị cần chuyển đổi (đơn vị {start_unit}): "))
    
    result = convert_units(start_unit, target_unit, measurement)
    print(f"Kết quả: {measurement} {start_unit} = {result} {target_unit}")