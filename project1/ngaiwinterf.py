def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'yards': 1.09361
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

# Ví dụ sử dụng
length_conversion = convert_length(10, 'meters', 'kilometers')
mass_conversion = convert_mass(5, 'kilograms', 'pounds')
temp_conversion_c_to_f = convert_temperature(100, 'Celsius', 'Fahrenheit')
length_conversion_miles_to_yards = convert_length(1, 'miles', 'yards')
mass_conversion_grams_to_ounces = convert_mass(200, 'grams', 'ounces')
temp_conversion_k_to_c = convert_temperature(273.15, 'Kelvin', 'Celsius')
volume_conversion = convert_volume(2, 'liters', 'gallons')
time_conversion = convert_time(3600, 'seconds', 'hours')
area_conversion = convert_area(10000, 'square meters', 'acres')

print("10 meters to kilometers:", length_conversion)
print("5 kilograms to pounds:", mass_conversion)
print("100 Celsius to Fahrenheit:", temp_conversion_c_to_f)
print("1 mile to yards:", length_conversion_miles_to_yards)
print("200 grams to ounces:", mass_conversion_grams_to_ounces)
print("273.15 Kelvin to Celsius:", temp_conversion_k_to_c)
print("2 liters to gallons:", volume_conversion)
print("3600 seconds to hours:", time_conversion)
print("10000 square meters to acres:", area_conversion)

# Noice

