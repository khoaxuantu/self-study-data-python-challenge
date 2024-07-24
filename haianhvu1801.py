#Great job!
def convert_units(value, old_unit, new_unit):
    convert_units = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001}

    if old_unit not in convert_units or new_unit not in convert_units:
        raise ValueError("Invalid length units")

    value_in_meters = value * convert_units[old_unit]
    converted_value = value_in_meters / convert_units[new_unit]

    return converted_value
    
length_in_km = convert_units(500, 'meter', 'kilometer')
print(f"500 meters is {length_in_km} kilometers")
length_in_m = convert_units(1,'kilometer','meter')
print(f"1 kilimeter is {length_in_m} meters")
length_in_centimeter = convert_units(1,'meter','centimeter')
print(f"1 meter is {length_in_centimeter} centimeters")
length_in_millimeter = convert_units(1,'meter','millimeter')
print(f"1 meter is {length_in_millimeter} millimeter")