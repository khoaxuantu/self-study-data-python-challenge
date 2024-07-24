units = {'Nanometer':1000000000000,'Micrometer':1000000000,'Milimeter':1000000,'Centimeter':100000,'Meter':1000,'Kilometer':1}
fr = input("Enter Starting Unit of Measurement (Nanometer,Micrometer,Milimeter,Centimeter,Meter,Kilometer): ")
to = input("Enter Unit of Measurement to Convert to (Nanometer,Micrometer,Milimeter,Centimeter,Meter,Kilometer): ")
value = float(input('Enter Starting Measurement in ' + fr + ': '))
result = (value*units[to])/units[fr]
print('Result:',value,fr,'=',result,to)

# Why does your code look similar to katoloc's code?

