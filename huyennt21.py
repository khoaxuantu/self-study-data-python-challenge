# Dictionary for unit conversions
Conversion = {
    'Length': {
        'Meter': 1, 
        'Kilometer': 0.001, 
        'Centimeter': 100, 
        'Millimeter': 1000, 
        'Micrometer': 1000000, 
        'Nanometer': 1000000000, 
        'Mile': 0.0006213689, 
        'Yard': 1.0936132983, 
        'Foot': 3.280839895,  
        'Inch': 39.37007874, 
        'Light Year': 1.057008707 * 10**(-16)
    },
    'Temperature': {
        'Celsius': 1, 
        'Kelvin': 274.15, 
        'Fahrenheit': 33.8
    },
    'Area': {
        'Square Meter': 1, 
        'Square Kilometer': 0.000001, 
        'Square Centimeter': 10000, 
        'Square Millimeter': 1000000, 
        'Square Micrometer': 1000000000000, 
        'Hectare': 0.0001, 
        'Square Mile': 3.861018768 * 10**(-7), 
        'Square Yard': 1.1959900463, 
        'Square Foot': 10.763910417, 
        'Square Inch': 1550.0031, 
        'Acre': 0.0002471054
    },
    'Volume': {
        'Cubic Meter': 1, 
        'Cubic Kilometer': 10**(-9), 
        'Cubic Centimeter': 1000000, 
        'Cubic Millimeter': 1000000000, 
        'Liter': 1000, 
        'Milliliter': 1000000, 
        'US Gallon': 264.17217686, 
        'US Quart': 1056.6887074, 
        'US Pint': 2113.3774149, 
        'US Cup': 4226.7548297, 
        'US Fluid Ounce': 33814.038638
    },
    'Weight': {
        'Kilogram': 1, 
        'Gram': 1000, 
        'Milligram': 1000000, 
        'Metric Ton': 0.001, 
        'Long Ton': 0.0009842073, 
        'Short Ton': 0.0011023122, 
        'Pound': 2.2046244202, 
        'Ounce': 35.273990723, 
        'Carrat': 5000, 
        'Atomic Mass Unit': 6.022136652 * 10**(26)
    },
    'Time': {
        'Second': 1, 
        'Millisecond': 1000, 
        'Microsecond': 1000000, 
        'Nanosecond': 1000000000, 
        'Picosecond': 1000000000000, 
        'Minute': 0.0166666667, 
        'Hour': 0.0002777778, 
        'Day': 0.0000115741, 
        'Week': 0.0000016534, 
        'Month': 3.802570537 * 10**(-7), 
        'Year': 3.168808781 * 10**(-8)
    }
}

# Display available conversion types
print(f'TYPES OF CONVERSIONS: {", ".join(Conversion.keys())}')

# Prompt user to choose a type of conversion and validate input
while True:
    unit_type = input('Choose type of conversion: ')
    if unit_type in Conversion.keys():
        break
    else:
        print('Choose a type of conversion in list TYPES OF CONVERSIONS above!!!')

# Display available units for the chosen conversion type
print(f'LIST OF UNITS: {", ".join(Conversion[unit_type].keys())}')

# Prompt user to choose the unit to convert from and validate input
while True:
    from_unit = input('Choose from_unit: ')
    if from_unit in Conversion[unit_type].keys():
        break
    else:
        print('Choose from_unit in LIST OF UNITS above!!!')

# Prompt user to choose the unit to convert to and validate input
while True:
    to_unit = input('Choose to_unit: ')
    if to_unit in Conversion[unit_type].keys():
        break
    else:
        print('Choose to_unit in LIST OF UNITS above!!!')

# Prompt the user to enter the value to convert and validate input
while True:
    try:    
        from_unit_value = float(input('Enter value to convert: '))
        break
    except:
        print('Enter a integer or a float value!!!')

# Calculate the converted value
if unit_type == 'Temperature':
    if from_unit == 'Celsius' and to_unit == 'Kelvin':
        to_unit_value = from_unit_value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        to_unit_value = from_unit_value - 273.15
    elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        to_unit_value = (from_unit_value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        to_unit_value = (from_unit_value - 32) * 5/9
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        to_unit_value = (from_unit_value - 273.15) * 9/5 + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        to_unit_value = (from_unit_value - 32) * 5/9 + 273.15
else:
    to_unit_value = from_unit_value * Conversion[unit_type][to_unit] / Conversion[unit_type][from_unit]

# Print the result of the conversion
print(f'{from_unit_value} {from_unit} = {to_unit_value} {to_unit}')


#Good job!! You nailed it!