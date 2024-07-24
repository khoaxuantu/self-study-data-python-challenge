def meter_to_(to_unit, value):
    if to_unit == "meter":
      return value
    elif to_unit == "kilometer":
      return value * 0.001
    elif to_unit == "centimeter":
      return value * 100
    elif to_unit == "milimeter":
      return value * 1000
    elif to_unit == "micrometer":
      return value * 1000000
    elif to_unit == "nanometer":
      return value * 1000000000
def kilometer_to_(to_unit, value):
    if to_unit == "meter":
      return value * 1000
    elif to_unit == "kilometer":
      return value
    elif to_unit == "centimeter":
      return value * 100000
    elif to_unit == "milimeter":
      return value * 1000000
    elif to_unit == "micrometer":
      return value * 1000000000
    elif to_unit == "nanometer":
      return value * 1000000000000
def centimeter_to_(to_unit, value):
    if to_unit == "meter":
      return value * 0.01
    elif to_unit == "kilometer":
      return value * 0.00001
    elif to_unit == "centimeter":
      return value
    elif to_unit == "milimeter":
      return value * 10
    elif to_unit == "micrometer":
      return value * 10000
    elif to_unit == "nanometer":
      return value * 10000000
def milimeter_to_(to_unit, value):
    if to_unit == "meter":
      return value * 0.001
    elif to_unit == "kilometer":
      return value * 0.000001
    elif to_unit == "centimeter":
      return value * 0.1
    elif to_unit == "milimeter":
      return value
    elif to_unit == "micrometer":
      return value * 1000
    elif to_unit == "nanometer":
      return value * 1000000
def micrometer_to_(to_unit, value):
    if to_unit == "meter":
      return value * 0.000001
    elif to_unit == "kilometer":
      return value * 9.999999999E-10
    elif to_unit == "centimeter":
      return value * 0.0001
    elif to_unit == "milimeter":
      return value * 0.001
    elif to_unit == "micrometer":
      return value
    elif to_unit == "nanometer":
      return value * 1000  
def nanometer_to_(to_unit, value):
    if to_unit == "meter":
      return value * 1.E-9
    elif to_unit == "kilometer":
      return value * 1.E-12
    elif to_unit == "centimeter":
      return value * 1.E-7
    elif to_unit == "milimeter":
      return value * 0.000001
    elif to_unit == "micrometer":
      return value * 0.001
    elif to_unit == "nanometer":
      return value  


def convert_units(from_unit, to_unit, value):
    if from_unit == "meter":
        return meter_to_(to_unit, value)
    elif from_unit == "kilometer":
        return kilometer_to_(to_unit, value)
    elif from_unit == "centimeter":
        return centimeter_to_(to_unit, value)
    elif from_unit == "milimeters":
        return milimeter_to_(to_unit, value)
    elif from_unit == "micrometer":
        return micrometer_to_(to_unit, value)
    elif from_unit == "nanometer":
        return nanometer_to_(to_unit, value)

def main():
    print("Enter Starting Unit of Measurement (meter, kilometer, centimeter, milimeter, micrometer, nanometer):")
    from_unit = input().strip().lower()
    print("Enter Unit of Measurement to Convert to (meter, kilometer, centimeter, milimeter, micrometer, nanometer):")
    to_unit = input().strip().lower()
    print(f"Enter Starting Measurement in {from_unit.capitalize()}:")
    value = float(input())
    
    result = convert_units(from_unit, to_unit, value)
    
    if result is not None:
        print(f"Result: {value} {from_unit.capitalize()} = {result} {to_unit.capitalize()}")
    else:
        print("Invalid unit conversion.")

if __name__ == "__main__":
    main()


#Great job!