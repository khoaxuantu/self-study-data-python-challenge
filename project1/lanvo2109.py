# Reviewer: Please handle out of bound input cases
a = input("Enter Starting Unit of Measurement (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ")
b = input("Enter Unit of Measurement to Convert to (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ")
FromUnit = float(input(f"Enter Starting Measurement in {a}: "))

ExponentFrom = 0
ExponentTo = 0

if a == "Meter":
    ExponentFrom = 0
elif a == "Kilometer":
    ExponentFrom = 3
elif a == "Centimeter":
    ExponentFrom = -2
elif a == "Millimeter":
    ExponentFrom = -3
elif a == "Micrometer":
    ExponentFrom = -6
elif a == "Nanometer":
    ExponentFrom = -9

if b == "Meter":
    ExponentTo = 0
elif b == "Kilometer":
    ExponentTo = 3
elif b == "Centimeter":
    ExponentTo = -2
elif b == "Millimeter":
    ExponentTo = -3
elif b == "Micrometer":
    ExponentTo = -6
elif b == "Nanometer":
    ExponentTo = -9

ToUnit = FromUnit * 10**(ExponentFrom - ExponentTo)

print(f"Result: {FromUnit} {a} = {ToUnit} {b}")

