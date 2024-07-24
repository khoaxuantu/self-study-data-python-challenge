units = ['Meter', 'Kilometer', 'Centimeter']
while True:
    unit = input('Enter Starting Unit of Measurement(Meter, Kilometer, Centimeter): ')
    if unit in units: break
    else: print('\nWrong unit. Please enter again!')
while True:
    unit_to_convert = input('Enter Unit of Measurement to Convert to(Meter, Kilometer, Centimeter): ')
    if unit_to_convert in units: break
    else: print('\nWrong unit. Please enter again!')
val = int(input(f'Enter Starting Measurement in {unit}: ')) #Using int() here cause the error if the user want to convert between decimal measurementes.
if unit == 'Meter':
    if unit_to_convert == 'Meter': result = val
    elif unit_to_convert == 'Kilometer': result = 0.001*val
    else: result = 100*val
elif unit == 'Kilometer':
    if unit_to_convert == 'Meter': result = 1000*val
    elif unit_to_convert == 'Kilometer': result = val
    else: result = 100000*val
else:
    if unit_to_convert == 'Meter': result = 0.01*val
    elif unit_to_convert == 'Kilometer': result = 0.00001*val
    else: result = val
print(f'Result: {val} {unit} = {result} {unit_to_convert}')

#Overal, good job!