class UnitConverter:
    """
    Reviewer:
    Dude we have not reached the OOP topic -_-
    But overally, I don't think your are truly OOP here. It looks like you are just using class more
    """
    def __init__(self):
        self.conversions = {
            'temperature': {
                'Celsius': 1.0,
                'Fahrenheit': 5/9,
                'Kelvin': 1.0
            },
            'length': {
                'Meter': 1.0,
                'Centimeter': 0.01,
                'Millimeter': 0.001,
                'Kilometer': 1000.0,
                'Inch': 0.0254,
                'Feet': 0.3048,
                'Yard': 0.9144,
                'Mile': 1609.34,
                'Nanometer': 1e-9,
                'LightYear': 9.461e15
            },
            'weight': {
                'Gram': 1.0,
                'Kilogram': 1000.0,
                'Pound': 453.592,
                'Ounce': 28.3495,
                'Ton': 1e6
            },
            'time': {
                'Second': 1.0,
                'Minute': 60.0,
                'Hour': 3600.0,
                'Day': 86400.0,
                'Week': 604800.0,
                'Month': 2.628e6,  # Average month (30.44 days)
                'Year': 3.154e7  # Average year (365.25 days)
            },
            'area': {
                'SquareMeter': 1.0,
                'SquareKilometer': 1e6,
                'SquareMile': 2.59e6,
                'SquareCentimeter': 1e-4,
                'SquareFoot': 0.092903,
                'SquareYard': 0.836127,
                'Acre': 4046.86
            },
            'volume': {
                'Liter': 1.0,
                'Milliliter': 0.001,
                'CubicMeter': 1000.0,
                'Gallon': 3.78541,
                'Quart': 0.946353,
                'Pint': 0.473176,
                'Cup': 0.236588
            }
        }

    def convert(self, from_unit, to_unit, value, category):
        if category not in self.conversions:
            raise ValueError("Invalid unit category.")
        
        if from_unit not in self.conversions[category] or to_unit not in self.conversions[category]:
            raise ValueError("Invalid units for this category.")
        
        # Handle temperature conversions separately
        # Reviewer: I swear if you use OOP truely, you don't need any of these if...else :)
        if category == 'temperature':
            if from_unit == 'Celsius':
                if to_unit == 'Fahrenheit':
                    return (value * 9/5) + 32
                elif to_unit == 'Kelvin':
                    return value + 273.15
            elif from_unit == 'Fahrenheit':
                if to_unit == 'Celsius':
                    return (value - 32) * 5/9
                elif to_unit == 'Kelvin':
                    return (value - 32) * 5/9 + 273.15
            elif from_unit == 'Kelvin':
                if to_unit == 'Celsius':
                    return value - 273.15
                elif to_unit == 'Fahrenheit':
                    return (value - 273.15) * 9/5 + 32

        # For other units
        base_unit_from = self.conversions[category][from_unit]
        base_unit_to = self.conversions[category][to_unit]
        return value * (base_unit_from / base_unit_to)

    # Reviewer:
    # Erm... What is the purpose of the user_input method inside the class `UnitConverter`?
    # Why we don't lift the input operations out of the class? Just let the `UnitConverter` do the converting units
    def user_input(self):
        while True:
            category = input("Choose unit category (temperature, length, weight, time, area, volume): ")
            if category not in self.conversions:
                print("Invalid unit category.")
                continue

            units = list(self.conversions[category].keys())
            print(f"Available units: {', '.join(units)}")
            
            from_unit = input("Enter the source unit: ")
            if from_unit not in units:
                print("Invalid source unit.")
                continue
            
            remaining_units = [unit for unit in units if unit != from_unit]
            print(f"Available target units: {', '.join(remaining_units)}")
            
            to_unit = input("Enter the target unit: ")
            if to_unit not in remaining_units:
                print("Invalid target unit.")
                continue

            value = float(input("Enter the value to convert: "))
            try:
                result = self.convert(from_unit, to_unit, value, category)
                print(f"{value} {from_unit} = {result} {to_unit}")
            except ValueError as e:
                print(e)

            # Ask if the user wants to perform another conversion
            again = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Troll Troll!!")
                break

# Using the UnitConverter class
converter = UnitConverter()
converter.user_input()

