# Definition of Units
conversion_factors = {
    'meters' : 1,
    'kilometers' : 1000,
    'centimeters' : 0.01,
    'yards' : 0.9144,
    'feet' : 0.3048,
    'inches' : 0.0254
}

# Get user input for units and value
from_unit = input("Enter Starting Unit of Measurement(meters, kilometers, centimeters, yards, feet, inches): ")
to_unit = input("Enter Unit of Measurement to Convert to(meters, kilometers, centimeters, yards, feet, inches): ")
value = float(input(f"Enter Starting Measurement in {from_unit}: "))

# Check if input units are supported
if from_unit not in conversion_factors:
    print(f"Unsupported unit: {from_unit}")
elif to_unit not in conversion_factors:
    print(f"Unsupported unit: {to_unit}")
else:
    # Convert value to meters
    value_in_meters = value*conversion_factors[from_unit]
    # Convert value from meters to target unit
    converted_value = value_in_meters/conversion_factors[to_unit]
    # Print the result
    print(f"Result: {value} {from_unit} = {converted_value} {to_unit}")

# Reviewer: Noice

