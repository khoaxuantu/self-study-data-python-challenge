unit_in = input("Enter the unit you want to convert \n (gram, kilogram,ounce,pound,metric ton,short ton):")
value = float(input("Enter the value you want to convert:"))
unit_out = input("Enter the unit you want to convert to \n (gram, kilogram,ounce,pound,metric ton,short ton):")

def unit_conversion (unit_in = str, value = float, unit_out=str) -> float:
    convert_dict = {"gram":1.00,"kilogram":1000.00, "ounce":28.3495, "pound": 453.592, "metric ton":1000000, "short ton":907184}
    value_converted = value*convert_dict[unit_in]/convert_dict[unit_out]
    return value_converted

value_converted = unit_conversion(unit_in,value, unit_out)

print(f"{value} {unit_in} is equal to {value_converted} {unit_out}")


#Keep up good works! You nailed it