def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1.0,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1000.0,
        'pounds': 453.592,
        'ounces': 28.3495,
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def main():
    print("Welcome to the Unit Converter!")
    print("Available conversions: length, weight")
    
    while True:
        conversion_type = input("Enter the type of conversion you want to perform: ").strip().lower()
        
        if conversion_type == 'length':
            from_unit = input("Enter the unit to convert from (Meters, Inches, Feet, Yards, Miles): ").strip().lower()
            to_unit = input("Enter the unit to convert to (Meters, Inches, Feet, Yards, Miles): ").strip().lower()
            value = float(input("Enter the value to convert: "))
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == 'weight':
            from_unit = input("Enter the unit to convert from (Kilograms, Pounds, Ounces): ").strip().lower()
            to_unit = input("Enter the unit to convert to (Kilograms, Pounds, Ounces): ").strip().lower()
            value = float(input("Enter the value to convert: "))
            result = convert_weight(value, from_unit, to_unit)
        else:
            print("Invalid conversion type.")
            continue
        
        print(f"Result: {value} {from_unit} = {result} {to_unit}")
        
        again = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if again != 'yes':
            break

    print("Thank you for using the Unit Converter!")
    input("Press enter to exit.")

if __name__ == "__main__":
    main()

# Reviewer: Noice

