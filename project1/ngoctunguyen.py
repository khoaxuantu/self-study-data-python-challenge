conversion_factors_to_meters = {
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "meters": 1.0,
    "kilometers": 1000.0,
    "miles": 1609.34,
}

# List of units
units = ["inches", "feet", "yards", "meters", "kilometers", "miles"]

from_unit = input(f"Enter Starting Unit of Measurement({', '.join(units)}): ").strip().lower()
to_unit = input(f"Enter Unit of Measurement to Convert to({', '.join(units)}): ").strip().lower()
value = float(input(f"Enter Starting Measurement in {from_unit.capitalize()}: "))

if from_unit in conversion_factors_to_meters and to_unit in conversion_factors_to_meters:

    result = value * conversion_factors_to_meters[from_unit] / conversion_factors_to_meters[to_unit]
    print(f"Result: {value} {from_unit.capitalize()} = {result} {to_unit.capitalize()}")
else:
    print("Invalid unit entered.")

#Guddd job!