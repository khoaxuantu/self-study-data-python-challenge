# Available length units: kilometers, meters, centimeters, millimeters, miles, feet
# Input variables here
from_unit = 'kilometers'
to_unit = 'miles'
value = 1

# Conversion factors with meters as the center
factors = {
          'kilometers': 1000,
          'meters': 1,
          'centimeters': 0.01,
          'millimeters': 0.001,
          'miles': 1609.344,
          'feet': 0.3048
}

# Convert the value to meters
value_in_meters = value * factors[from_unit]

# Then, convert value_in_meter to target unit
converted = round(value_in_meters / factors[to_unit], 4)

# Keep the "s" if value is plural. If value = 1, make the unit singular
from_unit_result = from_unit[:-1] if value == 1 else from_unit
to_unit_result = to_unit[:-1] if converted == 1 else to_unit

# Output the result
print('Enter Starting Unit of Measurement (kilometers, meters, centimeters, millimeters, miles, feet):', from_unit)
print('Enter Unit of Measurement to Convert to (kilometers, meters, centimeters, millimeters, miles, feet):', to_unit)
print('Enter Starting Measurement in', from_unit + ':', value)
print('Result:', value, from_unit_result, '=', converted, to_unit_result)

#Gud job!