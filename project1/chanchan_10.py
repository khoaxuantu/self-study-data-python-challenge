from_units = input('Enter Starting Unit of Measurement (m, cm, mm, inches, feet): ').strip().lower()
to_units = input('Enter Unit of Measurement to Convert to (m, cm, mm, inches, feet): ').strip().lower()
number = float(input(f'Enter Starting Measurement in {from_units}: '))

def m2cm(number): 
    return number * 100

def m2mm(number): 
    return number * 1000

def m2inches(number): 
    return number * 39.37007874

def m2feet(number): 
    return number * 3.280839895

def cm2m(number): 
    return number / 100

def cm2mm(number): 
    return number * 10

def cm2inches(number): 
    return number * 0.3937007874

def cm2feet(number): 
    return number * 0.032808399

def mm2m(number): 
    return number / 1000

def mm2cm(number): 
    return number / 10

def mm2inches(number): 
    return number * 0.03937007874

def mm2feet(number): 
    return number * 0.003280839895

def inches2m(number): 
    return number / 39.37007874

def inches2cm(number): 
    return number / 0.3937007874

def inches2mm(number): 
    return number / 0.03937007874

def inches2feet(number): 
    return number / 12

def feet2m(number): 
    return number / 3.280839895

def feet2cm(number): 
    return number / 0.032808399

def feet2mm(number): 
    return number / 0.003280839895

def feet2inches(number): 
    return number * 12

if from_units == 'm':
    if to_units == 'cm':
        result = m2cm(number)
    elif to_units == 'mm':
        result = m2mm(number)
    elif to_units == 'inches':
        result = m2inches(number)
    elif to_units == 'feet':
        result = m2feet(number)
    else:
        result = None
elif from_units == 'cm':
    if to_units == 'm':
        result = cm2m(number)
    elif to_units == 'mm':
        result = cm2mm(number)
    elif to_units == 'inches':
        result = cm2inches(number)
    elif to_units == 'feet':
        result = cm2feet(number)
    else:
        result = None
elif from_units == 'mm':
    if to_units == 'm':
        result = mm2m(number)
    elif to_units == 'cm':
        result = mm2cm(number)
    elif to_units == 'inches':
        result = mm2inches(number)
    elif to_units == 'feet':
        result = mm2feet(number)
    else:
        result = None
elif from_units == 'inches':
    if to_units == 'm':
        result = inches2m(number)
    elif to_units == 'cm':
        result = inches2cm(number)
    elif to_units == 'mm':
        result = inches2mm(number)
    elif to_units == 'feet':
        result = inches2feet(number)
    else:
        result = None
elif from_units == 'feet':
    if to_units == 'm':
        result = feet2m(number)
    elif to_units == 'cm':
        result = feet2cm(number)
    elif to_units == 'mm':
        result = feet2mm(number)
    elif to_units == 'inches':
        result = feet2inches(number)
    else:
        result = None
else:
    result = None

if result is not None:
    print(f'{number} {from_units} is equal to {result} {to_units}')
else:
    print('Error.')

#Good job overall! However, you can shorten your code by many ways, for example: using conversion factors as follow:
'''
def unit_conversion (unit_in, value, unit_out):
    convert_dict = {"gram":1.00,"kilogram":1000.00, "ounce":28.3495}
    value_converted = value*convert_dict[unit_in]/convert_dict[unit_out]
    return value_converted
'''