def convert_length(value, from_unit, to_unit):
    # Define conversion rates relative to meters
    units = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'micrometer': 1e6,
        'nanometer': 1e9
    }

    # Convert from input units to meters
    value_in_meters = value / units[from_unit]

    # Convert from meters to output units
    converted_value = value_in_meters * units[to_unit]

    return converted_value

# Example usage:
from_unit = input("Enter Starting Unit of Measurement (meter, kilometer, centimeter, millimeter, micrometer, nanometer): ")
to_unit = input("Enter Unit of Measurement to Convert To (meter, kilometer, centimeter, millimeter, micrometer, nanometer): ")
value = float(input(f"Enter Starting Measurement in {from_unit.title()}: "))

result = convert_length(value=value, from_unit=from_unit, to_unit=to_unit)
print(f"Result: {value} {from_unit.title()} = {result} {to_unit.title()}")

#Nice work!