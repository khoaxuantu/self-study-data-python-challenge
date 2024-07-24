def format_string(input_string, width=20):
    if input_string == "":
        print("*" * width)
    else:
        w = width - 4
        formatted_string = "* {:^{w}} *".format(input_string, w=w)
        print(formatted_string)

map_data = {
    "nanometer": 1,
    "micrometer": 10**3,
    "millimeter": 10**6,
    "centimeter": 10**7,
    "meter": 10**9,
    "kilometer": 10**12,
}

for line in ["", "Measurements", "", *map_data.keys(), ""]:
    format_string(line)

lst_str = ', '.join(map_data.keys())

unit_from = input("Enter Starting Unit of Measurement: ").lower()
if unit_from not in map_data:
    print(f'Invalid Unit of Measurement. Please choose from: "{lst_str}"')
    exit()

unit_to = input("Enter Starting Unit of Measurement: ").lower()
if unit_to not in map_data:
    print(f'Invalid Unit of Measurement. Please choose from: "{lst_str}"')
    exit()

try:
    value = float(input(f"Enter Starting Measurement in {unit_from.capitalize()}s: "))
except ValueError:
    print("Invalid Value. Please enter a number.")
    exit()
    
result = value * map_data[unit_from] / map_data[unit_to]
print(f"Result: {value} {unit_from.capitalize()}s = {result} {unit_to.capitalize()}s")

#Gudd job! You nailed it!!