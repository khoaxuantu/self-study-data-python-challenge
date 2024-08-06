# This is the program that helps you convert any unit of length

length = {'nanometer': 1000000000000, 'micrometer': 1000000000, 'millimeter': 1000000, 'centimeter': 100000,'inch': 39370.07874, 
          'decimeter': 10000,'foot': 3280.839895, 'yard': 1093.6132983, 'meter': 1000, 'dekameter': 100, 'hectometer': 10, 
          'kilometer': 1, 'mile': 0.6213688756, 'light year': 1.057008707E-13} # This is a dictionary of all units of length

print ('Which is unit of length you want to convert?')
unit = input ('Please enter the exact name of the unit you want to convert (Do not use Abbreviation): ')
value = float(input ('Enter the number (float or integer) you want to convert: '))
print ("""
This is the result:
       """)

if unit.lower() in length.keys():
    length_list = list (length.keys()) # to convert keys of length's dictionary to list
    index_unit1 = length_list.index(unit.lower()) # to find a location of unit you choosen in length_list
    index_unit2 = length_list.index(unit.lower()) # to find a location of unit you choosen in length_list
    
    while index_unit2 > 0: # this loop is used to convert the unit to the lower unit
        index_unit2 -= 1
        converted_value = value * length[length_list[index_unit2]] / length[unit.lower()] # to convert value of unit to another unit
        print (f'{value} {unit.lower()} = {converted_value} {length_list[index_unit2]}')    

    while index_unit1 < (len(length_list) - 1): # this loop is used to convert the unit to the higher unit
        index_unit1 += 1
        converted_value = value * length[length_list[index_unit1]] / length[unit.lower()] 
        print (f'{value} {unit.lower()} = {converted_value} {length_list[index_unit1]}')

#Keep up the good work!