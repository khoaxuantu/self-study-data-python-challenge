def Unit_Converter_Temp(from_unit, to_unit, unit_value):
    valid_units = {'celsius', 'kelvin', 'fahrenheit'}
    
    if from_unit not in valid_units or to_unit not in valid_units:
        return 'invalid measurement'

    if from_unit == to_unit:
        return unit_value

    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (unit_value * 9/5) + 32
        elif to_unit == 'kelvin':
            return unit_value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (unit_value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (unit_value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return unit_value - 273.15
        elif to_unit == 'fahrenheit':
            return (unit_value - 273.15) * 9/5 + 32

    return None 

while True:
    from_unit = input("Enter Starting Unit of Measurement (celsius, kelvin, fahrenheit) or 'exit' to quit: ")
    if from_unit == 'exit':
        break

    to_unit = input("Enter Unit of Measurement to Convert to (celsius, kelvin, fahrenheit): ")
    if to_unit == 'exit':
        break

    try:
        unit_value = float(input(f"Enter Starting Measurement in {from_unit}: "))
    except ValueError:
        print('Invalid input. Please enter a numerical value.')
        continue

    converted_value = Unit_Converter_Temp(from_unit, to_unit, unit_value)

    if converted_value == 'invalid measurement':
        print('Invalid unit of measurement')
    elif converted_value is not None:
        print(f"Result: {unit_value} {from_unit} = {converted_value:.2f} {to_unit}")
    else:
        print("Invalid conversion units")


#Gudd job!!