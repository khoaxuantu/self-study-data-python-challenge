"""
- Nice work! But this project requires you to convert between a pair, which means from KM -> M and from M -> KM. So you have 6 conversions = 3 pairs

- You can further improve your program by placing your code into a loop, for example

while True:
       print("Enter 0 to stop the program")

       selection = input("Your selection:")
       if selection == 0:
                break
"""

print("Lenght Conversion Program")
print("Enter 1 to convert from kilometers to meters!")
print("Enter 2 to convert from kilometers to centimeters!")
print("Enter 3 to convert from kilometers to millimeters!")
print("Enter 4 to convert from kilometers to micrometers!")
print("Enter 5 to convert from kilometers to nanometers!")
print("Enter 6 to convert from kilometer to miles!")
selection = int(input("Enter your selection here: "))
value_to_convert = float(input("Enter the value to convert: "))

# Convert from kilometers to miters!
if selection == 1:
    value = value_to_convert * 1000
    print(value_to_convert, " kilometers convert to meters is: ", value, "meters")

# Convert from kilometers to centimeters!
elif selection == 2:
    value = value_to_convert * 100000
    print(value_to_convert, " kilometers convert to centimeters is: ", value, "centimeters")
    
# Convert from kilometers to millimeters!
elif selection == 3:
    value = value_to_convert * 1000000
    print(value_to_convert, " kilometers convert to millimeters is: ", value, "millimeters")
# Convert from kilometers to micrometers!")
elif selection == 4:
    value = value_to_convert * 1000000000
    print(value_to_convert, " kilometers convert to micrometers is: ", value, "micrometers")

# Convert from kilometers to nanometers!
elif selection == 5:
    value = value_to_convert * 1000000000000
    print(value_to_convert, " kilometers convert to nanometers is: ", value, "nanometers")

# Convert from kilometer to miles!
elif selection == 6:
    value = value_to_convert * 0.6213688756
    print(value_to_convert, " kilometers convert to miles is: ", value, "miles")

# Out of selection!
else:
    print("Invalid selection! Please enter from 1-6!!!")
