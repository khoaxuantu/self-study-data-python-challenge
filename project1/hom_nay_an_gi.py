lengths = {"km": 1000.0, "m": 1.0, "cm": 0.01}

start_unit = input("Enter Starting Unit of Measurement (km, m, cm): ").lower()
to_unit = input("Enter Unit of Measurement to Convert to (km, m, cm): ").lower()
try:
    value = float(input("Enter Starting Measurement in " + start_unit.upper() + " : ").replace(",","."))
except ValueError as e:
    print(f"Error: Invalid input. Please enter a numerical value. Commas (,) are not allowed. Use decimal points (.) instead.")
    exit()
if start_unit not in lengths or to_unit not in lengths:
  print(f"Error: Invalid units. Please enter 'km', 'm', or 'cm'.")
  exit()

if start_unit == to_unit:
  new_value = value
  print("Result: " + str(value) + " " + start_unit.upper() + " = " + str(new_value) + " " + to_unit.upper())
else:
  conversion_factor = lengths[start_unit] / lengths[to_unit]
  new_value = value * conversion_factor
  print("Result: " + str(value) + " " + start_unit.upper() + " = " + str(new_value) + " " + to_unit.upper())

#Great Job!