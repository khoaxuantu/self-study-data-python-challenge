#CHOOSE LENGTH
length_units = {'Meter': 1, 
    'Kilometer': 0.001, 
    'Centimeter': 100, 
    'Millimeter': 1000, 
    'Micrometer': 1000000, 
    'Nanometer': 1000000000}

#Enter starting unit:
from_unit = input("Enter Starting Unit of Measurement (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer):")
#Enter ending unit:
to_unit = input("Enter Unit of Measurement to Convert to (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer):")
#Enter number you want to convert:
value = input(f"Enter Starting Measurement in {from_unit}:")

if from_unit not in length_units or to_unit not in length_units:
    print("Invalid Unit")

#Use the Meter as a medium
#Convert from the first unit to Meters:
value_in_meters = int(value) / length_units[from_unit]

#Convert from Meters to the final unit:
converted_value = value_in_meters * length_units[to_unit]
    
print("Result:", value, from_unit, "=", converted_value, to_unit)

# Noice

