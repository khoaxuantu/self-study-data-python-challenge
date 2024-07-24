def convert_length():
    u1 = input("Type in unit to be converted. (Unit must be one of: Nanometer, Micrometer, Millimeter, Centimeter, Meter, Kilometer): ").strip().lower()
    u2 = input("Choose the target unit. (Unit must be one of: Nanometer, Micrometer, Millimeter, Centimeter, Meter, Kilometer): ").strip().lower()
    x = float(input("Enter the value to convert: "))
    
    # Conversion factors
    units = {
        'nanometer': 1e9,
        'micrometer': 1e6,
        'millimeter': 1e3,
        'centimeter': 1e2,
        'meter': 1,
        'kilometer': 1e-3
    }
    
    if u1 in units and u2 in units:
        # Convert x from u1 to meters
        x_meters = x * units[u1]
        
        # Convert x from meters to u2
        result = x_meters / units[u2]
        
        print(f"{x} {u1} is equal to {result} {u2}")
    else:
        print("Invalid unit input. Please choose from the specified units.")
    
    again = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if again == 'yes':
        convert_length()
    else:
        print("Conversion session ended.")

# Start the conversion process
convert_length()


#Everything was perfect except the converting part. x_meters = x / units[u1] and result = x_meters * units[u2] 
#So sorry!