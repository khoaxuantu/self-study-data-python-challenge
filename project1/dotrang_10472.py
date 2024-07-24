def convert_length(value, from_unit, to_unit):
    units = {
        'millimeter': 1,
        'centimeter': 10,
        'meter': 1000,
        'kilometer': 1000000,
        'micrometer': 0.001,
        'nanometer': 0.000001,
        'mile': 16093540,
        'yard': 914.4,
        'foot': 304.8,
        'inch': 25.4,
        'light_year': 9460660000000000000
    }
    if from_unit not in units or to_unit not in units:
        return 'Invalid unit'
    value_in_millimeter = value * units[from_unit]
    converted_value = value_in_millimeter / units[to_unit]
    return converted_value
while True:
    try:
        value = float(input('import value: ')) 
    except ValueError:
        print('Invalid value. Please enter number.')
        continue
    from_unit = input('Enter Starting Unit of Measurement (millimeter, centimeter, meter, kilometer, micrometer, nanometer, mile, yard, foot, inch, light year ): ').lower()
    to_unit = input('Enter  Unit of Measurement to Convert to (millimeter, centimeter, meter, kilometer, micrometer, nanometer, mile, yard, foot, inch, light year ): ').lower()
    
    result = convert_length(value, from_unit, to_unit)
    
    if isinstance(result, str): 
        print(result)
    else:
        print(f'Result: {result}{to_unit}')
    
    cont = input('Do you want to make another conversion? (yes/no): ').lower()
    if cont != 'yes':
        break

# Reviewer: Nice try :) Would be better if you make your standard outputs prettier

