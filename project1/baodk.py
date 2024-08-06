# declare measurement dictionary
measurements = \
    { "Length": { "Inches": 1e4/254,
                  "Feet": 1e4/3048,
                  "Yards": 1e4/9144,
                  "Miles": 1e3/1609344,
                  "Meters": 1 },
      "Area": { "Hectare": 1e-4,
                "Square miles": 1/2589990,
                "Acres": 1e3/4046856,
                "Square meters": 1},
      "Weight": { "Ounces": 1e3/28350,
                  "Pounds": 1e3/453592,
                  "Miligrams": 1e3,
                  "Kilograms": 1e-3}}

# switch measurement units
# measurement = measurements["Length"]
measurement = measurements["Area"]
# measurement = measurements["Weight"]

# handling input unit to convert
all_units = list(measurement.keys())
while True:
    unit_from = input(f"Enter Starting unit of Measurement({", ".join(all_units)}) ").strip().capitalize()
    ratio_from = measurement.get(unit_from)
    if ratio_from is None:
        print("Improper unit entry! Enter again!")
    else:
        break
# handling input unit converting to
units_to_convert = [u for u in all_units if u != unit_from]
while True:
    unit_to = input(f"Enter unit of Measurement to Convert to({", ".join(units_to_convert)}) ").strip().capitalize()
    ratio_to = measurement.get(unit_to)
    if ratio_to is None or unit_to == unit_from:
        print("Improper unit entry! Enter again!")
    else:
        break

# check quantity for converting whether convertible
while True:
    val_input = input(f"Enter Starting Measurement in {unit_from}: ").strip()
    if  val_input.startswith("-") and val_input[1:].replace(".", "", 1).isnumeric() \
    or val_input.replace(".", "", 1).isnumeric():
        break
    else:
        print("Improper measurement entry! Enter again!")

# calculation and print out the result
converted_val = float(val_input) / ratio_from * ratio_to
print(f"Result: {val_input} {unit_from} = {int(converted_val) if str(converted_val).endswith(".0") else converted_val} {unit_to}")

#Good job!