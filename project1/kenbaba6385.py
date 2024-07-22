number_conver={
'length' :{
        ('km', 'km'): 1,
        ('km', 'm'): 1000,
        ('km', 'cm'): 100000,
        ('km', 'mm'): 1000000,
        ('km', 'yard'): 1093.61,
        ('m', 'km'): 1/1000,
        ('m', 'm'): 1,
        ('m', 'cm'): 100,
        ('m', 'mm'): 1000,
        ('m', 'yard'): 1.09361,
        ('cm', 'km'): 1/100000,
        ('cm', 'm'): 1/100,
        ('cm', 'cm'): 1,
        ('cm', 'mm'): 10,
        ('cm', 'yard'): 0.0109361,
        ('mm', 'km'): 1/1000000,
        ('mm', 'm'): 1/1000,
        ('mm', 'cm'): 1/10,
        ('mm', 'mm'): 1,
        ('mm', 'yard'): 0.001093,
        ('yard', 'km'): 0.0009144,
        ('yard', 'm'): 0.9144,
        ('yard', 'cm'): 91.44,
        ('yard', 'mm'): 914.4,
        ('yard', 'yard'): 1
},
'weight':{
        ('kg', 'kg'): 1,
        ('kg', 'g'): 1000,
        ('kg', 'mg'): 1000000,
        ('g', 'kg'): 1/1000,
        ('g', 'g'): 1,
        ('g', 'mg'): 1000,
        ('mg', 'kg'): 1/1000000,
        ('mg', 'g'): 1/1000,
        ('mg', 'mg'): 1,
}
}
convert_type = input("Enter conversion type (length, weight,..): ")
number=(number_conver[convert_type].get((start_unit, end_unit))) # start_unit and end_unit are not defined here, so I cannot give you points

# Please handle the out of bound cases
if(convert_type=='length'):
    start_unit = input("Enter Starting Unit of Measurement (km,m,cm,mm,yard): ")
    end_unit = input("Enter Unit of Measurement to Convert to (km,m,cm,mm,yard): ")
elif(convert_type=='weight'):
    start_unit = input("Enter Starting Unit of Measurement (kg,g,mg): ")
    end_unit = input("Enter Unit of Measurement to Convert to (kg,g,mg): ")
a = input("Enter Starting Measurement in "+start_unit)
a=int(a)
if number!=0:
    result=a*number
    print(f"Result: {a} {start_unit} = {result} {end_unit}")
else :
    print('No number')

