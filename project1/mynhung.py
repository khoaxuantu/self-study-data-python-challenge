
measure_dict = {
    1: 'Meter',
    2: 'Kilometer',
    3: 'Centimeter',
    4: 'Millimeter',
    5: 'Inch',
    6: 'Yard'
}

conversion_factors = {
    'Meter': {
        'Meter': 1,
        'Kilometer': 0.001,
        'Centimeter': 100,
        'Millimeter': 1000,
        'Inch': 39.3701,
        'Yard': 1.09361
    },
    'Kilometer': {
        'Meter': 1000,
        'Kilometer': 1,
        'Centimeter': 100000,
        'Millimeter': 1000000,
        'Inch': 39370.1,
        'Yard': 1093.61
    },
    'Centimeter': {
        'Meter': 0.01,
        'Kilometer': 0.00001,
        'Centimeter': 1,
        'Millimeter': 10,
        'Inch': 0.393701,
        'Yard': 0.0109361
    },
    'Millimeter': {
        'Meter': 0.001,
        'Kilometer': 0.000001,
        'Centimeter': 0.1,
        'Millimeter': 1,
        'Inch': 0.0393701,
        'Yard': 0.00109361
    },
    'Inch': {
        'Meter': 0.0254,
        'Kilometer': 0.0000254,
        'Centimeter': 2.54,
        'Millimeter': 25.4,
        'Inch': 1,
        'Yard': 0.0277778
    },
    'Yard': {
        'Meter': 0.9144,
        'Kilometer': 0.0009144,
        'Centimeter': 91.44,
        'Millimeter': 914.4,
        'Inch': 36,
        'Yard': 1
    }
}

def convert_value(value, start_measure, target_measure):
    start_measure_type = measure_dict[start_measure]
    target_measure_type = measure_dict[target_measure]
    
    conversion_factor = conversion_factors[start_measure_type][target_measure_type]
    return value * conversion_factor

def main():
    print("Available Units of Measurement:")
    for key, value in measure_dict.items():
        print(f"{key}: {value}")

    try:
        start_measure = int(input("Enter Starting Unit of Measurement: "))
        target_measure = int(input("Enter Target Unit of Measurement: "))
        
        if start_measure not in measure_dict or target_measure not in measure_dict:
            print("Invalid unit of measurement.")
            return
        
        value = float(input(f"Enter Starting Measurement in {measure_dict[start_measure]}: "))

        result = convert_value(value, start_measure, target_measure)

        print(f"Result: {value} {measure_dict[start_measure]} = {result} {measure_dict[target_measure]}")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()
