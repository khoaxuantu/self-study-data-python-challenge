#Using strip() and lower() is a great idea to ensure the user's input. Keep up the good works!
def convert_units():
    value = float(input("Enter the distance: "))
    from_unit = input("Enter the unit of the distance (meter, kilometer, centimeter, millimeter, micrometer, mile): ").strip().lower()
    to_unit = input("Enter the unit to convert to (meter, kilometer, centimeter, millimeter, micrometer, mile): ").strip().lower()
    
    # Conversion to meters based on the input unit
    if from_unit == "kilometer":
        value_in_meters = value * 1000
    elif from_unit == "centimeter":
        value_in_meters = value / 100
    elif from_unit == "millimeter":
        value_in_meters = value / 1000
    elif from_unit == "micrometer":
        value_in_meters = value / 1_000_000
    elif from_unit == "mile":
        value_in_meters = value * 1609.344
    elif from_unit == "meter":
        value_in_meters = value
    else:
        print("Invalid input unit.")
        return
    
    # Conversion from meters to the desired output unit
    if to_unit == "kilometer":
        result = value_in_meters / 1000
    elif to_unit == "centimeter":
        result = value_in_meters * 100
    elif to_unit == "millimeter":
        result = value_in_meters * 1000
    elif to_unit == "micrometer":
        result = value_in_meters * 1_000_000
    elif to_unit == "mile":
        result = value_in_meters / 1609.344
    elif to_unit == "meter":
        result = value_in_meters
    else:
        print("Invalid output unit.")
        return
    
    # Display the result
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

# Call the function
convert_units()