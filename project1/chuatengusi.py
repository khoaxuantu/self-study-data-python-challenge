StartUnit = input("Enter Starting Unit of Measurement (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ")
TargetUnit = input("Enter Unit of Measurement to Convert to (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ")
StartUnitValue = float(input(f"Enter Starting Measurement in {StartUnit}: "))

UnitExponent = {"Meter": 0, "Kilometer": 3, "Centimeter": -2, "Millimeter": -3, "Micrometer": -6, "Nanometer": -9}

ExponentFrom = UnitExponent.get(StartUnit)
ExponentTo = UnitExponent.get(TargetUnit)

TargetUnitValue = StartUnitValue * 10**(ExponentFrom - ExponentTo)

print(f"Result: {StartUnitValue} {StartUnit} = {TargetUnitValue} {TargetUnit}")

#Good job!! You nailed it