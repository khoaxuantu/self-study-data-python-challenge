def length_conversion (value, from_unit, to_unit):
    conversions = {'meters': 1, 'kilometers': 1000, 'miles': 1609.34}
    return value * conversions[from_unit] / conversions[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        return (value * 9/5 + 32) if to_unit == 'Fahrenheit' else (value + 273.15)
    if from_unit == 'Fahrenheit':
        return ((value - 32) * 5/9) if to_unit == 'Celsius' else ((value - 32) * 5/9 + 273.15)
    if from_unit == 'Kelvin':
        return (value - 273.15) if to_unit == 'Celsius' else ((value - 273.15) * 9/5 + 32)

def weight_conversion(value, from_unit, to_unit):
    conversions = {'kilograms': 1,'pounds': 0.453592,'grams': 0.001}
    return value * conversions[from_unit] / conversions[to_unit]

def time_conversion (value, from_unit, to_unit):
    conversions = {'seconds': 1, 'minutes': 60, 'hours': 3600}
    return value * conversions[from_unit] / conversions[to_unit]

# Overall, nice work! However, you can further improve your program by using the input() function to take the user's input and print the result out based on the units converted
# Keep up the good works for the next projects.