def convert_length(value, from_unit, to_unit):
    conversion_to_meters = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'miles': 1609.35,
        'feet': 0.3048,
        'inches': 0.0254
    }
    converted_value = value * conversion_to_meters[from_unit] / conversion_to_meters[to_unit]
    return converted_value

def valid_unit(prompt):
    unit_lst = ['meters', 'kilometers', 'centimeters', 'miles', 'feet', 'inches']
    while True:
        unit = input(prompt)
        if unit in unit_lst:
            return unit
        print("Invalid input. Please enter one of the following units: meters, kilometers, centimeters, miles, feet, inches.")

def valid_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input. Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number greater than 0.")

def result():
    from_unit = valid_unit("Enter starting unit of measurement (meters, kilometers, centimeters, miles, feet, inches): ")
    to_unit = valid_unit("Enter unit of measurement to convert to (meters, kilometers, centimeters, miles, feet, inches): ")
    value = valid_value(f"Enter starting measurement in {from_unit}: ")
    converted_value = convert_length(value, from_unit, to_unit)
    print(f"Result: {value} {from_unit} = {converted_value} {to_unit}")

result()

# Noice clean code

