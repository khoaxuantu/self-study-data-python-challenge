convert_list = {"Second":{"Minute" : 1/60, "Hour":1/3600, "Day":1/86400,"Month":1/2629800,"Year": 1/31557600},
                "Minute":{"Second": 60, "Hour": 1/60,"Day": 1/1440, "Month": 1/43830, "Year": 1/525960},
                "Hour":  {"Second": 3600, "Minute": 60, "Day": 1/24, "Month": 1/730.5, "Year": 1/8766},
                "Day":   {"Second": 86400, "Minute": 1440, "Hour": 24, "Month": 1/30.4375,  "Year": 1/365.25},
                "Month": {"Second": 2629800, "Minute": 43830, "Hour": 730.5, "Day": 30.4375, "Year": 1/12},
                "Year":  {"Second": 31557600, "Minute": 525960, "Hour": 8766, "Day": 365.25,  "Month": 12}}
unit = str(input('Enter Starting Unit of Measurement:')) 
conv = str(input('Enter Unit of Measurement to Convert to:'))
num  = float(input('Enter Starting Measurement in ' + unit))
result = 0
if unit in convert_list and conv in convert_list[unit]:
    unit_measure = convert_list[unit][conv]
    result = num * unit_measure
    print(f"{num} {unit} = {result} {conv}")
else:
    print("Your given unit goes wrong, type in Available Unit Above")
    
# Nice try

