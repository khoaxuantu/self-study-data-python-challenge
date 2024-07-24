convert = {'Meter':1.0, 'Kilometer':1000.0, 'Centimeter':0.01, 'Millimeter':0.001, 'Micrometer':0.000001, 'Nanometer':0.000000001}

from_unit = str(input('Enter Unit of Measurement(Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ')).capitalize()
to_unit = str(input('Enter Unit of Measurement to Convert to(Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ')).capitalize()

#Check valid unit, print result
if from_unit in convert and to_unit in convert:
    value = float(input('Enter Value to Convert ' + from_unit+ ': '))
    result = value*convert[from_unit]/convert[to_unit]
    print('Result:',str(value), from_unit, '=', str(result), to_unit)
else:
    print('Unit is not available, try again!')

# Reviewer: Noice

