start_unit = input("Enter the starting unit of the measurement(inches, feet, yards): ")
start_unit = start_unit.lower()
end_unit = input("Enter the target unit of the measurement(inches, feet, yards): ")
end_unit = end_unit.lower()
start_measure = float(input("Enter starting measurement in %s" % start_unit))

result = start_measure
if start_unit == "inches":
    if end_unit == "feet":
        result = start_measure / 12
    elif end_unit == "yards":
        result = start_measure / 36
elif start_unit == "feet":
    if end_unit == "inches":
        result = start_measure * 12
    elif end_unit == "yards":
        result = start_measure / 3
elif start_unit == "yards":
    if end_unit == "inches":
        result = start_measure * 36
    elif end_unit == "feet":
        result = start_measure * 3
start_measure = round(start_measure, 10)
result = round(result, 10)
print("Result:", start_measure, start_unit, "=", result, end_unit)

#Gud work!