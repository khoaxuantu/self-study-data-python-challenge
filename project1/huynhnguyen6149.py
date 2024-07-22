def conv_length(choose_1, choose_2, x):

    switcher = {
        'Meter': 1,
        'Kilometer': 0.001,
        'Centimeter': 100,
        'Milimeter': 1000,
        'Micrometer': 1000000,
        'Nanometer': 1000000000,
        'Mile': 1/1609.35,
        'Yard': 1/0.9144,
        'Foot': 1/0.3048,
        'Inch': 1/0.0254,
        'Light Year': 1/9460660000000000
    }
    return (switcher[choose_2]/switcher[choose_1])*x

def conv_temp(choose_1, choose_2, x):

    if choose_1 == 'Celsius':
        switcher = {
            'Celsius': x,
            'Kelvin': x + 273.15,
            'Fahrenheit': x*1.8 + 32 
    }

    elif choose_1 == 'Kelvin':
        switcher = {
            'Celsius': x - 273.15,
            'Kelvin': x,
            'Fahrenheit': (x - 273.15)*1.8 + 32
    }

    else:
        switcher = {
            'Celsius': (x - 32)/1.8,
            'Kelvin': (x - 32)/1.8 + 273.15,
            'Fahrenheit': x
    }
    return switcher[choose_2]

def conv_area(choose_1, choose_2, x):

    switcher = {
        'Square Meter': 1,
        'Square Kilometer': 0.000001,
        'Square Centimeter': 10000,
        'Square Milirometer': 1000000,
        'Square Micrometer': 1000000000000,
        'Hectare': 0.0001,
        'Square Mile': 1/2589990,
        'Square Yard': 1.1959900463,
        'Square Foot': 10.763910417,
        'Square Inch': 1550.0031,
        'Acre': 1/4046.8564224
    }
    return (switcher[choose_2]/switcher[choose_1])*x

def conv_volume(choose_1, choose_2, x):

    switcher = {
        'Cubic Meter': 1,
        'Cubic Kilometer': 1.E-9,
        'Cubic Centimeter': 1000000,
        'Cubic Milirometer': 1000000000,
        'Liter': 1000,
        'Mililiter': 1000000,
        'US Gallon': 264.17217686,
        'US Quart': 1056.68870743,
        'US Pint': 2113.3774149,
        'US Cup': 4226.7548297,
        'US Fluid Ounce': 33814.038638
    }
    return (switcher[choose_2]/switcher[choose_1])*x

def conv_weight(choose_1, choose_2, x):

    switcher = {
        'Kilogram': 1,
        'Gram': 1000,
        'Miligram': 1000000,
        'Metric Ton': 0.001,
        'Long Ton': 1/1016.04608,
        'Short Ton': 1/907.184,
        'Pound': 1/0.453592,
        'Ounce': 1/0.0283495,
        'Carrat': 5000,
        'Atomic Mass Unit': 6.022136652E+26
    }
    return (switcher[choose_2]/switcher[choose_1])*x

def conv_time(choose_1, choose_2, x):

    switcher = {
        'Second': 60,
        'Milisecond': 60000,
        'Microsecond': 60000000,
        'Nanosecond': 60000000000,
        'Picosecond': 60000000000000,
        'Minute': 1,
        'Hour': 1/3600,
        'Day': 1/86400,
        'Week': 1/604800,
        'Month': 1/2629800,
        'Year': 1/31557600
    }
    return (switcher[choose_2]/switcher[choose_1])*x

# def conv_temp(choose_1, choose_2, x):

print('Physical quantity:')
print('1. Length')
print('2. Temparature')
print('3. Area')
print('4. Volume')
print('5. Weight')
print('6. Time')
choose = int(input('Enter the physical quantity: (1, 2, ... 6): '))
match choose:
    case 1:

        print('Unit of Measurement:')
        print('1.Meter 2.Kilometer 3.Centimeter 4.Milimeter 5.Micrometer')
        print('6.Nanometer 7.Mile 8.Yard 9.Foot 10.Inch 11.Light Year')

        # Please handle invalid input here
        # For instance, I type `1` as input, it still passes through the `conv_length` method, then raises `KeyError`
        choose_1 = str(input('Enter Starting Unit of Measurement: '))
        choose_2 = str(input('Enter Unit of Measurement to Convert to: '))
        x = float(input(f'Enter Starting Measurement in {choose_1}: '))

        print(f'Result: {x} {choose_1} = {conv_length(choose_1, choose_2, x)} {choose_2}')

    case 2:

        print('Unit of Measurement:')
        print('1.Celsius 2.Kelvin 3.Fahrenheit')

        choose_1 = str(input('Enter Starting Unit of Measurement: '))
        choose_2 = str(input('Enter Unit of Measurement to Convert to: '))
        x = float(input(f'Enter Starting Measurement in {choose_1}: '))
        
        print(f'Result: {x} {choose_1} = {conv_temp(choose_1, choose_2, x)} {choose_2}')
    
    case 3:

        print('Unit of Measurement:')
        print('1.Square Meter 2.Square Kilometer 3.Square Centimeter 4.Square Milimeter 5.Square Micrometer')
        print('6.Hectare 7.Square Mile 8. Square Yard 9.Square Foot 10.Square Inch 11.Acre')

        choose_1 = str(input('Enter Starting Unit of Measurement: '))
        choose_2 = str(input('Enter Unit of Measurement to Convert to: '))
        x = float(input(f'Enter Starting Measurement in {choose_1}: '))

        print(f'Result: {x} {choose_1} = {conv_area(choose_1, choose_2, x)} {choose_2}')
    
    case 4:

        print('Unit of Measurement:')
        print('1.Cubic Meter 2.Cubic Kilometer 3.Cubic Centimeter 4.Cubic Milimeter 5.Liter')
        print('6.Mililiter 7.US Gallon 8. US Quart 9.US Pint 10.US Cup 11.US Fluid Ounce')

        choose_1 = str(input('Enter Starting Unit of Measurement: '))
        choose_2 = str(input('Enter Unit of Measurement to Convert to: '))
        x = float(input(f'Enter Starting Measurement in {choose_1}: '))

        print(f'Result: {x} {choose_1} = {conv_volume(choose_1, choose_2, x)} {choose_2}')
    
    case 5:

        print('Unit of Measurement:')
        print('1.Kilogram 2.Gram 3.Miligram 4.Metric Ton 5.Long Ton')
        print('6.Short Ton 7.Pound 8. Ounce 9.Carrat 10.Atomic Mass Unit')

        choose_1 = str(input('Enter Starting Unit of Measurement: '))
        choose_2 = str(input('Enter Unit of Measurement to Convert to: '))
        x = float(input(f'Enter Starting Measurement in {choose_1}: '))

        print(f'Result: {x} {choose_1} = {conv_weight(choose_1, choose_2, x)} {choose_2}')

    case 6:

        print('Unit of Measurement:')
        print('1.Second 2.Milisecond 3.Microsecond 4.Nanosecond 5.Picosecond')
        print('6.Minute 7.Hour 8.Day 9.Week 10.Month 11.Year')

        choose_1 = str(input('Enter Starting Unit of Measurement: '))
        choose_2 = str(input('Enter Unit of Measurement to Convert to: '))
        x = float(input(f'Enter Starting Measurement in {choose_1}: '))

        print(f'Result: {x} {choose_1} = {conv_time(choose_1, choose_2, x)} {choose_2}')

