conversions = {'Meter': 1,
    'Kilometer': 0.001,
    'Centimeter': 100,
    'Millimeter': 1000,
    'Micrometer': 1000000,
    'Nanometer': 1000000000}
#Enter starting unit below (Ex: meter):
Starting_unit= 'Meter'
#Enter ending unit below (Ex: Nanometer):
Ending_unit = 'Nanometer'
#Enter number you want to convert here (Ex: 10):
value = 1

if Starting_unit not in conversions or Ending_unit not in conversions:
    print("Invalid Unit")

value_in_meters = int(value) / conversions[Starting_unit]

converted_value = value_in_meters * conversions[Ending_unit]

print("Result:", value, Starting_unit, "=", converted_value, Ending_unit)

# Good work! However, I think your code can be enhanced by using the input() function to ask the user for input :3 
# Keep up the good work!