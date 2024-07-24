valid_units = ['meter', 'kilometer', 'millimeter']
unit1 = input(f'Enter Starting Unit of Measurement (millimeter, meter, kilometer) ->').strip().lower()
unit2 = input(f'Enter Unit of Measurement to Convert to (millimeter, meter, kilometer) ->').strip().lower()
while unit1 and unit2 in valid_units:
    value = float(input(f'Enter Starting Measurement in {unit1}  -> '))
    # Reviewer: Don't be if...else slave dude -.-
    if unit1 == "millimeter" and unit2 == "millimeter":
            answer = float(value)
    elif unit1 == "millimeter" and unit2 == "meter":
            answer = float(value)/1000
            print('Result:',answer)
    elif unit1 == "millimeter" and unit2 == "kilometer":
            answer = float(value)/1000000
    elif unit1 == "meter" and unit2 == "meter":
            answer = float(value)
    elif unit1 == "meter" and unit2 == "millimeter":
            answer = float(value)*1000
    elif unit1 == "meter" and unit2 == "kilometer":
            answer = float(value)/1000
    elif unit1 == "kilometer" and unit2 == "kilometer":
            answer = float(value)
    elif unit1 == "kilometer" and unit2 == "meter":
            answer = float(value)*1000
    elif unit1 == "kilometer" and unit2 == "millimeter":
            answer = float(value)*1000000
    print("Result:",answer)
    break
else:
    print("Invalid unit. Please enter one of the following: millimeter, meter, kilometer")

