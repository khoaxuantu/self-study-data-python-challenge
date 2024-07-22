#so many def its a dictionary 
def meters_to_feet(meters):
    return meters * 3.28084

def meters_to_miles(meters):
    return meters * 0.000621371

def meters_to_inches(meters):
    return meters * 39.3701

def meters_to_centimeters(meters):
    return meters * 100

def meters_to_kilometers(meters):
    return meters * 0.001

def feet_to_meters(feet):
    return feet / 3.28084

def feet_to_miles(feet):
    return feet * 0.000189394

def feet_to_inches(feet):
    return feet * 12

def feet_to_centimeters(feet):
    return feet * 30.48

def feet_to_kilometers(feet):
    return feet * 0.0003048

def miles_to_meters(miles):
    return miles / 0.000621371

def miles_to_feet(miles):
    return miles / 0.000189394

def miles_to_inches(miles):
    return miles * 63360

def miles_to_centimeters(miles):
    return miles * 160934

def miles_to_kilometers(miles):
    return miles * 1.60934

def inches_to_meters(inches):
    return inches * 0.0254

def inches_to_feet(inches):
    return inches / 12

def inches_to_miles(inches):
    return inches / 63360

def inches_to_centimeters(inches):
    return inches * 2.54

def inches_to_kilometers(inches):
    return inches * 0.0000254

def centimeters_to_meters(centimeters):
    return centimeters * 0.01

def centimeters_to_feet(centimeters):
    return centimeters / 30.48

def centimeters_to_miles(centimeters):
    return centimeters / 160934

def centimeters_to_inches(centimeters):
    return centimeters * 0.393701

def centimeters_to_kilometers(centimeters):
    return centimeters * 0.00001

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def kilometers_to_feet(kilometers):
    return kilometers / 0.0003048

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def kilometers_to_inches(kilometers):
    return kilometers / 0.0000254

def kilometers_to_centimeters(kilometers):
    return kilometers * 100000

def main():
    conversions = {
        ('meters', 'feet'): meters_to_feet,
        ('meters', 'miles'): meters_to_miles,
        ('meters', 'inches'): meters_to_inches,
        ('meters', 'centimeters'): meters_to_centimeters,
        ('meters', 'kilometers'): meters_to_kilometers,
        ('feet', 'meters'): feet_to_meters,
        ('feet', 'miles'): feet_to_miles,
        ('feet', 'inches'): feet_to_inches,
        ('feet', 'centimeters'): feet_to_centimeters,
        ('feet', 'kilometers'): feet_to_kilometers,
        ('miles', 'meters'): miles_to_meters,
        ('miles', 'feet'): miles_to_feet,
        ('miles', 'inches'): miles_to_inches,
        ('miles', 'centimeters'): miles_to_centimeters,
        ('miles', 'kilometers'): miles_to_kilometers,
        ('inches', 'meters'): inches_to_meters,
        ('inches', 'feet'): inches_to_feet,
        ('inches', 'miles'): inches_to_miles,
        ('inches', 'centimeters'): inches_to_centimeters,
        ('inches', 'kilometers'): inches_to_kilometers,
        ('centimeters', 'meters'): centimeters_to_meters,
        ('centimeters', 'feet'): centimeters_to_feet,
        ('centimeters', 'miles'): centimeters_to_miles,
        ('centimeters', 'inches'): centimeters_to_inches,
        ('centimeters', 'kilometers'): centimeters_to_kilometers,
        ('kilometers', 'meters'): kilometers_to_meters,
        ('kilometers', 'feet'): kilometers_to_feet,
        ('kilometers', 'miles'): kilometers_to_miles,
        ('kilometers', 'inches'): kilometers_to_inches,
        ('kilometers', 'centimeters'): kilometers_to_centimeters
    }
    #there has to be a better way to do this lol
    print("Welcome to Wendys, what do you want?")
    print("1. Meters to Feet")
    print("2. Meters to Miles")
    print("3. Meters to Inches")
    print("4. Meters to Centimeters")
    print("5. Meters to Kilometers")
    print("6. Feet to Meters")
    print("7. Feet to Miles")
    print("8. Feet to Inches")
    print("9. Feet to Centimeters")
    print("10. Feet to Kilometers")
    print("11. Miles to Meters")
    print("12. Miles to Feet")
    print("13. Miles to Inches")
    print("14. Miles to Centimeters")
    print("15. Miles to Kilometers")
    print("16. Inches to Meters")
    print("17. Inches to Feet")
    print("18. Inches to Miles")
    print("19. Inches to Centimeters")
    print("20. Inches to Kilometers")
    print("21. Centimeters to Meters")
    print("22. Centimeters to Feet")
    print("23. Centimeters to Miles")
    print("24. Centimeters to Inches")
    print("25. Centimeters to Kilometers")
    print("26. Kilometers to Meters")
    print("27. Kilometers to Feet")
    print("28. Kilometers to Miles")
    print("29. Kilometers to Inches")
    print("30. Kilometers to Centimeters")
    print("31. Quit")

    while True:
        choice = input("Enter your menu item (1-31): ")

        if choice == '31':
            print("Bye Felicia.")
            break
        
        if choice not in [str(i) for i in range(1, 32)]:
            print("Sir this is a Wendys. Please enter a number from 1 to 31.\n")
            continue
        
        from_unit, to_unit = {
            '1': ('meters', 'feet'),
            '2': ('meters', 'miles'),
            '3': ('meters', 'inches'),
            '4': ('meters', 'centimeters'),
            '5': ('meters', 'kilometers'),
            '6': ('feet', 'meters'),
            '7': ('feet', 'miles'),
            '8': ('feet', 'inches'),
            '9': ('feet', 'centimeters'),
            '10': ('feet', 'kilometers'),
            '11': ('miles', 'meters'),
            '12': ('miles', 'feet'),
            '13': ('miles', 'inches'),
            '14': ('miles', 'centimeters'),
            '15': ('miles', 'kilometers'),
            '16': ('inches', 'meters'),
            '17': ('inches', 'feet'),
            '18': ('inches', 'miles'),
            '19': ('inches', 'centimeters'),
            '20': ('inches', 'kilometers'),
            '21': ('centimeters', 'meters'),
            '22': ('centimeters', 'feet'),
            '23': ('centimeters', 'miles'),
            '24': ('centimeters', 'inches'),
            '25': ('centimeters', 'kilometers'),
            '26': ('kilometers', 'meters'),
            '27': ('kilometers', 'feet'),
            '28': ('kilometers', 'miles'),
            '29': ('kilometers', 'inches'),
            '30': ('kilometers', 'centimeters')
        }[choice]

        try:
            value = float(input(f"Enter length in {from_unit}: "))
            result = conversions[(from_unit, to_unit)](value)
            print(f"{value} {from_unit} = {result} {to_unit}\n")
        except ValueError:
            print("Sir this is a Wendys. Please enter a number from 1 to 31.\n")

if __name__ == "__main__":
    main()

# Too long don't read :)

