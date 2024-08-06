conversion_factors = {
    'meters': {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'yards': 1.0936132983,
        'feet': 3.280839895,
        'inches': 39.37007874,
    },
    'kilometers': {
        'meters': 1000,
        'kilometers': 1,
        'centimeters': 100000,
        'yards': 1093.6132983,
        'feet': 3280.839895,
        'inches': 39370.07874,
    },
    'centimeters': {
        'meters': 0.01,
        'kilometers': 0.00001,
        'centimeters': 1,
        'yards': 0.010936133,
        'feet': 0.032808399,
        'inches': 0.3937007874,
    },
    'yards': {
        'meters': 0.9144,
        'kilometers': 0.0009144,
        'centimeters': 91.44,
        'yards': 1,
        'feet': 3,
        'inches': 36,
    },
    'feet': {
        'meters': 0.3048,
        'kilometers': 0.0003048,
        'centimeters': 30.48,
        'yards': 0.3333333333,
        'feet': 1,
        'inches': 12,
    },
    'inches': {
        'meters': 0.0254,
        'kilometers': 0.0000254,
        'centimeters': 2.54,
        'yards': 0.0277777778,
        'feet': 0.0833333333,
        'inches': 1,
    }
}

while True:
    starting_unit = input("Enter Starting Unit of Measurement (Meters, Kilometers, Centimeters, Yards, Feet, Inches): ").lower()
    converting_unit = input("Enter Unit of Measurement to Convert to (Meters, Kilometers, Centimeters, Yards, Feet, Inches): ").lower()
    
    if starting_unit not in conversion_factors or converting_unit not in conversion_factors[starting_unit]:
        print("Invalid input, please try again!")
    else:
        starting_number = float(input(f"Enter Starting Measurement in {starting_unit}: "))
        output_number = starting_number * conversion_factors[starting_unit][converting_unit]
        print(f"Result: {starting_number} {starting_unit} = {output_number} {converting_unit}")
    continue_lookup = input("Do you want to perform another conversion? (Yes/No): ").lower()
    
    if continue_lookup == 'no':
        break

#Good job! You nailed it!