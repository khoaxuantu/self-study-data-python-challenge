units = {'Meter': 1, 'Kilometer': 1000, 'Centimeter': 0.01, 'Millimeter': 0.001, 'Mile': 1609.35, 'Foot': 0.3048}

check = False
while check == False:
    start_unit = input('Enter starting unit of measurement(Meter, Kilometer, Centimeter, Millimeter, Mile, Foot): ')
    converted_unit = input('Enter unit of measurement to convert to(Meter, Kilometer, Centimeter, Millimeter, Mile, Foot): ')
    start_unit = start_unit.capitalize()
    converted_unit = converted_unit.capitalize()
    input_value = float(input('Enter starting measurement in ' + start_unit + ': '))

    if start_unit in units and converted_unit in units:
        converted_value = input_value * units[start_unit] / units[converted_unit]
        print('Result: ', input_value, start_unit, '=', converted_value, converted_unit)
    else:
        print('Invalid unit of measurement, please try again')
        continue
    
    try_again = input('Would you like to convert another measurement? (y/n): ')
    if try_again == 'n':
        check = True
    else:
        continue
    
# Noice

