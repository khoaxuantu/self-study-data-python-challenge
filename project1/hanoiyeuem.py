def convert(value, from_unit, to_unit):
    to_inches = {
        'inches': 1,
        'feet': 12,
        'yards': 36
    }
    
    value_in_inches = value * to_inches[from_unit]
    
    from_inches = {
        'inches': 1,
        'feet': 1 / 12,
        'yards': 1 / 36
    }
    
    result = value_in_inches * from_inches[to_unit]
    return result

from_unit = input("Enter Starting Unit of Measurement (inches, feet, yards): ")
to_unit = input("Enter Unit of Measurement to Convert to (inches, feet, yards): ")
value = float(input(f"Enter Starting Measurement in {from_unit.capitalize()}: "))

######Why your function is convert() but then you call convert_length() here??#####
result = convert_length(value, from_unit.lower(), to_unit.lower())


print(f"Result: {value} {from_unit.capitalize()} = {result} {to_unit.capitalize()}")

#This converter cannot run so you don't get any point