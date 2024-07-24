while True:
    print("Unit Converter\n1. Kilometer -> Meter\n2. Celsius -> Fahrenheit\n3. Square KiloMeter -> Hectare\n4. CubitMeter -> Liter \n5. Kilogram -> Gram\n6. Day -> Second")
    print("Please choose the unit you want to convert")
    choose = int(input())
    print("Numer: ")
    num = float(input())

    if choose == 1:
        meter = num * 1000
        print(f"{num}Km is equal to {meter}m")
        continue
    elif choose == 2:
        celsius = float(num)
        fahrenheit = celsius_to_fahrenheit(celsius) #If you want to use any function from another library, you have to called it from the beginning. 
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        continue
    elif choose == 3:
        ha = 100*num
        print(f"{num} Square Kilometer is equal to {ha}ha")
        continue
    elif choose == 4:
        lit = 1000*num
        print(f"{num} Cubic Meter is equal to {lit}Liter")
        continue
    elif choose == 5:
        gram = num* 1000
        print(f"{num}Kg is equal to {gram}g")
        continue
    elif choose == 6:
        second = num * 86400
        print(f"{num} days is equal to {second}s")
        continue
    else:
        print("Error type of choose")
        continue

# This project requires you to convert between a pair, which means from KM -> M and from M -> KM. So you have 5 conversions = 2.5 pairs, which does not satisfies the requiremnt.