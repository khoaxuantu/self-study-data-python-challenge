units = input('Choose the units (meter/kilometer/centimeter/milimeter): ')
to_unit = input('Enter the to_units (meter/kilometer/centimeter/milimeter): ')
to_value = None
if to_unit == units:
    d = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'milimeter': 1000
    }
    from_unit = input('Enter the unit you want to convert: ')
    from_value = float(input('Enter value of unit you want to convert: '))
    to_value = (from_value*1)/d[from_unit]
    print(f'from {from_value}/{from_unit} to {to_value}/{to_unit}')
elif to_unit == units:
    d = {
        'meter': 1000,
        'kilometer': 1,
        'centimeter': 100000,
        'milimeter': 1000000
    }
    from_unit = input('Enter the unit you want to convert: ')
    from_value = float(input('Enter value of unit you want to convert: '))
    to_value = (from_value*1)/d[from_unit]
    print(f'from {from_value}/{from_unit} to {to_value}/{to_unit}')
elif to_unit == units:
    d = {
        'meter': 0.01,
        'kilometer': 0.0001,
        'centimeter': 1,
        'milimeter': 10
    }
    from_unit = input('Enter the unit you want to convert: ')
    from_value = float(input('Enter value of unit you want to convert: '))
    to_value = (from_value*1)/d[from_unit]
    print(f'from {from_value}/{from_unit} to {to_value}/{to_unit}')
elif to_unit == units:
    d = {
        'meter': 0.001,
        'kilometer': 0.000001,
        'centimeter': 0.1,
        'milimeter': 1
    }
    from_unit = input('Enter the unit you want to convert: ')
    from_value = float(input('Enter value of unit you want to convert: '))
    to_value = (from_value*1)/d[from_unit]
    print(f'from {from_value}/{from_unit} to {to_value}/{to_unit}')

# example
# units = 'meter'
# to_unit = 'meter'
# from_unit = 'kilometer'
# from_value = 2
# output = from 2.0/kilometer to 2000.0/meter

###Comment:
# Overall, great job! 
# However, I am not fully understand your intention of creating the units and to_units variable. It may cause confusion for other users as well.
# You can improve your program by taking 2 inputs only: from_unit and to_unit