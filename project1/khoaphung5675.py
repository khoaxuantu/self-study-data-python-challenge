#Em nộp lại project do hiểu sai đề nha hihi :>

def convert_units(value, from_unit, to_unit):
    # Conversion factors relative to mmeters
    conversion_factors = {
        'meters': 1,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'kilometers': 1000
    }

    # Convert from the original unit to meters
    value_in_meters = value * conversion_factors[from_unit]

    # Convert from meters to the desired unit
    converted_value = value_in_meters / conversion_factors[to_unit]

    return converted_value

def main():
    print("Unit of Measurement Converter Project")
    print("Available units: meters, centimeters, millimeters, kilometers")
    
    # Reviewer: Please handle the out of bound cases
    from_unit = input("Enter Starting Unit of Measurement (meters, centimeters, millimeters, kilometers): ").strip().lower()
    to_unit = input("Enter Unit of Measurement to Convert to (meters, centimeters, millimeters, kilometers): ").strip().lower()
    value = float(input(f"Enter Starting Measurement in {from_unit}: "))

    result = convert_units(value, from_unit, to_unit)
    print(f"Result: {value} {from_unit} = {result} {to_unit}")

if __name__ == "__main__":
    main()

