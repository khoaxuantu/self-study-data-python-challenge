def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'inches': 0.0254,
        'feet': 0.3048
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        'square_meters': 1,
        'square_kilometers': 1e6,
        'square_feet': 0.092903,
        'acres': 4046.86
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic_meters': 1000,
        'gallons': 3.78541
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_units(value, from_unit, to_unit, unit_type):
    if unit_type == 'length':
        return convert_length(value, from_unit, to_unit)
    elif unit_type == 'temperature':
        return convert_temperature(value, from_unit, to_unit)
    elif unit_type == 'weight':
        return convert_weight(value, from_unit, to_unit)
    elif unit_type == 'area':
        return convert_area(value, from_unit, to_unit)
    elif unit_type == 'volume':
        return convert_volume(value, from_unit, to_unit)
    elif unit_type == 'time':
        return convert_time(value, from_unit, to_unit)
    else:
        raise ValueError("Unsupported unit type")

def main():
    while True:
        print("Welcome to Unit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Area")
        print("5. Volume")
        print("6. Time")
        
        choice = int(input("Select the type of conversion (1/2/3/4/5/6): "))
        
        unit_types = {
            1: 'length',
            2: 'weight',
            3: 'temperature',
            4: 'area',
            5: 'volume',
            6: 'time'
        }
        
        conversions = {
            'length': [
                ('Meters to Kilometers', 'meters', 'kilometers'),
                ('Kilometers to Meters', 'kilometers', 'meters'),
                ('Inches to Feet', 'inches', 'feet'),
                ('Feet to Inches', 'feet', 'inches')
            ],
            'weight': [
                ('Grams to Kilograms', 'grams', 'kilograms'),
                ('Kilograms to Grams', 'kilograms', 'grams'),
                ('Pounds to Ounces', 'pounds', 'ounces'),
                ('Ounces to Pounds', 'ounces', 'pounds')
            ],
            'temperature': [
                ('Celsius to Fahrenheit', 'celsius', 'fahrenheit'),
                ('Fahrenheit to Celsius', 'fahrenheit', 'celsius'),
                ('Celsius to Kelvin', 'celsius', 'kelvin'),
                ('Kelvin to Celsius', 'kelvin', 'celsius')
            ],
            'area': [
                ('Square Meters to Square Kilometers', 'square_meters', 'square_kilometers'),
                ('Square Kilometers to Square Meters', 'square_kilometers', 'square_meters'),
                ('Square Feet to Acres', 'square_feet', 'acres'),
                ('Acres to Square Feet', 'acres', 'square_feet')
            ],
            'volume': [
                ('Liters to Milliliters', 'liters', 'milliliters'),
                ('Milliliters to Liters', 'milliliters', 'liters'),
                ('Cubic Meters to Gallons', 'cubic_meters', 'gallons'),
                ('Gallons to Cubic Meters', 'gallons', 'cubic_meters')
            ],
            'time': [
                ('Seconds to Minutes', 'seconds', 'minutes'),
                ('Minutes to Seconds', 'minutes', 'seconds'),
                ('Hours to Days', 'hours', 'days'),
                ('Days to Hours', 'days', 'hours')
            ]
        }
        
        unit_type = unit_types.get(choice)
        
        if not unit_type:
            print("Invalid choice. Please select a valid option.")
            continue
        
        while True:
            print(f"\nSelected conversion type: {unit_type.capitalize()}")
            for i, (desc, _, _) in enumerate(conversions[unit_type], start=1):
                print(f"{i}. {desc}")
            
            # Reviewer:
            # Caught a small bug here :)
            conversion_choice = int(input(f"Select conversion (1/{'/'.join(map(str, range(1, len(conversions[unit_type]) + 1)))}): "))
            
            if conversion_choice < 1 or conversion_choice > len(conversions[unit_type]):
                print("Invalid conversion choice. Please select a valid option.")
                continue
            
            desc, from_unit, to_unit = conversions[unit_type][conversion_choice - 1]
            
            value = float(input(f"Enter the value to convert: "))
            
            try:
                result = convert_units(value, from_unit, to_unit, unit_type)
                print(f"{value} {from_unit} is equal to {result} {to_unit}")
            except ValueError as e:
                print(e)

            another_conversion = input("Do you want to perform another conversion in this category? (yes/no): ").lower()
            if another_conversion != 'yes':
                break
        
        another_category = input("Do you want to select another conversion category? (yes/no): ").lower()
        if another_category != 'yes':
            print("Thank you for using the Unit Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()

# Reviewer: Noice. You overkill it :)

