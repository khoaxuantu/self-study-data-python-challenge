conversions={'Meter':1, 'Kilometer':1000, 'Centimeter':0.01, 'Millimeter': 0.001, 'Micrometer': 0.000001}
print()
from_unit =input('Enter Starting Unit of Measurement (Meter, Kilometer, Centimeter, Millimeter, Micrometer): ')
print()
to_unit = input('Enter Unit of Measurement to Convert to (Meter, Kilometer, Centimeter, Millimeter, Micrometer): ')
print()
from_value = float(input(f"Enter Starting Measurement in {from_unit}: "))
from_value_in_meter=from_value*conversions[from_unit]
to_value=from_value_in_meter/conversions[to_unit]
print(f'{from_value} {from_unit} = {to_value} {to_unit}')

#Great job!. But you can improve the input by using the strip() and lower() function to accept the mistype case.