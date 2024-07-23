# LENGTHS CONVERTER
length = {
    'Centimeter': {
        'Centimeter': 1,
        'Meter': 0.01,
        'Kilometer': 0.00001,
        'Inch': 0.3937007874,
        'Feet': 0.032808399,
        'Mile': 0.0000062137,
        'Yard': 0.010936133,
        'Light Year': 1.057008707E-18
    },
    'Meter': {
        'Centimeter': 100,
        'Meter': 1,
        'Kilometer': 0.001,
        'Inch': 39.37007874,
        'Feet': 3.280839895,
        'Mile': 0.0006213689,
        'Yard': 1.0936132983,
        'Light Year': 1.057008707E-16
    },
    'Kilometer': {
        'Centimeter': 100000,
        'Meter': 1000,
        'Kilometer': 1,
        'Inch': 39370.07874,
        'Feet': 3280.839895,
        'Mile': 0.6213688756,
        'Yard': 1093.6132983,
        'Light Year': 1.057008707E-13
    },
    'Inch': {
        'Centimeter': 2.54,
        'Meter': 0.0254,
        'Kilometer': 0.0000254,
        'Inch': 1,
        'Feet': 0.0833333333,
        'Mile': 0.0000157828,
        'Yard': 0.0277777778,
        'Light Year': 2.684802117E-18
    },
    'Feet': {
        'Centimeter': 30.48,
        'Meter': 0.3048,
        'Kilometer': 0.0003048,
        'Inch': 12,
        'Feet': 1,
        'Mile': 0.0001893932,
        'Yard': 0.3333333333,
        'Light Year': 3.22176254E-17
    },
    'Mile': {
        'Centimeter': 160935,
        'Meter': 1.60935,
        'Kilometer': 1.6093439799,
        'Inch': 63360.23622,
        'Feet': 5280.019685,
        'Mile': 1,
        'Yard': 1760.0065617,
        'Light Year': 1.701096963E-13
    },
    'Yard': {
        'Centimeter': 91.44,
        'Meter': 0.9144,
        'Kilometer': 0.0009144,
        'Inch': 36,
        'Feet': 3,
        'Mile': 0.0005681797,
        'Yard': 1,
        'Light Year': 9.665287622E-17
    },
    'Light Year': {
        'Centimeter': 946066000000000000,
        'Meter': 9460660000000000,
        'Kilometer': 9460660000000,
        'Inch': 372466929133858300,
        'Feet': 31038910761154856,
        'Mile': 5878559666946,
        'Yard': 10346303587051618,
        'Light Year': 1
    }
}

for unit in length:
    print(unit)
from_unit = input("Enter from unit: ")
to_unit = input("Enter to unit: ")
value = float(input(f"Enter the value in {from_unit}: "))
converted_value = value * length[from_unit][to_unit]
print(f"{value} {from_unit} is equal to {converted_value} {to_unit}.")

# Reviewer: Noice

