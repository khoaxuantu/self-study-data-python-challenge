Caculate={'Meter':1,'Kilometer':1000,'Centimeter':0.01,'Foot':0.3048,'Inch':0.0254,'Light year':9460660000000000}
y1=input("Enter Starting Unit of Measurement(Meter,Kilometer,Centimeter,Foot,Inch,Light year): ").capitalize()
y2=input('Enter Unit of Mesurement to Convert to(Meter,Kilometer,Centimeter,Foot,Inch,Light year): ').capitalize()
x=int(input(f'Enter Starting Measurement in {y1}: '))
if y2=='Meter':
    print(f'Result: {x} {y1} = {x*1*Caculate[y1]} Meter')
elif y2=='Kilometer':
    print(f'Result: {x} {y1} = {x*0.001*Caculate[y1]} Kilometer')
elif y2=='Centimeter':
    print(f'Result: {x} {y1} = {x*100*Caculate[y1]} Centimeter')
elif y2=='Foot':
    print(f'Result: {x} {y1} = {x*3.280839895*Caculate[y1]} Foot')
elif y2=='Inch':
    print(f'Result: {x} {y1} = {x*39.37007874*Caculate[y1]} Inch')
elif y2=='Light year':
    print(f'Result: {x} {y1} = {x*1.057008707E-16*Caculate[y1]} Light Year')

# Reviewer: Noice

