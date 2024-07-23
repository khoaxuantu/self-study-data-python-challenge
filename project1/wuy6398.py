from_ = input('Enter Starting Unit of Measurement (meters, miles, yards, feet, inches, light years):').capitalize()
to_ = input('Enter Unit of Measurement to Convert to (meters, miles, yards, feet, inches, light years):').capitalize()
length = int(input(f"Enter Starting Measurement in {from_}:"))

mile_ = {'Meters': 1609.344,
          'Miles': 1,
          'Yards': 1760,
          'Feet': 5280,
          'Inches': 1760*36,
          'Light years': 9460730472580800/1609.344}

if from_ not in mile_.keys() or to_ not in mile_.keys():
    print(f"There're currently no measurements of {from_} or {to_} in the system!")
else:
    if from_ == to_:
        result = length
    else:
        result = length/mile_[from_]*mile_[to_]
    print(f"Result: {length} {from_} = {result} {to_}")

# Reviewer: Noice

