Lengths = ["kilometer", "meter", "centimeter", "milimeter", "mile", "yard"]
conversion_coeffs = [1,1000,100000,1000000,0.621,1093.613]

print("Units to choose ( Please use small caps only )") #You can use lower() to returns a string where all characters are lower case 
i = 0
for unit in Lengths:
    print(Lengths[i])
    i+=1

from_unit = input("Enter the Unit to convert from : ")
to_unit = input("Enter the unit to convert to : ")
value = int(input("Enter the Value : ")) #Use int() may cause the user can't input the decimal measurements!
converted_value = round(value/conversion_coeffs[Lengths.index(from_unit)]*conversion_coeffs[Lengths.index(to_unit)], 5)

print(f" {value} {from_unit} = {converted_value} {to_unit} ")

#Overall, good job!