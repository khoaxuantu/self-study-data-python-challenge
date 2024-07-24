print('SPEECH CONVERTING PROGRAMMING\n')

unit_list = ['m/s', 'km/h', 'm/h', 'km/s', 'mm/h', 'cm/s']

unit1 = input('Enter Starting Unit of Measurement (m/s, km/h, m/h, km/s, mm/h, cm/s): ')
while unit1 not in unit_list:
    print('The unit does not include in the available unit list.')
    unit1 = input('Please enter the Starting Unit of Measurement again: ')
    
unit2 = input('Enter Unit of Measurement to Convert to (m/s, km/h, m/h, km/s, mm/h, cm/s): ')
while unit2 not in unit_list:
    print('The unit does not include in the available unit list.')
    unit2 = input('Please enter the Unit of Measurement to Convert to again: ')
    
value = float(input('Enter Starting Measurement in ' + unit1 + ': '))

speech_converter_dictionary = {
    'm/s': {'km/h': 3.6, 'm/h': 3600, 'km/s': 0.001, 'mm/h':3600000, 'cm/s': 100, 'm/s': 1},
    'km/h': {'m/s': 0.2777777778, 'm/h': 1000, 'km/s': 0.0002777778, 'mm/h':1000000, 'cm/s': 27.777777778, 'km/h': 1},
    'm/h': {'m/s': 0.0002777778, 'km/h': 0.001, 'km/s': 2.777777777E-7, 'mm/h': 1000, 'cm/s': 0.0277777778, 'm/h': 1},
    'km/s': {'m/s': 1000, 'km/h': 3600, 'm/h': 3600000, 'mm/h':3600000000, 'cm/s': 100000, 'km/s': 1},
    'mm/h': {'m/s': 2.777777777E-7, 'km/h': 0.000001, 'm/h': 0.001, 'km/s':2.777777777E-10, 'cm/s': 0.0000277778, 'mm/h': 1},
    'cm/s': {'m/s': 0.01, 'km/h': 0.036, 'm/h': 36, 'mm/h':36000, 'km/s': 0.00001, 'cm/s': 1}
}

convert = value * speech_converter_dictionary[unit1][unit2]

print('Result:', value, unit1, '=', convert, unit2)

#Nice work!!