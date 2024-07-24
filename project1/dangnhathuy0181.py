Length = {'Meter': 1, 'Kilometer':0.001, 'Centimeter':100, 'Mile':0.0006213689, 'Yard':1.0936132983, 'Foot':3.280839895}
decision = 'Yes'

def convertion(str1, str2, number):
    if str1 and str2 in Length.keys():
        number2 = number / Length[str1] * Length[str2]
        if number2 >= 10000000000:
            number2 = int(number2)
        print(f"Result: {number} {str1} = {round(number2, 10)} {str2}")
    else:
        print("Your input is not founded, try again")

while decision == 'Yes':
    ini_unit = input(f"Enter starting unit of measurement {list(Length.keys())}: ")
    conv_unit = input(f"Enter Unit of measurement to Conver to: {list(Length.keys())}: ")
    num = int(input(f"Enter starting measurement in {ini_unit}: "))
    convertion(ini_unit, conv_unit, num)
    decision = input('Do you want to perform another convertion (Yes/No): ')
else:
    print('Thankiu for your efforts')


#Keep up the good work!