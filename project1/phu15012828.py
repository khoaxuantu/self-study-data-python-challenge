# Reviewer: Please handle the out of bound cases
from_m = input("Enter Starting unit of Measurement(meter, kilometer, centimeter, mile, yard, foot):")
convert_m = input("Enter Unit of Measurement to Convert to(meter, kilometer, centimeter, mile, yard, foot):")
start_m = input("Enter Starting Measurement in :")

## convert starting unit to meter
to_meters = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048
    }
start_m_in_meters = float(start_m) * to_meters[from_m]

## convert that value to wanted measuremetn
result = 0.0
if convert_m == 'meter':
    result = float(start_m_in_meters)
    print(f"Result: {start_m} {from_m} = {result} {convert_m}")  
elif convert_m == 'kilometer':
    result = float(start_m_in_meters) * 0.001
    print(f"Result: {start_m} {from_m} = {result} {convert_m}")  
elif convert_m == 'centimeter':
    result = float(start_m_in_meters) * 100
    print(f"Result: {start_m} {from_m} = {result} {convert_m}")  
elif convert_m == 'mile':
    result = float(start_m_in_meters) * 0.0006213689
    print(f"Result: {start_m} {from_m} = {result} {convert_m}")  
elif convert_m == 'yard':
    result = float(start_m_in_meters) * 1.0936132983
    print(f"Result: {start_m} {from_m} = {result} {convert_m}")  
elif convert_m == 'foot':
    result = float(start_m_in_meters) * 3.280839895
    print(f"Result: {start_m} {from_m} = {result} {convert_m}")

