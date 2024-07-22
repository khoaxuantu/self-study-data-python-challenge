def Converter(x, unit1, unit2):
    time_values = {
        'second' : 1,
        'minute' : 60,
        'hour'   : 3600,
        'day'    : 86400,
        'week'   : 604800,
        'month'  : 2592000,
        'year'   : 31557600
    }
    if unit1 not in time_values: # Can be 'or unit 2 not in time_values' instead of 2 ifs 
        return "Invalid"
    if unit2 not in time_values: 
        return "Invalid"
    time = x * time_values[unit1]
    time = time / time_values[unit2]
    return time

u1 = ''
u2 = ''
x = 0
while not u1:
    u1 = input("Enter your Unit of Measurement(Second, Minute, Hour, Day, Week, Month):  ")

while not u2:
    u2 = input("Enter the Unit of Measurement to convert into(Second, Minute, Hour, Day, Week, Month): ")

x = float(input("Enter Starting Measurement in " + u1.title()+ ": "))
x = Converter(x, u1.lower(), u2.lower())
print(x)

