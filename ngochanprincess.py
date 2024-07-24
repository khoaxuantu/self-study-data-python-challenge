length = {"km": 1000.0, "m": 1.0, "cm": 0.01, "mm": 0.001, "micro-m": 0.000001, "nm": 1.E-9}

start_unit = input("Enter Starting Unit of Measurement (km, m, cm, mm, micro-m, nm): ")
to_unit = input("Enter Unit of Measurement to Convert to (km, m, cm, mm, micro-m, nm): ")
value = float(input("Enter Starting Measurement in Yards: "))

if start_unit == to_unit:
    to_value = value
    print("Result: " + str(value) + " " + start_unit + " = " + str(to_value) + " " + to_unit)
    
else:
    he_so = length[start_unit] / length[to_unit]
    to_value = value * he_so
    print("Result: " + str(value) + " " + start_unit + " = " + str(to_value) + " " + to_unit)

#Keep up the good works!