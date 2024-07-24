conversions = {
    'miles': {'kilometers': 1.60934, 'meters': 1609.34, 'inches': 63360, 'feet': 5280, 'yards': 1760},
    'kilometers': {'meters': 1000, 'miles': 0.6214, 'inches': 39370.1, 'feet': 3280.84, 'yards': 1093.61},
    'meters': {'kilometers': 1/1000, 'miles': 0.000621371, 'inches': 39.3701, 'feet': 3.28084, 'yards': 1.09361}, 
    'inches': {'miles': 1/63360, 'kilometers': 1/39370.1, 'meters': 1/39.3701, 'feet': 1/12, 'yards': 1/36},
    'feet': {'miles': 1/5280, 'kilometers': 1/3280.84, 'meters': 1/3.28084, 'inches': 12, 'yards': 1/3},
    'yards': {'miles': 1/1760, 'kilometers': 1/1093.61, 'meters': 1/1.09361, 'inches': 36, 'feet': 3}
}

from_unit = input("Enter Starting Unit of Measurement(miles, kilometers, meters, inches, feet, yards): ").lower()
to_unit = input("Enter Unit of Measurement to Convert to(miles, kilometers, meters, inches, feet, yards): ").lower()
value = eval(input(f"Enter Starting Measurement in {from_unit.capitalize()}: "))

if from_unit == to_unit:
    result = value
else:
    result = value * conversions[from_unit][to_unit]

print(f"Result: {value} {from_unit.capitalize()} = {result} {to_unit.capitalize()}")