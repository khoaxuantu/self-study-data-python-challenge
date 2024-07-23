def convert_volume_units():
    print("Welcome to the Volume Unit Conversion Tool!")
    print("Please select the units you want to convert between:")
    print("1. Liter")
    print("2. Milliliter")
    print("3. Cubic Meter")
    print("4. US Gallon")
    print("5. US Fluid Ounce")
    print("6. Cubic Centimeter")

    # Get user input for the units
    unit1 = int(input("Enter the number for the 1st unit: "))
    unit2 = int(input("Enter the number for the 2nd unit: "))

    # Get the value to be converted
    value = float(input("Enter the value to be converted: "))

    # Define the conversion factors
    conversion_factors = {
        (1, 2): (1000, 0.001),
        (1, 3): (1000, 0.001),
        (1, 4): ( 0.264172, 3.78541),
        (1, 5): (33.8140227, 0.0295735156),
        (1, 6): (1000, 0.001),        
        (2, 1): (0.001, 1000),
        (2, 3): (0.000001, 1000000),
        (2, 4): (0.000264172, 3785.41),
        (2, 5): (0.0338140386, 29.573515625),       
        (2, 6): (1, 1),        
        (3, 1): (0.001, 1000),
        (3, 2): (1000000, 0.000001),        
        (3, 4): (264.172, 0.003785),        
        (3, 5): (33814.038638, 0.0000295735),
        (3, 6): (1000000, 0.000001),        
        (4, 1): (3.78541, 0.264172),
        (4, 2): (3785.41, 0.000264172),
        (4, 3): (0.003785, 264.172),        
        (4, 5): (128, 0.0078125),        
        (4, 6): (3785.41, 0.000264172),        
        (5, 1): (0.0295735156, 33.8140227),        
        (5, 2): (29.573515625, 0.0338140386),        
        (5, 3): (0.033814, 29.5735),
        (5, 4): (0.0078125, 128),
        (5, 6): (29.573515625, 0.0338140386),
        (6, 1): (0.001, 1000),
        (6, 2): (1, 1),
        (6, 3): (0.000001, 1000000),
        (6, 4): (0.000264172, 3785.41),
        (6, 5): (0.0338140386, 29.573515625)
    }

    # Perform the conversion
    if (unit1, unit2) in conversion_factors:
        factor1, factor2 = conversion_factors[(unit1, unit2)]
        result = value * factor1
        print(f"{value} {unit_names[unit1]} is equal to {result} {unit_names[unit2]}.")
    else:
        print("Invalid unit selection. Please try again.")

    # Add the code to ask if the user wants to continue
    while True:
        continue_conversion = input("Do you want to convert another value? (y/n) ").lower()
        if continue_conversion == 'y':
            convert_volume_units()
        elif continue_conversion == 'n':
            print("Thank you for using the Volume Unit Conversion Tool")
        break

# Define the unit names
unit_names = {
    1: 'liter',
    2: 'milliliter',
    3: 'cubic meter',
    4: 'US gallon',
    5: 'US fluid ounce',
    6: 'cubic centimeter'
}

convert_volume_units()

# Reviewer: Noice

