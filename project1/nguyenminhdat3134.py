# Dictionary to store 6 conversion factors
conversion_factors = {
    'Meter': {'Kilometer': 0.001, 'Centimeter': 100, 'Yard': 1.09361, 'Foot': 3.28084, 'Inch': 39.3701},
    'Kilometer': {'Meter': 1000, 'Centimeter': 100000, 'Yard': 1093.61, 'Foot': 3280.84, 'Inch': 39370.1},
    'Centimeter': {'Meter': 0.01, 'Kilometer': 0.00001, 'Yard': 0.0109361, 'Foot': 0.0328084, 'Inch': 0.393701},
    'Yard': {'Meter': 0.9144, 'Kilometer': 0.0009144, 'Centimeter': 91.44, 'Foot': 3, 'Inch': 36},
    'Foot': {'Meter': 0.3048, 'Kilometer': 0.0003048, 'Centimeter': 30.48, 'Yard': 0.333333, 'Inch': 12},
    'Inch': {'Meter': 0.0254, 'Kilometer': 0.0000254, 'Centimeter': 2.54, 'Yard': 0.0277778, 'Foot': 0.0833333}
}

# List to store available units
units = list(conversion_factors.keys())

#While loop to run infinte times
while True:
    print("\nAvailable units: ", units)
    unit_from = input(f"Enter Starting Unit of Measurement({units}): ")
    unit_to = input("Enter Unit of Measurement to Convert to: ")
    value = float(input(f"Enter Starting Measurement in {unit_from}: "))

    #Checking the input exists in units list
    if unit_from in units and unit_to in units:
        result = value * conversion_factors[unit_from][unit_to]
        print(f"Result: {value} {unit_from} = {result} {unit_to}")
    else:
        print("Invalid unit. Please try again.")

    #Run the loop again or break it
    response = input("\nDo you want to convert again? (y/n): ").lower()
    if response == 'n' or response == "no":
        break

#Gudddd job!