#Excellent enthusiasm but please careful with the output. Limiting the decimal points (4f) causes the output cannot show the answers correctly.
#Mistype the 'ValueError'
# ------Program-------------------
print("LENGTH | TEMPURATURE | AREA | VOLUME | WEIGHT | TIME")

rep = 1
while rep == 1:
    unit = input("Choose unit: ").upper()


    if unit == "LENGTH":
        
        print("Measurement: m, km, cm, mm, mcrm, nnm, mile, yard, foot, inch, light year")
        unit_measurement = {"m":1, "km": 0.001, "cm":100, "mm": 1000, "mcrm": 1000000, "nnm":1000000000, "mile":0.0006213689, "yard":1.0936132983, "foot":3.280839895, "inch":39.37007874, "light year":1.057008707E-16}
        while True:
            frm = input("From: ").lower()
            to = input("To: ").lower()
            value = float(input(f"Enter value of {frm}: "))
        
            if frm not in list(unit_measurement.keys()) or to not in unit_measurement.keys():
                print("Invalid input!. Please try again")
            else:
                break
                
        print("Output:")
        print(f"{value} {frm} = {value*unit_measurement[to]/unit_measurement[frm]:.4f} {to}")
            
    elif unit == "TEMPURATURE":
        
        print("Measurement: censius, kelvin, fahrenheit")
        unit_measurement = {"censius":[0, 1], "kelvin":[273.15, 1], "fahrenheit":[32, 1.8]}
        while True:
            frm = input("From: ").lower()
            to = input("To: ").lower()
            value = float(input(f"Enter value of {frm}: "))
        
            if frm not in list(unit_measurement.keys()) or to not in unit_measurement.keys():
                print("Invalid input!. Please try again")
            else:
                break
                
        print("Output:")
        print(f"{value} {frm} = {(unit_measurement[to][0]-unit_measurement[frm][0]) + value*unit_measurement[to][1]:.4f} {to}")
    
    elif unit == "AREA":
        
        print("Measurement: m2, km2, cm2, mm2, mcrm2, hectare, mile2, yard2, foot2, inch2, acre")
        unit_measurement = {"m2":1, "km2": 0.001**2, "cm2":100**2, "mm2": 1000**2, "mcrm2": 1000000**2, "hectare":1100**2, "mile2":0.0006213689**2, "yard2":1.0936132983**2, "foot2":3.280839895**2, "inch2":39.37007874**2, "acre":0.0002471054}
        while True:
            frm = input("From: ").lower()
            to = input("To: ").lower()
            value = float(input(f"Enter value of {frm}: "))
        
            if frm not in list(unit_measurement.keys()) or to not in unit_measurement.keys():
                print("Invalid input!. Please try again")
            else:
                break
                
        print("Output:")
        print(f"{value} {frm} = {value*unit_measurement[to]/unit_measurement[frm]:.4f} {to}")
        
        
    elif unit == "VOLUME":
        
        print("Measurement: m3, km3, cm3, mm3, l, ml, gallon, quart, pint, mile, yard, foot, inch")
        unit_measurement = {"m3":1, "km3": 0.001**3, "cm3":100**3, "mm3": 1000**3, "l": 1000, "ml":1000000, "gallon":264.17217686, "quart":1056.6887074, "pint":2113.3774149,"mile3":0.0006213689**3, "yard3":1.0936132983**3, "foot3":3.280839895**3, "inch3":39.37007874**3}
        while True:
            frm = input("From: ").lower()
            to = input("To: ").lower()
            value = float(input(f"Enter value of {frm}: "))
        
            if frm not in list(unit_measurement.keys()) or to not in unit_measurement.keys():
                print("Invalid input!. Please try again")
            else:
                break
                
        print("Output:")
        print(f"{value} {frm} = {value*unit_measurement[to]/unit_measurement[frm]:.4f} {to}")
        
    elif unit == "WEIGHT":
        
        print("Measurement: g, kg, mg, ton, pound, ounce, carrat")
        unit_measurement = {"g":1, "kg": 1000, "mg": 0.001, "ton": 10**6, "pound": 0.0022046244, "ounce": 0.0352739907, "carrat": 5}
        while True:
            frm = input("From: ").lower()
            to = input("To: ").lower()
            value = float(input(f"Enter value of {frm}: "))
        
            if frm not in list(unit_measurement.keys()) or to not in unit_measurement.keys():
                print("Invalid input!. Please try again")
            else:
                break
                
        print("Output:")
        print(f"{value} {frm} = {value*unit_measurement[to]/unit_measurement[frm]:.4f} {to}")
            
    elif unit == "TIME":
        
        print("Measurement: s, ms, min, h, d, w, m, y")
        unit_measurement = {"s": 3600, "ms": 3600000, "min": 60, "h": 1, "d": 1/24, "w": 1/24*7, "m": 1/24*30, "y": 1/24*365}
        while True:
            frm = input("From: ").lower()
            to = input("To: ").lower()
            value = float(input(f"Enter value of {frm}: "))
        
            if frm not in list(unit_measurement.keys()) or to not in unit_measurement.keys():
                print("Invalid input!. Please try again")
            else:
                break
                
        print("Output:")
        print(f"{value} {frm} = {value*unit_measurement[to]/unit_measurement[frm]:.4f} {to}")
            
    # Ask user to conitnue or not
    try:
        rep = int(input("Press 1 to continue: "))
    except valueError:
        break


  