def convert_area(value, from_unit, to_unit):
    units = {
        'square meter': 1,
        'square kilometer': 0.000001,
        'square centimeter': 10000,
        'square millimeter': 1000000,
        'square micrometer': 1000000000000,
        'hectare': 0.0001
    }

    value_in_square_meters = value / units[from_unit]
    converted_value = value_in_square_meters * units[to_unit]

    return converted_value
    
from_unit = input("Enter Starting Unit of Measurement (square meter, square kilometer, square centimeter, square millimeter, square micrometer, hectare): ")
to_unit = input("Enter Unit of Measurement to Convert to (square meter, square kilometer, square centimeter, square millimeter, square micrometer, hectare): ")
value = float(input(f"Enter Starting Measurement in {from_unit.title()}: "))

result = convert_area(value = value, from_unit = from_unit, to_unit = to_unit)
print(f"Result: {value} {from_unit.title()} = {result} {to_unit.title()}")

#Keep up the good works!
