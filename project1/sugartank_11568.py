starting_unit = input('Enter starting unit of measurement (inches, feet, yards): ')
target_unit = input('Enter target unit of measurement (inches, feet, yards): ')
measurement = float(input('Enter starting measurement in ' + starting_unit + ': '))

conversion_factors = {'inches': 1, 'feet': 12, 'yards': 36}

if starting_unit in conversion_factors and target_unit in conversion_factors:
    result = measurement * (conversion_factors[starting_unit] / conversion_factors[target_unit])
    print(f'{measurement} {starting_unit} is equal to {result} {target_unit}.')
else:
    print('Invalid units. Please enter inches, feet, or yards for both starting and target units.')

#Nice job!