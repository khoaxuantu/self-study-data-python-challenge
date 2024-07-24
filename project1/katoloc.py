convert={'Nanometer':1000000000000,'Micrometer':1000000000,'Millimeter':1000000,'Centimeter':100000,'Meter':1000,'Kilometer':1}
fr=input("Enter Starting Unit of Measurement(Nanometer,Micrometer,Milimete,Centimeter,Meter,Kilometer): ")
to=input("Enter Unit of Measurement to Convert to(Nanometer,Micrometer,Milimete,Centimeter,Meter,Kilometer): ")
value=float(input('Enter Starting Measurement in ' + fr + ': '))
result=(value*convert[to])/convert[fr]
print('Result:',value,fr,'=',result,to)

# Reviewer: Why does you code look similar to phutoan.

