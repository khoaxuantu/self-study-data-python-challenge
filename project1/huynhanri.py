def convert_length(value, from_unit, to_unit):
    # Convert from the input unit to inches first
    if from_unit == "inches":
        value_in_inches = value
    elif from_unit == "feet":
        value_in_inches = value * 12  # 1 foot = 12 inches
    elif from_unit == "yards":
        value_in_inches = value * 36  # 1 yard = 36 inches
    elif from_unit == "meter":
        value_in_inches = value / 0.0254  # 1 meter = 39.3701 inches, so 1 inch = 0.0254 meters
    elif from_unit == "mile":
        value_in_inches = value * 63360  # 1 mile = 63360 inches
    elif from_unit == "centimeter":
        value_in_inches = value / 2.54  # 1 centimeter = 0.393701 inches, so 1 inch = 2.54 centimeters
    else:
        return "Invalid input unit. Let try again"  # Handle invalid input units

    # Convert from inches to the desired output unit
    if to_unit == "inches":
        return value_in_inches
    elif to_unit == "feet":
        return value_in_inches / 12  # Convert inches to feet
    elif to_unit == "yards":
        return value_in_inches / 36  # Convert inches to yards
    elif to_unit == "meter":
        return value_in_inches * 0.0254  # Convert inches to meters
    elif to_unit == "mile":
        return value_in_inches / 63360  # Convert inches to miles
    elif to_unit == "centimeter":
        return value_in_inches * 2.54  # Convert inches to centimeters
    else:
        return "Invalid output unit. Let try again"  # Handle invalid output units

def main():
    # Get input from the user for the starting unit
    print("Enter Starting Unit of Measurement (inches, feet, yards, meter, mile, centimeter):")
    from_unit = input().strip().lower()
    
    # Get input from the user for the unit to convert to
    print("Enter Unit of Measurement to Convert to (inches, feet, yards, meter, mile, centimeter):")
    to_unit = input().strip().lower()
    
    # Get the measurement value from the user
    print(f"Enter Starting Measurement in {from_unit.capitalize()}:")
    value = float(input().strip())
    
    # Perform the conversion
    result = convert_length(value, from_unit, to_unit)
    if isinstance(result, str):  # Check if result is an error message
        print(result)
    else:
        # Print the result in a formatted string
        print(f"Result: {value} {from_unit.capitalize()} = {result:.2f} {to_unit.capitalize()}")

# The following block ensures the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()

#Great job but please careful with the output. Limiting the decimal points (2f) causes the output cannot show the answer correctly.