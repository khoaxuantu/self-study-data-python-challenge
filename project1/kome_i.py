unit_from = input("Enter Unit to Convert From (Meter, Kilometer, Centimeter): ")
unit_to = input("Enter Unit to Convert To (Meter, Kilometer, Centimeter): ")
start_measure = input("Enter Starting Measurement in " + unit_from + ": ")
start_measure = float(start_measure)
if unit_from == "Meter":
    if unit_to == "Meter":
        to_measure = int(start_measure)
    elif unit_to == "Kilometer":
        to_measure = start_measure * (1 / 10 ** 3)
    elif unit_to == "Centimeter":
        to_measure = int(start_measure * (10 ** 2))
    else:
        to_measure = "Error: Please enter valid Unit to Convert to"
elif unit_from == "Kilometer":
    if unit_to == "Meter":
        to_measure = int(start_measure * (10 ** 3))
    elif unit_to == "Kilometer":
        to_measure = int(start_measure)
    elif unit_to == "Centimeter":
        to_measure = int(start_measure * (10 ** 5))
    else:
        to_measure = "Error: Please enter valid Unit to Convert to"   
elif unit_from == "Centimeter":
    if unit_to == "Meter":
        to_measure = start_measure * (1 / 10 ** 2)
    elif unit_to == "Kilometer":
        to_measure = start_measure * (1 / 10 ** 5)
    elif unit_to == "Centimeter":
        to_measure = start_measure
    else:
        to_measure = "Error: Please enter valid Unit to Convert to"
else:
    to_measure = "Error Please enter valid Unit to Convert From"

print("Result: "+ str(start_measure) + " " + unit_from + " = " + str(to_measure) + " " + unit_to)

#Good job!