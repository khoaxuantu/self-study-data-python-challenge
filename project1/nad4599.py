#project
def meters_to_kilometers(meters):
    return meters / 1000

def meters_to_foot(meters):
    return meters * 3.280839895

def meters_to_centimeter(meters): 
    return meters * 100

def meters_to_lightyear(meters): 
    return meters * 1.057008707E-16

def meters_to_inch(meters): 
    return meters * 39.37007874

def meters_to_nanometer(meters): 
    return meters * 1000000000

#to call the function dynamically
conversion_dict = {
    'meters_to_kilometers': meters_to_kilometers,
    'meters_to_foot': meters_to_foot,
    'meters_to_centimeter': meters_to_centimeter,
    'meters_to_lightyear': meters_to_lightyear,
    'meters_to_inch': meters_to_inch,
    'meters_to_nanometer': meters_to_nanometer
}
values = [10, 10, 10, 10, 10,10]
units = ['kilometers', 'foot', 'centimeter','lightyear', 'inch', 'nanometer']

converted_values = [conversion_dict[f"meters_to_{unit}"](value) if unit!= 'meters' else value for unit, value in zip(units, values)]
print([f"{value} meters" for value in values])
print([f"equal to {value} ({unit})" for value, unit in zip(converted_values, units)])

"""
Noice

But you only perform one-direction conversions, which does not fulfill the requirements.
So you earn 1 bonus point for it

The requirements require you to make at least 3 convertible units
For example:
minute -> hour & hour -> minute,
second -> minute & minute -> second,
millisecond -> second & second -> millisecond
"""

