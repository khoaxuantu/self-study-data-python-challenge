def convert_weight(value, from_unit, to_unit):
    conversion_factors_to_kg = {
        'Kilogram': 1,
        'Gram': 1000,
        'Milligram': 1000000,
        'Metric Ton': 0.001,
        'Long Ton': 0.0009842073,
        'Short Ton': 0.0011023122,
        'Pound': 2.2046244202,
        'Ounce': 35.273990723,
        'Carat': 5000,
        'Atomic mass unit': 6.022136652e+26
    }

    # Convert Starting value to kilogram
    value_in_kg = value * conversion_factors_to_kg[from_unit]

    # Convert from kilogram to the target unit
    value_in_target_unit = value_in_kg / conversion_factors_to_kg[to_unit]

    # Round to the nearest integer
    return round(value_in_target_unit)

# Receive input
from_unit = input("Enter Starting Unit of Measurement (Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
to_unit = input("Enter Unit of Measurement to Convert to (Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
value = int(input(f"Enter Starting Measurement in {from_unit}: "))

# Starting convert
try:
    converted_value = convert_weight(value, from_unit, to_unit)
    # Result
    print(f'Result: {value} {from_unit} = {converted_value} {to_unit}')
except KeyError:
    print("Error: Invalid unit entered. Please check your units and try again.")
#final



#Please careful with the output. Limiting the decimal points round() causes the output to return integer value so it cannot show some decimals point answers correctly.
#Besides, I believe you have mistypes the converting part, it should be:
'''
    # Convert Starting value to kilogram
    value_in_kg = value / conversion_factors_to_kg[from_unit]

    # Convert from kilogram to the target unit
    value_in_target_unit = value_in_kg * conversion_factors_to_kg[to_unit]
'''
#So your program is not right! Be careful next time !