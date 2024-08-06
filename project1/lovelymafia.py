converter_dict = {
    "length": {
        "meter": 1,
        "kilometer": 1e-3,
        "centimeter": 1e2,
        "millimeter": 1e3,
        "micrometer": 1e6,
        "nanometer": 1e9,
        "mile": 0.0006213689,
        "yard": 1.0936132983,
        "foot": 3.280839895,
        "inch": 39.37007874,
        "light year": 1.057008707e-16,
    },
    "temperature": {"celsius": 1, "fahrenheit": 33.8, "kelvin": 274.15},
    "weight": {
        "kilogram": 1,
        "gram": 1e3,
        "milligram": 1e6,
        "metric ton": 1e-3,
        "long ton": 0.0009842073,
        "short ton": 0.0011023122,
        "pound": 2.2046244202,
        "ounce": 35.273990723,
        "carrat": 5000,
        "atomic mass unit": 6.022136652e26,
    },
    "time": {
        "second": 1,
        "millisecond": 1e3,
        "microsecond": 1e6,
        "nanosecond": 1e9,
        "picosecond": 1e12,
        "minute": 0.0166666667,
        "hour": 0.0002777778,
        "day": 1.157407407e-5,
        "week": 1.653439153e-6,
        "month": 3.802570537e-7,
        "year": 3.168808781e-8,
    },
    "area": {
        "square meter": 1,
        "square kilometer": 1e-6,
        "square centimeter": 1e4,
        "square millimeter": 1e6,
        "hectare": 1e-4,
        "acre": 0.0002471054,
        "square mile": 3.861021585e-7,
        "square yard": 1.1959900463,
        "square foot": 10.7639104167,
        "square inch": 1550.0031000062,
    },
    "volume": {
        "cubic meter": 1,
        "cubic kilometer": 1e-9,
        "cubic centimeter": 1e6,
        "cubic millimeter": 1e9,
        "liter": 1e3,
        "milliliter": 1e6,
        "us gallon": 264.1720523581,
        "us quart": 1056.6882094325,
        "us pint": 2113.376418865,
        "us cup": 4226.75283773,
        "us fluid ounce": 33814.022699494,
        "us table spoon": 67628.045398988,
        "us tea spoon": 202884.13619696,
        "imperial gallon": 219.9692483,
        "imperial quart": 879.8769932,
        "imperial pint": 1759.7539864,
        "imperial fluid ounce": 35195.0797272,
        "imperial table spoon": 56312.12756352,
        "imperial tea spoon": 168936.38269056,
        "cubic mile": 2.3991275858e-10,
        "cubic yard": 1.3079506193,
        "cubic foot": 35.3146667215,
        "cubic inch": 61023.744094732
    },
}

def convert(converter, fromUnit, toUnit, value):
    converter = converter.lower()
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    assert ( # Reviewer: Lovely! Great to see some asserts here. Would be better if you use them with except then
        converter in converter_dict
    ), f"Invalid converter, only support: {', '.join(converter_dict.keys())}"
    assert (
        fromUnit in converter_dict[converter]
    ), f"Invalid fromUnit of {converter} converter, only support: {', '.join(converter_dict[converter].keys())}"
    assert (
        toUnit in converter_dict[converter]
    ), f"Invalid toUnit of {converter} converter, only support: {', '.join(converter_dict[converter].keys())}"
    return (
        value * converter_dict[converter][toUnit] / converter_dict[converter][fromUnit]
    )
    
def interface():
    print("Welcome to the Unit Converter!")
    converter = input(f"Enter the converter you want to use ({', '.join(converter_dict.keys())})")
    fromUnit = input(f"Enter the Starting Unit of Measurement ({', '.join(converter_dict[converter].keys())})")
    toUnit = input(f"Enter the Unit of Measurement to Convert to ({', '.join(converter_dict[converter].keys())})")
    value = float(input(f"Enter the Starting Measurement in {fromUnit.lower().title()}: "))
    convert_value = convert(converter, fromUnit, toUnit, value)
    print(f"Result: {value} {fromUnit.lower().title()} = {convert_value} {toUnit.lower().title()}")

interface()

# Reviewer: Noice. You overkill it :)

