lengths = {"km": 1000.0, "m": 1.0, "cm": 0.01, "mm": 0.001, "micro-m": 0.000001, "nm": 1.E-9}

start_unit = input("Enter Starting Unit of Measurement (km, m, cm, mm, micro-m, nm): ")
to_unit = input("Enter Unit of Measurement to Convert to (km, m, cm, mm, micro-m, nm): ")
value = float(input("Enter Starting Measurement in Yards: "))

if start_unit == to_unit:
    new_value = value
    print("Result: " + str(value) + " " + start_unit + " = " + str(new_value) + " " + to_unit)
    
else:
    conversion_factor = lengths[start_unit] / lengths[to_unit]
    new_value = value * conversion_factor
    print("Result: " + str(value) + " " + start_unit + " = " + str(new_value) + " " + to_unit)


#Good work!