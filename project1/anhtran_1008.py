while(True):
    print("------------------------------------------------------------------------------------------------------------------")
    print("---Unit of Measurement Converter---")
    print("1- Meter")
    print("2- Kilometer")
    print("3- Centimeter")
    print("4- Millimeter")
    print("5- Micrometer")
    print("6- Nanometer")
    print("*Which units do you want to convert?")
    
    start_to = int(input('- Enter unit of measurement:   '))
    end_to = int(input('- Enter unit of measurement to convert to   '))
    x = float(input('- Enter starting measurement   '))
    
    # Reviewer: Don't be if...else slave dude -.-
    if start_to == 1 and end_to == 1:
          print(x)
    elif start_to == 1 and end_to == 2:  
          print(x*0.001)
    elif start_to == 1 and end_to == 3:  
          print(x*100)
    elif start_to == 1 and end_to == 4:  
          print(x*1000)
    elif start_to == 1 and end_to == 5:  
          print(x*1000000)
    elif start_to == 1 and end_to == 6:  
          print(x*1000000000)
    elif start_to == 2 and end_to == 1:  
          print(x*1000)
    elif start_to == 2 and end_to == 2:  
          print(x)
    elif start_to == 2 and end_to == 3:  
          print(x*100000)
    elif start_to == 2 and end_to == 4:  
          print(x*1000000)
    elif start_to == 2 and end_to == 5:  
          print(x*1000000000)
    elif start_to == 2 and end_to == 6:  
          print(x*1000000000000)
    elif start_to == 3 and end_to == 1:  
          print(x*0.01)
    elif start_to == 3 and end_to == 2:  
          print(x*0.00001)
    elif start_to == 3 and end_to == 3:  
          print(x*1)
    elif start_to == 3 and end_to == 4:  
          print(x*10)
    elif start_to == 3 and end_to == 5:  
          print(x*10000)
    elif start_to == 3 and end_to == 6:  
          print(x*10000000)
    elif start_to == 4 and end_to == 1:  
          print(x*0.001)
    elif start_to == 4 and end_to == 2:  
          print(x*0.000001)
    elif start_to == 4 and end_to == 3:  
          print(x*0.1)
    elif start_to == 4 and end_to == 4:  
          print(x*1)
    elif start_to == 4 and end_to == 5:  
          print(x*1000)
    elif start_to == 4 and end_to == 6:  
          print(x*1000000)
    elif start_to == 5 and end_to == 1:  
          print(x*0.000001)
    elif start_to == 5 and end_to == 2:  
          print(x*1e-09)
    elif start_to == 5 and end_to == 3:  
          print(x*0.0001)
    elif start_to == 5 and end_to == 4:  
          print(x*0.001)
    elif start_to == 5 and end_to == 5:  
          print(x*1)
    elif start_to == 5 and end_to == 6:  
          print(x*1000)
    elif start_to == 6 and end_to == 1:  
          print(x*1e-9)
    elif start_to == 6 and end_to == 2:  
          print(x*1e-12)
    elif start_to == 6 and end_to == 3:  
          print(x*1e-7)
    elif start_to == 6 and end_to == 4:  
          print(x*0.000001)
    elif start_to == 6 and end_to == 5:  
          print(x*0.001)
    elif start_to == 6 and end_to == 6:  
          print(x*1)
    else:
        print('Erro - please try again!')

