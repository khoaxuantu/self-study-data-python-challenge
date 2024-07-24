print("First !!!! Please enter the correct upper and lower case format !!!")
unit_in = input("Enter starting Unit of Measurement(Meter, Kilometer, Centimeter, Millimeter, Yard, Inch) :")
unit_out = input("Enter Unit of Measurement to convert to (Meter, Kilometer, Centimeter, Millimeter, Yard, Inch) :")
value = float(input(f"Enter starting Measurement in {unit_in}:"))

Dic_1m = {'Meter':1 ,'Kilometer':0.001 , 'Centimeter' :100 ,'Millimeter': 1000 ,'Yard':1.0936132983 ,'Inch':39.37007874}
for x in Dic_1m:
    if(unit_in == x):
        h = float(Dic_1m[x])
    if(unit_out == x):
        out = Dic_1m[x]
result = float(value*(out/h))
print(result)

# Reviewer: Noice

