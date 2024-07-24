# Step 1: Enter the starting unit of measurement (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer)
starting_unit = input("Enter the starting unit of measurement(Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ")

# Step 2: Enter the unit of measurement to convert to (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer)
target_unit = input("Enter the unit of measurement to convert to(Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer): ")

# Step 3: Enter starting number of measurement
starting_number = float(input(f"Enter starting number of measurement in {starting_unit}: "))

# Step 4: Perform the conversion
conversion_factors = {
    "Meter": {"Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Micrometer": 1000000, "Nanometer": 1000000000},
    "Kilometer": {"Meter": 1000, "Centimeter": 100000, "Millimeter": 1000000, "Micrometer": 1000000000, "Nanometer": 1000000000000},
    "Centimeter": {"Meter": 0.01, "Kilometer": 0.00001, "Millimeter": 10, "Micrometer": 10000, "Nanometer": 10000000},
    "Millimeter": {"Meter": 0.001, "Kilometer": 0.000001, "Centimeter": 10, "Micrometer": 1000, "Nanometer": 1000000},
    "Micrometer": {"Meter": 0.000001, "Kilometer": 0.000000001, "Centimeter": 0.001, "Millimeter": 100, "Nanometer": 1000},
    "Nanometer": {"Meter": 0.000000001, "Kilometer": 0.000000000001, "Centimeter": 0.0000001, "Millimeter": 0.000001, "Micrometer": 0.001}
}

# Check whether the measurement is in the conversion set
if starting_unit in conversion_factors and target_unit in conversion_factors[starting_unit]:
    # Calculate the value after conversion
    converted_value = starting_number * conversion_factors[starting_unit][target_unit]
# Step 5: Print out the results
    print(f"Result: {starting_number} {starting_unit} = {converted_value} {target_unit}")
else:
    print("Conversion between these units is not supported.")

#Great Job!