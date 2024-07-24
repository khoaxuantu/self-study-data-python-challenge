def convert_units():
    print("\n LENGTH CONVERTER\n")

    conversion_factors = {
            'meters': 1,
            'kilometers': 0.001,
            'centimeters': 100,
            'millimeters': 1000,
            'miles': 0.000621371,
            'yards': 1.09361,
            'feet': 3.28084,
            'inches': 39.3701
        }
    
    print('Available units of Length:  ') 
    print('meters, kilometers, centimeters, millimeters, miles, yards, feet, inches ')
    print('_____________________________\n')
    value = float(input("Nhập giá trị cần chuyển đổi: "))
    from_unit = input("Nhập đơn vị gốc: ").lower()
    to_unit = input("Nhập đơn vị đích: ").lower()

    if from_unit in conversion_factors and to_unit in conversion_factors:
        result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    
    else:
        raise ValueError("Unsupported unit conversion")
    
    print('_____________________________\n')

    print(f"Result: {value} {from_unit} = {result} {to_unit}")


convert_units()

#Gud job! You nailed it