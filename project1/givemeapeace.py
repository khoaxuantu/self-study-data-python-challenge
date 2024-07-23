def get_unit_category():
    categories = ["temperature", "length", "weight", "time", "area", "volume"] # 6 type of convert unit
    while True:
        print(f"Choose unit category {tuple(categories)}:")
        choice = input().lower()
        if choice in categories:
            return choice
        print("Invalid category. Please choose from the list.")

def get_units(category):
    units = {
        "temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "length": ["Meter", "Centimeter", "Millimeter", "Kilometer", "Inch", "Foot", "Yard", "Mile"],
        "weight": ["Kilogram", "Gram", "Milligram", "Ton", "Pound", "Ounce"],
        "time": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        "area": ["SquareMeter", "SquareKilometer", "Hectare", "Acre", "SquareFoot", "SquareInch"],
        "volume": ["CubicMeter", "Liter", "Milliliter", "Gallon", "Quart", "Pint", "CubicFoot", "CubicInch"]
    }
    return units.get(category, [])

def convert_unit(value, from_unit, to_unit, category):
    if category == "temperature":
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
    else:
        base_units = {
            "length": "Meter",
            "weight": "Kilogram",
            "time": "Second",
            "area": "SquareMeter",
            "volume": "CubicMeter"
        }
        
        conversion_factors = {
            "length": {"Meter": 1, "Centimeter": 0.01, "Millimeter": 0.001, "Kilometer": 1000, 
                       "Inch": 0.0254, "Foot": 0.3048, "Yard": 0.9144, "Mile": 1609.34},
            "weight": {"Kilogram": 1, "Gram": 0.001, "Milligram": 1e-6, "Ton": 1000, 
                       "Pound": 0.453592, "Ounce": 0.0283495},
            "time": {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, 
                     "Week": 604800, "Month": 2592000, "Year": 31536000},
            "area": {"SquareMeter": 1, "SquareKilometer": 1e6, "Hectare": 10000, 
                     "Acre": 4046.86, "SquareFoot": 0.092903, "SquareInch": 0.00064516},
            "volume": {"CubicMeter": 1, "Liter": 0.001, "Milliliter": 1e-6, 
                       "Gallon": 0.00378541, "Quart": 0.000946353, "Pint": 0.000473176, 
                       "CubicFoot": 0.0283168, "CubicInch": 1.63871e-5}
        }
        
        base_value = value * conversion_factors[category][from_unit]
        return base_value / conversion_factors[category][to_unit]

    return value  # If no conversion was done (same unit)

def main():
    while True:
        category = get_unit_category()
        available_units = get_units(category)
        
        print(f"Available units: {', '.join(available_units)}")
        
        while True:
            source_unit = input("Enter the source unit: ")
            if source_unit in available_units:
                break
            print(f"Invalid unit. Please choose from the available units: {', '.join(available_units)}")
        
        print(f"Available target units: {', '.join(available_units)}")
        
        while True:
            target_unit = input("Enter the target unit: ")
            if target_unit in available_units:
                break
            print(f"Invalid unit. Please choose from the available units: {', '.join(available_units)}")
        
        while True:
            try:
                value = float(input("Enter the value to convert: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.") #handle when entering the wrong type to prevent crash
        
        result = convert_unit(value, source_unit, target_unit, category)
        
        if result is not None:
            print(f"{value} {source_unit} = {result:.2f} {target_unit}")
        else:
            print("Conversion not available for the selected category.")
        
        while True:
            choice = input("Do you want to perform another conversion? (yes/no): ").lower()
            if choice in ['yes', 'no']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if choice != 'yes':
            print("End")
            print("Please start the convert again to reconvert")
            break

if __name__ == "__main__":
    main()

# Reviewer: Noice, you overkill it :)

