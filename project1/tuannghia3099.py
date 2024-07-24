# Project - tuannghia3099
starting_unit = input('Enter Starting Unit of Measurement (meter, kilometer, centimeter, millimeter, micrometer): ')
converted_unit = input('Enter Unit of Measurement to Convert to (meter, kilometer, centimeter, millimeter, micrometer): ')
starting_value = int(input('Enter Starting Measurement in ' + str(starting_unit) + ':'))

if starting_unit == 'meter':
    if converted_unit == 'kilometer':
        result = starting_value * 0.001
    elif converted_unit == 'centimeter':
        result = starting_value * 100
    elif converted_unit == 'millimeter':
        result = starting_value * 1000
    elif converted_unit == 'meter':
        result = starting_value * 1
    else:
        result = starting_value * 1000000
elif starting_unit == 'kilometer':
    if converted_unit == 'meter':
        result = starting_value * 1000
    elif converted_unit == 'centimeter':
        result = starting_value * 100000
    elif converted_unit == 'millimeter':
        result = starting_value * 1000000
    elif converted_unit == 'kilometer':
        result = starting_value * 1
    else:
        result = starting_value * 1000000000
elif starting_unit == 'centimeter':
    if converted_unit == 'meter':
        result = starting_value * 0.01
    elif converted_unit == 'kilometer':
        result = starting_value * 0.00001
    elif converted_unit == 'millimeter':
        result = starting_value * 10
    elif converted_unit == 'centimeter':
        result = starting_value * 1
    else:
        result = starting_value * 10000
elif starting_unit == 'millimeter':
    if converted_unit == 'meter':
        result = starting_value * 0.001
    elif converted_unit == 'centimeter':
        result = starting_value * 0.1
    elif converted_unit == 'kilometer':
        result = starting_value * 0.000001
    elif converted_unit == 'millimeter':
        result = starting_value * 1
    else:
        result = starting_value * 1000
else:
    if converted_unit == 'meter':
        result = starting_value * 0.000001
    elif converted_unit == 'centimeter':
        result = starting_value * 0.0001
    elif converted_unit == 'kilometer':
        result = starting_value * 9.999999999E-10
    elif converted_unit == 'micrometer':
        result = starting_value * 1
    else:
        result = starting_value * 0.001

print('Result: ' + str(starting_value) + ' ' + str(starting_unit) + ' = ' + str(result) + ' ' + str(converted_unit))

#Good work!