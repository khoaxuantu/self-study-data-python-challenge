Unit_Input = input("Enter Starting Unit of Measurement(Kilometer, Meter, Centimeter, Millimeter, Micrometer, Nanometer): ")
Unit_Output = input("Enter Unit of Measurement to Convert to(Kilometer, Meter, Centimeter, Millimeter, Micrometer, Nanometer): ")
Number_Of_Unit_Input = float(input("Enter Starting Measurement in " + Unit_Input.capitalize() + ": ")) 

Result = 0.0
if Unit_Input in ['Kilometer', 'kilometer']:
    if Unit_Output in ['Meter', 'meter']:
        Result = Number_Of_Unit_Input * float(10 ** 3)
    elif Unit_Output in ['Centimeter', 'centimeter']:
        Result = Number_Of_Unit_Input * float(10 ** 5)
    elif Unit_Output in ['Millimeter', 'millimeter']:
        Result = Number_Of_Unit_Input * float(10 ** 6)
    elif Unit_Output in ['Micrometer', 'micrometer']:
        Result = Number_Of_Unit_Input * float(10 ** 9)
    elif Unit_Output in ['Nanometer', 'nanometer']:
        Result = Number_Of_Unit_Input * float(10 ** 12)
    else:
        Result = Number_Of_Unit_Input
elif Unit_Input in ['Meter', 'meter']:
    if Unit_Output in ['Kilometer', 'kilometer']:
        Result = Number_Of_Unit_Input * 0.001
    elif Unit_Output in ['Centimeter', 'centimeter']:
        Result = Number_Of_Unit_Input * float(10 ** 2)
    elif Unit_Output in ['Millimeter', 'millimeter']:
        Result = Number_Of_Unit_Input * float(10 ** 3)
    elif Unit_Output in ['Micrometer', 'micrometer']:
        Result = Number_Of_Unit_Input * float(10 ** 6)
    elif Unit_Output in ['Nanometer', 'nanometer']:
        Result = Number_Of_Unit_Input * float(10 ** 9)
    else:
        Result = Number_Of_Unit_Input
elif Unit_Input in ['Centimeter', 'centimeter']:
    if Unit_Output in ['Kilometer', 'kilometer']:
        Result = Number_Of_Unit_Input * 0.00001
    elif Unit_Output in ['Meter', 'meter']:
        Result = Number_Of_Unit_Input * 0.01
    elif Unit_Output in ['Millimeter', 'millimeter']:
        Result = Number_Of_Unit_Input * float(10)
    elif Unit_Output in ['Micrometer', 'micrometer']:
        Result = Number_Of_Unit_Input * float(10 ** 4)
    elif Unit_Output in ['Nanometer', 'nanometer']:
        Result = Number_Of_Unit_Input * float(10 ** 7)
    else:
        Result = Number_Of_Unit_Input
elif Unit_Input in ['Millimeter', 'millimeter']:
    if Unit_Output in ['Kilometer', 'kilometer']:
        Result = Number_Of_Unit_Input * 0.000001
    elif Unit_Output in ['Meter', 'meter']:
        Result = Number_Of_Unit_Input * 0.001
    elif Unit_Output in ['Centimeter', 'centimeter']:
        Result = Number_Of_Unit_Input * 0.1
    elif Unit_Output in ['Micrometer', 'micrometer']:
        Result = Number_Of_Unit_Input * float(10 ** 3)
    elif Unit_Output in ['Nanometer', 'nanometer']:
        Result = Number_Of_Unit_Input * float(10 ** 6)
    else:
        Result = Number_Of_Unit_Input
elif Unit_Input in ['Micrometer', 'micrometer']:
    if Unit_Output in ['Kilometer', 'kilometer']:
        Result = Number_Of_Unit_Input * 0.000000001
    elif Unit_Output in ['Meter', 'meter']:
        Result = Number_Of_Unit_Input * 0.000001
    elif Unit_Output in ['Centimeter', 'centimeter']:
        Result = Number_Of_Unit_Input * 0.0001
    elif Unit_Output in ['Millimeter', 'millimeter']:
        Result = Number_Of_Unit_Input * 0.001
    elif Unit_Output in ['Nanometer', 'nanometer']:
        Result = Number_Of_Unit_Input * float(1000)
    else:
        Result = Number_Of_Unit_Input
elif Unit_Input in ['Nanometer', 'nanometer']:
    if Unit_Output in ['Kilometer', 'kilometer']:
        Result = Number_Of_Unit_Input * 0.000000000001
    elif Unit_Output in ['Meter', 'meter']:
        Result = Number_Of_Unit_Input * 0.000000001
    elif Unit_Output in ['Centimeter', 'centimeter']:
        Result = Number_Of_Unit_Input * 0.0000001
    elif Unit_Output in ['Millimeter', 'millimeter']:
        Result = Number_Of_Unit_Input * 0.000001
    elif Unit_Output in ['Micrometer', 'micrometer']:
        Result = Number_Of_Unit_Input * 0.001
    else:
        Result = Number_Of_Unit_Input
print("Result: " + str(int(Number_Of_Unit_Input)) + " " + Unit_Input.capitalize() + " = " + str(int(Result)) + " " + Unit_Output.capitalize())

#Your code does a great job of converting between various units of length. 
#However, you can optimized/ shorten it by utilize the capitalize() function in the converting part.