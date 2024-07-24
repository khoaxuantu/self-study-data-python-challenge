unit_measure=input("Enter Units of Measurement (Length, Temperature, Area): ")
if unit_measure == "Length":
    unit_in=input(f"Enter Input Unit of {unit_measure} (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer, Mile, Yard, Foot, Inch, Light year): ")
    value=float(input("Enter Input Value: "))
    unit_out=input(f"Enter Output Unit of {unit_measure} (Meter, Kilometer, Centimeter, Millimeter, Micrometer, Nanometer, Mile, Yard, Foot, Inch, Light year): ")
    if unit_in == "Kilometer" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*10**3} {unit_out}")
    elif unit_in == "Meter" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-3)} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*10**5} {unit_out}")
    elif unit_in == "Centimeter" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-5)} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*10**6} {unit_out}")
    elif unit_in == "Millimeter" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-6)} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*10**9} {unit_out}")
    elif unit_in == "Micrometer" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-9)} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*10**12} {unit_out}")
    elif unit_in == "Nanometer" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-12)} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*0.6213688756} {unit_out}")
    elif unit_in == "Mile" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*1.60935} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*1093.6132983} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*0.0009144} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*3280.839895} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*0.0003048} {unit_out}")

    elif unit_in == "Kilometer" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*39370.07874} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*0.0000254} {unit_out}")
    
    elif unit_in == "Kilometer" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.057008707*10^(-13)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Kilometer":
        print(f"Result: {value} {unit_in} = {value*9460660000000} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*100} {unit_out}")
    elif unit_in == "Centimeter" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*0.01} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*1000} {unit_out}")
    elif unit_in == "Millimeter" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*0.001} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*1000000} {unit_out}")
    elif unit_in == "Micrometer" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*0.000001} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*10**9} {unit_out}")
    elif unit_in == "Nanometer" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*10**(-9)} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*0.0006213689} {unit_out}")
    elif unit_in == "Mile" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*1609.35} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*1.0936132983} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*0.9144} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*3.280839895} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*0.3048} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*39.37007874} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*0.0254} {unit_out}")

    elif unit_in == "Meter" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.057008707*10(-16)} {unit_out}") #Cause Syntax Error
    elif unit_in == "Light year" and unit_out == "Meter":
        print(f"Result: {value} {unit_in} = {value*9460660000000000} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*10} {unit_out}")
    elif unit_in == "Millimeter" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*0.1} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*10000} {unit_out}")
    elif unit_in == "Micrometer" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*0.0001} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*10**7} {unit_out}")
    elif unit_in == "Nanometer" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*10**(-7)} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*0.0000062137} {unit_out}")
    elif unit_in == "Mile" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*160935} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*0.010936133} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*91.44} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*0.032808399} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*30.48} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*0.3937007874} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*2.54} {unit_out}")

    elif unit_in == "Centimeter" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.057008707*10**(-18)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Centimeter":
        print(f"Result: {value} {unit_in} = {value*946066000000000000} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*1000} {unit_out}")
    elif unit_in == "Micrometer" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*0.001} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*1000000} {unit_out}")
    elif unit_in == "Nanometer" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*0.000001} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*6.213688756*10**(-7)} {unit_out}")
    elif unit_in == "Mile" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*1609350} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*0.0010936133} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*914.4} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*0.0032808399} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*304.8} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*0.0393700787} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*25.4} {unit_out}")

    elif unit_in == "Millimeter" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.057008707*10**(-19)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Millimeter":
        print(f"Result: {value} {unit_in} = {value*946066*10**13} {unit_out}")

    elif unit_in == "Micrometer" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*1000} {unit_out}")
    elif unit_in == "Nanometer" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*0.001} {unit_out}")

    elif unit_in == "Micrometer" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*6.213688756*10**(-10)} {unit_out}")
    elif unit_in == "Mile" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*1609350000} {unit_out}")

    elif unit_in == "Micrometer" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*0.0000010936} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*914400} {unit_out}")

    elif unit_in == "Micrometer" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*0.0000032808} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*304800} {unit_out}")

    elif unit_in == "Micrometer" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*0.0000393701} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*25400} {unit_out}")

    elif unit_in == "Micrometer" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.057008707*10**(-22)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Micrometer":
        print(f"Result: {value} {unit_in} = {value*9.46066*10**21} {unit_out}")

    elif unit_in == "Nanometer" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*6.213688756*10**(-13)} {unit_out}")
    elif unit_in == "Mile" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*160935*10**7} {unit_out}")

    elif unit_in == "Nanometer" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*1.093613298*10**(-9)} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*914400000} {unit_out}")

    elif unit_in == "Nanometer" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*3.280839895*10**(-9)} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*304800000} {unit_out}")

    elif unit_in == "Nanometer" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*3.937007874*10**(-8)} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*25400000} {unit_out}")

    elif unit_in == "Nanometer" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.057008707*10**(-25)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Nanometer":
        print(f"Result: {value} {unit_in} = {value*9.460659999*10**24} {unit_out}")

    elif unit_in == "Mile" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*1760.0065617} {unit_out}")
    elif unit_in == "Yard" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*0.0005681797} {unit_out}")

    elif unit_in == "Mile" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*5280.019685} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*0.0001893932} {unit_out}")

    elif unit_in == "Mile" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*63360.23622} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*0.0000157828} {unit_out}")

    elif unit_in == "Mile" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*1.701096963*10**(-13)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Mile":
        print(f"Result: {value} {unit_in} = {value*5878559666946} {unit_out}")

    elif unit_in == "Yard" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*3} {unit_out}")
    elif unit_in == "Foot" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*(1/3)} {unit_out}")

    elif unit_in == "Yard" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*36} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*(1/36)} {unit_out}")

    elif unit_in == "Yard" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*9.665287622*10**(-17)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Yard":
        print(f"Result: {value} {unit_in} = {value*10346303587051618} {unit_out}")

    elif unit_in == "Foot" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*12} {unit_out}")
    elif unit_in == "Inch" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*(1/12)} {unit_out}")

    elif unit_in == "Foot" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*3.22176254*10**(-17)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Foot":
        print(f"Result: {value} {unit_in} = {value*31038910761154856} {unit_out}")

    elif unit_in == "Inch" and unit_out == "Light year":
        print(f"Result: {value} {unit_in} = {value*2.684802117*10**(-18)} {unit_out}")
    elif unit_in == "Light year" and unit_out == "Inch":
        print(f"Result: {value} {unit_in} = {value*372466929133858300} {unit_out}")
    
    elif unit_in == unit_out:
        print(f"Result: {value} {unit_in} = {value} {unit_out}")
    else:
        print("Incorrect format, please retry!")

elif unit_measure == "Temperature":
    unit_in=input(f"Enter Input Unit of {unit_measure} (Celsius, Kelvin, Fahrenheit): ")
    value=float(input("Enter Input Value: "))
    unit_out=input(f"Enter Output Unit of {unit_measure} (Celsius, Kelvin, Fahrenheit): ")
    if unit_in == "Celsius" and unit_out == "Kelvin":
        print(f"Result: {value} {unit_in} = {value + 273.15} {unit_out}")
    elif unit_in == "Kelvin" and unit_out == "Celsius":
        print(f"Result: {value} {unit_in} = {value - 273.15} {unit_out}")

    elif unit_in == "Celsius" and unit_out == "Fahrenheit":
        print(f"Result: {value} {unit_in} = {(value * 9/5) + 32} {unit_out}")
    elif unit_in == "Fahrenheit" and unit_out == "Celsius":
        print(f"Result: {value} {unit_in} = {(value - 32) * 5/9} {unit_out}")

    elif unit_in == "Kelvin" and unit_out == "Fahrenheit":
        print(f"Result: {value} {unit_in} = {(value * 9/5) - 459.67} {unit_out}")
    elif unit_in == "Fahrenheit" and unit_out == "Kelvin":
        print(f"Result: {value} {unit_in} = {(value + 459.67) * 5/9} {unit_out}")
    
    elif unit_in == unit_out:
        print(f"Result: {value} {unit_in} = {value} {unit_out}")
    else:
        print("Incorrect format, please retry!")

elif unit_measure == "Area":
    unit_in=input(f"Enter Input Unit of {unit_measure} (Square Meter, Square Kilometer, Square Centimeter, Square Millimeter, Square Micrometer, Hectare, Square Mile, Square Yard, Square Foot, Square Inch, Acre): ")
    value=float(input("Enter Input Value: "))
    unit_out=input(f"Enter Output Unit of {unit_measure} (Square Meter, Square Kilometer, Square Centimeter, Square Millimeter, Square Micrometer, Hectare, Square Mile, Square Yard, Square Foot, Square Inch, Acre): ")
    
    if unit_in == "Square Kilometer" and unit_out == "Square Meter":
        print(f"Result: {value} {unit_in} = {value*10**6} {unit_out}")
    elif unit_in == "Square Meter" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-6)} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Centimeter":
        print(f"Result: {value} {unit_in} = {value*10**10} {unit_out}")
    elif unit_in == "Square Centimeter" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-10)} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Millimeter":
        print(f"Result: {value} {unit_in} = {value*10**12} {unit_out}")
    elif unit_in == "Square Millimeter" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-12)} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Micrometer":
        print(f"Result: {value} {unit_in} = {value*10**18} {unit_out}")
    elif unit_in == "Square Micrometer" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*10**(-18)} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Hectare":
        print(f"Result: {value} {unit_in} = {value*100} {unit_out}")
    elif unit_in == "Hectare" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*0.01} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Mile":
        print(f"Result: {value} {unit_in} = {value*0.3861018768} {unit_out}")
    elif unit_in == "Square Mile" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*2.58999} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Yard":
        print(f"Result: {value} {unit_in} = {value*1195990.0463} {unit_out}")
    elif unit_in == "Square Yard" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*8.3612736*10**(-7)} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Foot":
        print(f"Result: {value} {unit_in} = {value*10763910.417} {unit_out}")
    elif unit_in == "Square Foot" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*9.290304*10**(-8)} {unit_out}")

    elif unit_in == "Square Kilometer" and unit_out == "Square Inch":
        print(f"Result: {value} {unit_in} = {value*1550003100} {unit_out}")
    elif unit_in == "Square Inch" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*6.4516*10**(-10)} {unit_out}")
    
    elif unit_in == "Square Kilometer" and unit_out == "Acre":
        print(f"Result: {value} {unit_in} = {value*247.10538147} {unit_out}")
    elif unit_in == "Acre" and unit_out == "Square Kilometer":
        print(f"Result: {value} {unit_in} = {value*0.0040468564} {unit_out}")
    elif unit_in == unit_out:
        print(f"Result: {value} {unit_in} = {value} {unit_out}")
    else:
        print("Incorrect format, please retry!")

# Really appriciate the effort you put into this project. Nice work! 
# But you can shorten your code by using the conversion factors. For example:
'''
def convert_length(value, from_unit, to_unit):
    # Define conversion rates relative to meters
    units = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'micrometer': 1e6,
        'nanometer': 1e9
    }

    # Convert from input units to meters
    value_in_meters = value / units[from_unit]

    # Convert from meters to output units
    converted_value = value_in_meters * units[to_unit]

    return converted_value
'''
# Writing too long code may cause you to failed tracking your syntax. 
# For example: you have an syntax error at line 97: You didn't include the exponential operation (**).