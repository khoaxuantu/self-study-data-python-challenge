
# Conversion factors
METER_TO_KILOMETER = 0.001
METER_TO_FEET = 3.28084
METER_TO_MILES = 0.000621371

KILOMETER_TO_METER = 1000
KILOMETER_TO_FEET = 3280.84
KILOMETER_TO_MILES = 0.621371

FEET_TO_METER = 0.3048
FEET_TO_KILOMETER = 0.0003048
FEET_TO_MILES = 0.000189394

MILES_TO_METER = 1609.34
MILES_TO_KILOMETER = 1.60934
MILES_TO_FEET = 5280

# Conversion functions
def meters_to_kilometers(meters):
    return meters * METER_TO_KILOMETER

def meters_to_feet(meters):
    return meters * METER_TO_FEET

def meters_to_miles(meters):
    return meters * METER_TO_MILES

def kilometers_to_meters(kilometers):
    return kilometers * KILOMETER_TO_METER

def kilometers_to_feet(kilometers):
    return kilometers * KILOMETER_TO_FEET

def kilometers_to_miles(kilometers):
    return kilometers * KILOMETER_TO_MILES

def feet_to_meters(feet):
    return feet * FEET_TO_METER

def feet_to_kilometers(feet):
    return feet * FEET_TO_KILOMETER

def feet_to_miles(feet):
    return feet * FEET_TO_MILES

def miles_to_meters(miles):
    return miles * MILES_TO_METER

def miles_to_kilometers(miles):
    return miles * MILES_TO_KILOMETER

def miles_to_feet(miles):
    return miles * MILES_TO_FEET

# User interface
def convert_units():
    print("Select the conversion type:")
    print("1. Length")
    conversion_type = int(input("Enter the number corresponding to your choice: "))
    
    if conversion_type == 1:
        print("Select the input unit:")
        print("1. Meters")
        print("2. Kilometers")
        print("3. Feet")
        print("4. Miles")
        input_unit = int(input("Enter the number corresponding to your choice: ")) # Needs out of bound input handler
        
        print("Select the output unit:")
        print("1. Meters")
        print("2. Kilometers")
        print("3. Feet")
        print("4. Miles")
        output_unit = int(input("Enter the number corresponding to your choice: ")) # Needs out of bound input handler
        
        value = float(input("Enter the value to convert: "))
        
        # I'm dead -.-
        if input_unit == 1:
            if output_unit == 1:
                result = value
            elif output_unit == 2:
                result = meters_to_kilometers(value)
            elif output_unit == 3:
                result = meters_to_feet(value)
            elif output_unit == 4:
                result = meters_to_miles(value)
        elif input_unit == 2:
            if output_unit == 1:
                result = kilometers_to_meters(value)
            elif output_unit == 2:
                result = value
            elif output_unit == 3:
                result = kilometers_to_feet(value)
            elif output_unit == 4:
                result = kilometers_to_miles(value)
        elif input_unit == 3:
            if output_unit == 1:
                result = feet_to_meters(value)
            elif output_unit == 2:
                result = feet_to_kilometers(value)
            elif output_unit == 3:
                result = value
            elif output_unit == 4:
                result = feet_to_miles(value)
        elif input_unit == 4:
            if output_unit == 1:
                result = miles_to_meters(value)
            elif output_unit == 2:
                result = miles_to_kilometers(value)
            elif output_unit == 3:
                result = miles_to_feet(value)
            elif output_unit == 4:
                result = value
        
        print(f"Converted value: {result}")

if __name__ == "__main__":
    convert_units()
