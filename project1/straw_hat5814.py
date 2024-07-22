unit1 = input("Enter Starting Unit of Measurement (kilometer, meter, decimeter, centimeter, millimeter, micrometer): ")
unit2 = input("Enter Unit of Measurement to Convert to (kilometer, meter, decimeter, centimeter, millimeter, micrometer): ")
num1 = float(input(f"Enter Starting Measurement in {unit1}: "))

# Define conversion factors
conversion_factors = {
    'kilometer': {
        'meter': 1000,
        'centimeter': 100000,
        'millimeter': 1000000,
        'micrometer': 1000000000
    },
    'meter': {
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'micrometer': 1000000
    },
    'decimeter': {
        'meter': 0.1,
        'centimeter': 10,
        'millimeter': 100,
        'micrometer': 100000
    },
    'centimeter': {
        'kilometer': 0.00001,
        'meter': 0.01,
        'millimeter': 10,
        'micrometer': 10000
    },
    'millimeter': {
        'kilometer': 0.000001,
        'meter': 0.001,
        'centimeter': 0.1,
        'micrometer': 1000
    },
    'micrometer': {
        'kilometer': 0.000000001,
        'meter': 0.000001,
        'centimeter': 0.0001,
        'millimeter': 0.001
    }
}

# Perform conversion
if unit1 in conversion_factors and unit2 in conversion_factors[unit1]:
    ans = num1 * conversion_factors[unit1][unit2]
    print(f"Result: {num1} {unit1} = {ans} {unit2}")
else:
    print("Invalid units entered or conversion not supported.")

# Noice

