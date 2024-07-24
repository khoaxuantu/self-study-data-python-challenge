conversion = {'nanometer': 1e-9, 'micrometer': 1e-6, 'millimeter': 1e-3, 'centimeter': 1e-2, 'meter': 1, 'kilometer': 1e3}

# Get user input for starting unit
start_unit = input('Enter starting unit of measurement (nanometer, micrometer, millimeter, centimeter, meter, kilometer): ')
while start_unit not in conversion.keys():
    start_unit = input('Invalid value. Enter starting unit of measurement again: ')

# Get user input for unit to convert to
convert_unit = input('Enter unit of measurement to convert to (nanometer, micrometer, millimeter, centimeter, meter, kilometer): ')
while convert_unit not in conversion.keys():
    convert_unit = input('Invalid value. Enter converting unit of measurement again: ')

# Get user input for the number of start units
value = float(input(f'Enter the number of {start_unit}: '))

# Perform conversion
converting_value = value * conversion[start_unit] / conversion[convert_unit]

# Handle pluralization for output
start_unit_plural = start_unit if value == 1 else start_unit + 's'
convert_unit_plural = convert_unit if converting_value == 1 else convert_unit + 's'

# Print result
print(f'Result: {value} {start_unit_plural} = {converting_value} {convert_unit_plural}')

#Great job!