"""
Bị xiên bởi: Tusss (https://github.com/khoaxuantu)
"""

# Conversion factors for length (to meters)
length_conversion_to_base = {
    'meter': 1.0,
    'kilometer': 1000.0,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'micrometer': 1e-6,
    'nanometer': 1e-9,
    'mile': 1609.34,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
    'light year': 9.461e+15
}

# Conversion factors for temperature
def convert_temperature(val, from_unit, to_unit):
    if from_unit == to_unit:
        return val
    # Convert to Celsius first
    if from_unit == 'celsius':
        temp_celsius = val
    elif from_unit == 'fahrenheit':
        temp_celsius = (val - 32) * 5/9
    elif from_unit == 'kelvin':
        temp_celsius = val - 273.15
    else:
        raise ValueError("Unsupported temperature unit")

    # Convert from Celsius to target unit
    if to_unit == 'celsius':
        return temp_celsius
    elif to_unit == 'fahrenheit':
        return temp_celsius * 9/5 + 32
    elif to_unit == 'kelvin':
        return temp_celsius + 273.15
    else:
        raise ValueError("Unsupported temperature unit")

# Conversion factors for area (to square meters)
area_conversion_to_base = {
    'square meter': 1.0,
    'square kilometer': 1e6,
    'square centimeter': 1e-4,
    'square millimeter': 1e-6,
    'square micrometer': 1e-12,
    'hectare': 1e4,
    'square mile': 2.58999e6,
    'square yard': 0.836127,
    'square foot': 0.092903,
    'square inch': 0.00064516,
    'acre': 4046.86
}

# Conversion factors for volume (to cubic meters)
volume_conversion_to_base = {
    'cubic meter': 1.0,
    'cubic kilometer': 1e9,
    'cubic centimeter': 1e-6,
    'cubic millimeter': 1e-9,
    'liter': 1e-3,
    'milliliter': 1e-6,
    'us gallon': 3.78541e-3,
    'us quart': 9.46352e-4,
    'us pint': 4.73176e-4,
    'us cup': 2.36588e-4,
    'us fluid ounce': 2.95735e-5,
    'us table spoon': 1.47868e-5,
    'us tea spoon': 4.92892e-6,
    'imperial gallon': 4.54609e-3,
    'imperial quart': 1.13652e-3,
    'imperial pint': 5.6826e-4,
    'imperial fluid ounce': 1.042e-4,
    'imperial table spoon': 5.21e-5,
    'imperial tea spoon': 1.73333e-5,
    'cubic mile': 4.16818e9,
    'cubic yard': 0.764555,
    'cubic foot': 2.83168e-2,
    'cubic inch': 1.63871e-5
}

# Conversion factors for weight (to kilograms)
weight_conversion_to_base = {
    'kilogram': 1.0,
    'gram': 1e-3,
    'milligram': 1e-6,
    'microgram': 1e-9,
    'pound': 0.453592,
    'ounce': 0.0283495,
    'stone': 6.35029,
    'carat': 2e-4,
    'ton': 907.185
}

# Conversion factors for time (to seconds)
time_conversion_to_base = {
    'second': 1.0,
    'minute': 60.0,
    'hour': 3600.0,
    'day': 86400.0,
    'week': 604800.0,
    'Month': 2.628e6,  # Average month (30.44 days)
    'Year': 3.154e7  # Average year (365.25 days)
}

def convert(value, from_unit, to_unit, category):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    conversion_factors = {
        'length': length_conversion_to_base,
        'temperature': None,  # Special handling required
        'area': area_conversion_to_base,
        'volume': volume_conversion_to_base,
        'weight': weight_conversion_to_base,
        'time': time_conversion_to_base
    }

    if category == 'temperature':
        return convert_temperature(value, from_unit, to_unit)

    if category not in conversion_factors:
        raise ValueError("Unsupported category")

    factors = conversion_factors[category]
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported unit")

    val_in_base = value * factors[from_unit]
    return val_in_base / factors[to_unit]

if __name__ == "__main__":
    category = input("Enter the category (length, temperature, area, volume, weight, time): ").strip().lower()
    value = float(input("Enter the value: "))
    from_unit = input("Enter the unit to convert from: ").strip().lower() # I need a suggestion for each category :dead:
    to_unit = input("Enter the unit to convert to: ").strip().lower() # Same

    try:
        result = convert(value, from_unit, to_unit, category)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(e)
