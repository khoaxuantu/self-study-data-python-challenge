def measurement_converter(starting_unit, converting_unit, starting_number):
    conversions = {
        ('inches', 'feet'): starting_number * 0.0833333333,
        ('feet', 'inches'): starting_number * 12,
        ('inches', 'yards'): starting_number * 0.0277777778,
        ('yards', 'inches'): starting_number * 36,
        ('feet', 'yards'): starting_number * 0.333333333,
        ('yards', 'feet'): starting_number * 3,
        ('kilometers', 'meters'): starting_number * 1000,
        ('meters', 'kilometers'): starting_number / 1000,
        ('kilometers', 'centimeters'): starting_number * 100000,
        ('centimeters', 'kilometers'): starting_number / 100000,
        ('meters', 'centimeters'): starting_number * 100,
        ('centimeters', 'meters'): starting_number / 100,
        ('centimeters', 'inches'): starting_number * 0.393701,
        ('inches', 'centimeters'): starting_number / 0.393701,
        ('centimeters', 'feet'): starting_number * 0.0328084,
        ('feet', 'centimeters'): starting_number / 0.0328084,
        ('centimeters', 'yards'): starting_number * 0.0109361,
        ('yards', 'centimeters'): starting_number / 0.0109361,
        ('meters', 'inches'): starting_number * 39.3701,
        ('inches', 'meters'): starting_number / 39.3701,
        ('meters', 'feet'): starting_number * 3.28084,
        ('feet', 'meters'): starting_number / 3.28084,
        ('meters', 'yards'): starting_number * 1.09361,
        ('yards', 'meters'): starting_number / 1.09361,
        ('kilometers', 'inches'): starting_number * 39370.1,
        ('inches', 'kilometers'): starting_number / 39370.1,
        ('kilometers', 'feet'): starting_number * 3280.84,
        ('feet', 'kilometers'): starting_number / 3280.84,
        ('kilometers', 'yards'): starting_number * 1093.61,
        ('yards', 'kilometers'): starting_number / 1093.61
    }

    if (starting_unit, converting_unit) in conversions:
        result = conversions[(starting_unit, converting_unit)]
        rounded_result = round(result, 2)
        return f"Result: {starting_number} {starting_unit} = {rounded_result} {converting_unit}"
    else:
        return f"Conversion from {starting_unit} to {converting_unit} is not supported."


while True:
    print("Enter 'stop' to end")
    starting_unit = input('Enter starting unit of measurement (inches, feet, yards, kilometers, meters, centimeters): ')

    if starting_unit == 'stop':
        break
   
    
    print(f"Please do not enter converting unit of measurement the same as {starting_unit}.")
    converting_unit = input('Enter unit of measurement to convert to (inches, feet, yards, kilometers, meters, centimeters): ')
    if converting_unit == 'stop':
        break
        
    starting_number = float(input(f'Enter starting measurement in {starting_unit}s: '))
    if starting_number == 'stop':
        break

    measurement_converter_result = measurement_converter(starting_unit, converting_unit, starting_number)
    print(measurement_converter_result)

# Reviewer: Noice! You overkill it :)

