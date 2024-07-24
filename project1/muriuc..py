# Units conversion factors relative to feet
conversion_factors = [
    12,          # inches
    1,           # feet
    1/3,         # yards
    1/5280,      # miles
    304.8,       # millimeters
    30.48,       # centimeters
    0.3048,      # meters
    0.0003048    # kilometers
]

# List of units
units = ["inches", "feet", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

# Print the options for the starting unit
print("Select the starting unit of measurement:")
for i, unit in enumerate(units, start=1):
    print(f"{i}. {unit}")

# Ask user for their choice of starting unit
start_choice = int(input('Enter your starting unit choice: '))

# Validate user's starting unit choice
if 1 <= start_choice <= len(units):
    from_unit = units[start_choice - 1]
    
    # Ask user to enter the starting measurement
    value = float(input(f"Enter Starting Measurement in {from_unit}: "))

    # Ask user for their choice of conversion
    target_choice = int(input('Enter your target unit choice: '))

    # Validate user's target unit choice
    if 1 <= target_choice <= len(units):
        # Perform the conversion
        from_index = start_choice - 1
        to_index = target_choice - 1
        value_in_feet = value / conversion_factors[from_index]
        converted_value = value_in_feet * conversion_factors[to_index]
        print(f"Result: {value} {from_unit.capitalize()} = {converted_value} {units[to_index].capitalize()}")
    else:
        print('Invalid choice.')
else:
    print('Invalid choice.')

#Good job!