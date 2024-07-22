def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meters = {
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34
    }
    
    # Convert to meters first, then to the target unit
    meters = value * to_meters[from_unit]
    return meters / to_meters[to_unit]

def main():
    units = ['inches', 'feet', 'yards', 'meters', 'kilometers', 'miles']
    
    print("Enter Starting Unit of Measurement(inches, feet, yards, meters, kilometers, miles): ", end='')
    from_unit = input().lower()
    
    print("Enter Unit of Measurement to Convert to(inches, feet, yards, meters, kilometers, miles): ", end='')
    to_unit = input().lower()
    
    if from_unit not in units or to_unit not in units:
        print("Invalid unit. Please choose from the given options.")
        return
    
    print(f"Enter Starting Measurement in {from_unit.capitalize()}: ", end='')
    value = float(input())
    
    result = convert_length(value, from_unit, to_unit)
    
    print(f"Result: {value} {from_unit.capitalize()} = {result:.2f} {to_unit.capitalize()}")

if __name__ == "__main__":
    main()

# Noice

