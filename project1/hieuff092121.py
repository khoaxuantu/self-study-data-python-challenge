chuyen={'Nanometer':1000000000000,'Micrometer':1000000000,'Millimeter':1000000,'Centimeter':100000,'Meter':1000,'Kilometer':1}
loai1=input("Enter Starting Unit of Measurement(Nanometer,Micrometer,Milimete,Centimeter,Meter,Kilometer): ")
loai2=input("Enter Unit of Measurement to Convert to(Nanometer,Micrometer,Milimete,Centimeter,Meter,Kilometer): ")
gtr=float(input('Enter Starting Measurement in ' + loai1 + ': '))
kq=(gtr*chuyen[loai2])/chuyen[loai1]
print('Result:',gtr,loai1,'=',kq,loai2)

#Gudd job! But be careful with your typing. It's Millimeter, not Milimete :)) Keep up the good works!