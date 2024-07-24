print("Enter Starting Unit of Measurement (centimeter, meter, kilometer, millimeter, micrometer, nanometer): ", end="")
startUnit = input()
startUnit = startUnit.strip().lower() 
#You can define the start_input and put it in one line, for ex:
#startUnit = input("Enter Starting Unit of Measurement (centimeter, meter, kilometer, millimeter, micrometer, nanometer): ", end="").strip().lower()
print("Enter Unit of Measurement to Covert to (centimeter, meter, kilometer, millimeter, micrometer, nanometer): ", end="")
endUnit = input()
endUnit = endUnit.strip().lower()
print(f"Enter Starting Measurement in {startUnit}: ", end="")
startValue = input()
if (startValue.isnumeric() == True):
    endValue = int(startValue) #Use int() may cause the user can't input the decimal measurements! You can use float() instead
    if startUnit == 'centimeter':
        endValue *= 0.01
    elif startUnit == 'kilometer':
        endValue *= 1000
    elif startUnit == 'millimeter':
        endValue *= 0.001
    elif startUnit == 'micrometer':
        endValue *= 0.000001
    elif startUnit == 'nanometer':
        endValue *= 10**-9
    
    if endUnit == 'centimeter':
        endValue /= 0.01
    elif endUnit == 'kilometer':
        endValue /= 1000
    elif endUnit == 'millimeter':
        endValue /= 0.001
    elif endUnit == 'micrometer':
        endValue /= 0.000001
    elif endUnit == 'nanometer':
        endValue /= 10**-9
    print (f"Result: {startValue} {startUnit}s = {endValue} {endUnit}s")

#Overall, good work! However, you miss the meter case in your if - elif statement so now it counted as 5 pairs => 3 bonus points