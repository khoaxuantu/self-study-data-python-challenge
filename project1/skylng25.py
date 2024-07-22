def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60934

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet * 0.3048

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km_to_miles(km)
        print(f"{km} kilometers is equal to {miles:.2f} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles_to_km(miles)
        print(f"{miles} miles is equal to {km:.2f} kilometers")
    elif choice == '3':
        meters = float(input("Enter distance in meters: "))
        feet = meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet:.2f} feet")
    elif choice == '4':
        feet = float(input("Enter distance in feet: "))
        meters = feet_to_meters(feet)
        print(f"{feet} feet is equal to {meters:.2f} meters")
    elif choice == '5':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == '6':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

# Noice

