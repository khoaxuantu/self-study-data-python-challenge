print()
conversion_1 = input('Enter starting unit of measurement(m/km/cm/mm/mile/yard): ' )
conversion_2 = input('Enter unit of measurement to convert to (m/km/cm/mm/mile/yard): ' )
from_value = float(input('Enter value: ' ))
print()

if conversion_1 == 'm' and conversion_2 == 'km':
    to_value = from_value * 0.001
if conversion_1 == 'm' and conversion_2 == 'cm':
    to_value = from_value * 100
if conversion_1 == 'm' and conversion_2 == 'mm':
    to_value = from_value * 1000
if conversion_1 == 'm' and conversion_2 == 'mile':
    to_value = from_value * 0.0006213689
if conversion_1 == 'm' and conversion_2 == 'yard':
    to_value = from_value * 1.0936132983
    
if conversion_1 == 'km' and conversion_2 == 'm':
    to_value = from_value * 1000
if conversion_1 == 'km' and conversion_2 == 'cm':
    to_value = from_value * 100000
if conversion_1 == 'km' and conversion_2 == 'mm':
    to_value = from_value * 1000000
if conversion_1 == 'km' and conversion_2 == 'mile':
    to_value = from_value * 0.6213688756
if conversion_1 == 'km' and conversion_2 == 'yard':
    to_value = from_value * 1093.6132983
    
if conversion_1 == 'cm' and conversion_2 == 'm':
    to_value = from_value * 0.01
if conversion_1 == 'cm' and conversion_2 == 'km':
    to_value = from_value * 0.00001
if conversion_1 == 'cm' and conversion_2 == 'mm':
    to_value = from_value * 10
if conversion_1 == 'cm' and conversion_2 == 'mile':
    to_value = from_value * 0.0000062137
if conversion_1 == 'cm' and conversion_2 == 'yard':
    to_value = from_value * 0.010936133
    
if conversion_1 == 'mm' and conversion_2 == 'cm':
    to_value = from_value * 0.1
if conversion_1 == 'mm' and conversion_2 == 'm':
    to_value = from_value * 0.0001
if conversion_1 == 'mm' and conversion_2 == 'km':
    to_value = from_value * 0.0000001
if conversion_1 == 'mm' and conversion_2 == 'mile':
    to_value = from_value * 6.213688756E-7
if conversion_1 == 'mm' and conversion_2 == 'yard':
    to_value = from_value * 0.0010936133

if conversion_1 == 'mile' and conversion_2 == 'cm':
    to_value = from_value * 160935
if conversion_1 == 'mile' and conversion_2 == 'm':
    to_value = from_value * 1609.35
if conversion_1 == 'mile' and conversion_2 == 'km':
    to_value = from_value * 1.60935
if conversion_1 == 'mile' and conversion_2 == 'mm':
    to_value = from_value * 1609350
if conversion_1 == 'mile' and conversion_2 == 'yard':
    to_value = from_value * 1760.0065617

if conversion_1 == 'yard' and conversion_2 == 'cm':
    to_value = from_value * 91.44
if conversion_1 == 'yard' and conversion_2 == 'm':
    to_value = from_value * 0.9144
if conversion_1 == 'yard' and conversion_2 == 'km':
    to_value = from_value * 0.0009144
if conversion_1 == 'yard' and conversion_2 == 'mm':
    to_value = from_value * 914.4
if conversion_1 == 'yard' and conversion_2 == 'mile':
    to_value = from_value * 0.0005681797
    
print('Result: ', from_value, conversion_1, '=' ,to_value, conversion_2)

#Guddd job!