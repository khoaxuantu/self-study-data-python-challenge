def convert(value, from_unit, to_unit):
    conversion_factors = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'micrometer': 1e6,
        'nanometer': 1e9
    }
    value_in_meters = value / conversion_factors[from_unit]
    converted_value = value_in_meters * conversion_factors[to_unit]
    
    return converted_value

units = ['meter', 'kilometer', 'centimeter', 'millimeter','micrometer', 'nanometer']
print("Available units:")
for i, unit in enumerate(units):
    print(f"{i+1}. {unit}")

value = float(input("Value "))

from_unit_index = int(input("From (1-6): ")) - 1
to_unit_index = int(input("To (1-6): ")) - 1

from_unit = units[from_unit_index]
to_unit = units[to_unit_index]
result = convert(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')

#Keep up the good works