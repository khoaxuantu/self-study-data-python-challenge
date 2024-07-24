#chuyen tat ca cac don vi ve meter lay meter lam chuan
length = {
    'kilometer': 0.001,
    'centimeter': 100,
    'millimeter': 1000,
    'micrometer': 1000000,
    'nanometer': 1000000000,
    'mile': 0.0006213689,
    'yard': 1.0936132983,
    'foot': 3.280839895,
    'inch': 39.37007874,
    'meter':1
}
temperature={
    'kelvin':274.15,
    'fahrenheit':33.8,
    'celsius':1
}
area={
    'square kilometer': 0.000001,
    'square centimeter': 10000,
    'square millimeter': 1000000,
    'square micrometer': 1000000000000,
    'square hectare': 0.0001,
    'square mile': 3.861018768E-7,
    'square yard': 1.1959900463,
    'square foot': 10.763910417,
    'square inch': 1550.0031,
    'square meter':1
}
def Lengthconverted(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    else:
        new_value = (value / length[from_unit]) * length[to_unit]
        return new_value
def Temperatureconverted(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    else:
        if to_unit=='kelvin' and from_unit=='celsius':
            new_value = value + temperature[to_unit]
        elif to_unit=='fahrenheit' and from_unit=='celsius':
            new_value=(value*9.5)+32
        elif to_unit=='celsius' and from_unit=='kelvin':
            new_value = value - temperature[to_unit]
        elif to_unit=='celsius' and from_unit=='fahrenheit':
            new_value=(value-32)/9.5
        elif to_unit=='kelvin' and from_unit=='fahrenheit':
            new_value=(value-32)/1.8+273.15
        elif to_unit=='fahrenheit' and from_unit=='kelvin':
            new_value=(value-273.15)*1.8+32
        return new_value
def Areaconverted(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    else:
        new_value = (value / area[from_unit]) * area[to_unit]
        return new_value

from_unit=input("Enter Starting Unit of Measurement: ")
to_unit=input("Enter Starting Unit of Measurement to convert to: ")
value=float(input(f"Enter Starting Measurement in {from_unit}: "))
if(from_unit in length):
    print(f'Result: {value} {from_unit} = {Lengthconverted(value, from_unit, to_unit)} {to_unit}') 
elif (from_unit in temperature):
    print(f'Result: {value} {from_unit} = {Temperatureconverted(value, from_unit, to_unit)} {to_unit}') 
elif (from_unit in area):
    print(f'Result: {value} {from_unit} = {Areaconverted(value, from_unit, to_unit)} {to_unit}') 

#Great job!

