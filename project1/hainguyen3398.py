print("***************Length Unit Converter***************\n")
length_unit=["m", "km", "cm", "mm", "mile", "yard"]
while True:
    while True:
        start = input("Enter starting unit of measurement (m, km, cm, mm, mile, yard):")
        if start in length_unit:
            break
        else:
            print("!!! Invalid unit. Please enter one of the following: m, km, cm, mm, mile, yard. !!!")
    while True:
        result = input("Enter unit of measurement to Convert to (m, km, cm, mm, mile, yard):")
        if result in length_unit:
            break
        else:
            print("!!! Invalid unit. Please enter one of the following: m, km, cm, mm, mile, yard. !!!")       
    while True:
        try:
            value = float(input(f"Enter starting measurement in {start}: "))
            if value < 0:
                print("!!! Please enter a positive value. !!!")
            else:
                break
        except ValueError:
            print("!!! Invalid input. Please enter a numerical value. !!!")
    # Don't be if...else slave dude -_-
    if start == 'm' :
        if result == 'm':
            print("Result: ",value,"m =",1*value,"m")
        elif result == 'km':
            print("Result: ",value,"m =",0.001*value,"km")
        elif result == 'cm':
            print("Result: ",value,"m =",100*value,"cm")
        elif result == 'mm':
            print("Result: ",value,"m =",1000*value,"mm")
        elif result == 'mile':
            print("Result: ",value,"m =",0.0006213689*value,"mile")
        else:
            print("Result: ",value,"m =",1.0936132983*value,"yard")
    elif start == 'km' :
        if result == 'm':
            print("Result: ",value,"km =",1000*value,"m")
        elif result == 'km':
            print("Result: ",value,"km =",1*value,"km")
        elif result == 'cm':
            print("Result: ",value,"km =",100000*value,"cm")
        elif result == 'mm':
            print("Result: ",value,"km =",1000000*value,"mm")
        elif result == 'mile':
            print("Result: ",value,"km =",0.6213688756*value,"mile")
        else:
            print("Result: ",value,"km =",1093.6132983*value,"yard")
    elif start == 'cm' :
        if result == 'm':
            print("Result: ",value,"cm =",0.01*value,"m")
        elif result == 'km':
            print("Result: ",value,"cm =",0.00001*value,"km")
        elif result == 'cm':
            print("Result: ",value,"cm =",1*value,"cm")
        elif result == 'mm':
            print("Result: ",value,"cm =",10*value,"mm")
        elif result == 'mile':
            print("Result: ",value,"cm =",0.0000062137*value,"mile")
        else:
            print("Result: ",value,"cm =",0.010936133*value,"yard")
    elif start == 'mm' :
        if result == 'm':
            print("Result: ",value,"mm =",0.001*value,"m")
        elif result == 'km':
            print("Result: ",value,"mm =",0.000001*value,"km")
        elif result == 'cm':
            print("Result: ",value,"mm =",0.1*value,"cm")
        elif result == 'mm':
            print("Result: ",value,"mm =",1*value,"mm")
        elif result == 'mile':
            print("Result: ",value,"mm =",6.213688756E-7*value,"mile")
        else:
            print("Result: ",value,"mm =",0.0010936133*value,"yard")
    elif start == 'mile' :
        if result == 'm':
            print("Result: ",value,"mile =",1609.35*value,"m")
        elif result == 'km':
            print("Result: ",value,"mile =",1.60935*value,"km")
        elif result == 'cm':
            print("Result: ",value,"mile =",160935*value,"cm")
        elif result == 'mm':
            print("Result: ",value,"mile =",1609350*value,"mm")
        elif result == 'mile':
            print("Result: ",value,"mile =",1*value,"mile")
        else:
            print("Result: ",value,"mole =",1760.0065617*value,"yard")
    else:
        if result == 'm':
            print("Result: ",value,"yard =",0.9144*value,"m")
        elif result == 'km':
            print("Result: ",value,"yard =",0.0009144*value,"km")
        elif result == 'cm':
            print("Result: ",value,"yard =",91.44*value,"cm")
        elif result == 'mm':
            print("Result: ",value,"yard =", 914.4*value,"mm")
        elif result == 'mile':
            print("Result: ",value,"yard =",0.0005681797*value,"mile")
        else:
            print("Result: ",value,"yard =",1*value,"yard")
    again=input("Do you want to continue? (y/n):")
    if again =='n':
        print("\nExiting the conversion program!\n")
        print("***************************************************")
        break
    else: print("\n")
 
