def convert_length(value, from_unit, to_unit):
    length_units = {
        'inches': 1,
        'feet': 1/12,
        'yards': 1/36
    }

    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])
    else:
        return None

def convert_mass(value, from_unit, to_unit):
    mass_units = {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }

    if from_unit in mass_units and to_unit in mass_units:
        return value * (mass_units[to_unit] / mass_units[from_unit])
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
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
    return None

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liters': 1,
        'milliliters': 1000,
        'gallons': 0.264172,
        'cups': 4.22675
    }

    if from_unit in volume_units and to_unit in volume_units:
        return value * (volume_units[to_unit] / volume_units[from_unit])
    else:
        return None

def convert_time(value, from_unit, to_unit):
    time_units = {
        'seconds': 1,
        'minutes': 1/60,
        'hours': 1/3600,
        'days': 1/86400
    }

    if from_unit in time_units and to_unit in time_units:
        return value * (time_units[to_unit] / time_units[from_unit])
    else:
        return None

def convert_area(value, from_unit, to_unit):
    area_units = {
        'square meters': 1,
        'square kilometers': 0.000001,
        'acres': 0.000247105,
        'hectares': 0.0001
    }

    if from_unit in area_units and to_unit in area_units:
        return value * (area_units[to_unit] / area_units[from_unit])
    else:
        return None

def get_conversion_function(unit_type):
    if unit_type == 'length':
        return convert_length
    elif unit_type == 'mass':
        return convert_mass
    elif unit_type == 'temperature':
        return convert_temperature
    elif unit_type == 'volume':
        return convert_volume
    elif unit_type == 'time':
        return convert_time
    elif unit_type == 'area':
        return convert_area
    else:
        return None

def main():
    unit_type = input("Enter Type of Measurement (length, mass, temperature, volume, time, area): ").strip().lower()
    from_unit = input(f"Enter Starting Unit of Measurement ({unit_type}): ").strip().lower()
    to_unit = input(f"Enter Unit of Measurement to Convert to ({unit_type}): ").strip().lower()
    value = float(input(f"Enter Starting Measurement in {from_unit.capitalize()}: "))

    convert_function = get_conversion_function(unit_type)
    if convert_function:
        result = convert_function(value, from_unit, to_unit)
        if result is not None:
            print(f"Result: {value} {from_unit.capitalize()} = {result} {to_unit.capitalize()}")
        else:
            print("Invalid units of measurement entered.")
    else:
        print("Invalid type of measurement entered.")

if __name__ == "__main__":
    main()


# Reviewer: Noice

