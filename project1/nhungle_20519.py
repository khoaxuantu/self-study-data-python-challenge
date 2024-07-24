print("Unit Converter")
print("1. Kilometer -> Meter")
print("2. Celsius -> Fahrenheit")
print("3. Hectare -> Square Meter")
print("4. Milliliter -> Liter")
print("5. Kilogram -> Gram")
print("6. Day -> Second")

q = 'Y'
while q == 'Y':
    while True:
        print("Please choose the unit you want to convert (1-6):")
        try:
            choose = int(input())
    
            if choose == 1:
                print("Number (Kilometer): ")
                num = float(input())
                result = num * 1000  # Convert Kilometer to Meter
                print(f"{num} Kilometer = {result} Meter")
                break
            elif choose == 2:
                print("Number (Celsius): ")
                num = float(input())
                result = num * 9 / 5 + 32  # Convert Celsius to Fahrenheit
                print(f"{num} Celsius = {result} Fahrenheit")
                break
            elif choose == 3:
                print("Number (Hectare): ")
                num = float(input())
                result = num * 10000  # Convert Hectare to Square Meter
                print(f"{num} Hectare = {result} Square Meter")
                break
            elif choose == 4:
                print("Number (Milliliter): ")
                num = float(input())
                result = num / 1000  # Convert Milliliter to Liter
                print(f"{num} Milliliter = {result} Liter")
                break
            elif choose == 5:
                print("Number (Kilogram): ")
                num = float(input())
                result = num * 1000  # Convert Kilogram to Gram
                print(f"{num} Kilogram = {result} Gram")
                break
            elif choose == 6:
                print("Number (Day): ")
                num = float(input())
                result = num * 86400  # Convert Day to Second
                print(f"{num} Day = {result} Second")
                break
            else:
                print("NOT VALID.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    q = input("Continue? Y/N: ").strip().upper()

#Great job, but this project requires you to convert between a pair, which means from KM -> M and from M -> KM. So you have 6 conversions = 3 pairs.