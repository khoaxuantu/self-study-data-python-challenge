def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Light Year": 9.461e+15
    }
    
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None

def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "Square Meter": 1,
        "Square Kilometer": 1e+6,
        "Square Centimeter": 1e-4,
        "Square Millimeter": 1e-6,
        "Square Micrometer": 1e-12,
        "Hectare": 10000,
        "Square Mile": 2.59e+6,
        "Square Yard": 0.836127,
        "Square Foot": 0.092903,
        "Square Inch": 0.00064516,
        "Acre": 4046.86
    }
    
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "Cubic Meter": 1,
        "Cubic Kilometer": 1e+9,
        "Cubic Centimeter": 1e-6,
        "Cubic Millimeter": 1e-9,
        "Liter": 0.001,
        "Milliliter": 1e-6,
        "US Gallon": 0.00378541,
        "US Quart": 0.000946353,
        "US Pint": 0.000473176,
        "US Cup": 0.00024,
        "US Fluid Ounce": 2.9574e-5,
        "US Table Spoon": 1.4787e-5,
        "US Tea Spoon": 4.9289e-6,
        "Imperial Gallon": 0.00454609,
        "Imperial Quart": 0.00113652,
        "Imperial Pint": 0.000568261,
        "Imperial Fluid Ounce": 2.8413e-5,
        "Imperial Table Spoon": 1.775e-5,
        "Imperial Tea Spoon": 5.9194e-6,
        "Cubic Mile": 4.168e+9,
        "Cubic Yard": 0.764555,
        "Cubic Foot": 0.0283168,
        "Cubic Inch": 1.6387e-5
    }
    
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Metric Ton": 1000,
        "Long Ton": 1016.05,
        "Short Ton": 907.185,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Carrat": 0.0002,
        "Atomic Mass Unit": 1.66054e-27
    }
    
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "Second": 1,
        "Millisecond": 1e-3,
        "Microsecond": 1e-6,
        "Nanosecond": 1e-9,
        "Picosecond": 1e-12,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2.628e+6,
        "Year": 3.154e+7
    }
    
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def main():
    while True:
        print("Select Unit Converter:")
        print("1. Length")
        print("2. Temperature")
        print("3. Area")
        print("4. Volume")
        print("5. Weight")
        print("6. Time")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '7':
            break

        value = float(input("Value convert: "))
        from_unit = input("From: ")
        to_unit = input("To: ")

        if choice == '1':
            result = convert_length(value, from_unit, to_unit)
        elif choice == '2':
            result = convert_temperature(value, from_unit, to_unit)
        elif choice == '3':
            result = convert_area(value, from_unit, to_unit)
        elif choice == '4':
            result = convert_volume(value, from_unit, to_unit)
        elif choice == '5':
            result = convert_weight(value, from_unit, to_unit)
        elif choice == '6':
            result = convert_time(value, from_unit, to_unit)
        else:
            print("Invalid choice!")
            continue

        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}")
        else:
            print("Invalid units!")

if __name__ == "__main__":
    main()

# Reviewer: Noice! You overkill it

