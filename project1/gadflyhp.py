# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
t_from = ''
t_to = ''
socandoi = 0
sodadoi = 0
countf = 1
countt = 1
t=''

mang_from = ['meter','yard','mile','foot','inch']
mang_to = ['meter','yard','mile','foot','inch']
while t_from not in mang_from and countf < 4:
    t_from = input('Enter staring unit of measurement (meter, yard, mile, foot, inch): ')
    countf += 1

if countf < 4: 
    while t_to not in mang_to and countt < 4:
        t_to = input('Enter unit of measurement to convert to (meter, yard, mile, foot, inch): ')
        countt += 1
    if countt < 4: 
        print('Enter starting measurement in '+t_from+': ', end='')
        socandoi = input()
        try:
            socandoi = float(socandoi)
        except:
            print('WRONG input\nReEnter starting measurement in '+t_from+': ', end='')
            socandoi = input()
            try:
                socandoi = float(socandoi)
            except:
                t_from ='Error'
                t_to = 'Error'
        if t_from == 'meter':
            if t_to == 'meter':
                sodadoi = socandoi
            elif t_to == 'yard':
                sodadoi = socandoi * 1.09 
            elif t_to == 'mile':
                sodadoi = socandoi * 0.0006213689 
            elif t_to == 'foot':
                sodadoi = socandoi * 3.280839895
            else:
                sodadoi = socandoi * 39.37007874
        elif t_from == 'yard':
            if t_to == 'meter':
                sodadoi = socandoi * 0.9144
            elif t_to == 'yard':
                sodadoi = socandoi  
            elif t_to == 'mile':
                sodadoi = socandoi * 0.0005681797 
            elif t_to == 'foot':
                sodadoi = socandoi * 3
            else:
                sodadoi = socandoi * 36       
        elif t_from == 'mile':
            if t_to == 'meter':
                sodadoi = socandoi * 1609.35
            elif t_to == 'yard':
                sodadoi = socandoi * 1760.0065617 
            elif t_to == 'mile':
                sodadoi = socandoi 
            elif t_to == 'foot':
                sodadoi = socandoi * 5280.019685
            else:
                sodadoi = socandoi * 63360.23622         
        elif t_from == 'foot':
            if t_to == 'meter':
                sodadoi = socandoi * 0.3048
            elif t_to == 'yard':
                sodadoi = socandoi * 0.3333333333 
            elif t_to == 'mile':
                sodadoi = socandoi * 0.0001893932 
            elif t_to == 'foot':
                sodadoi = socandoi
            else:
                sodadoi = socandoi * 12  
        else:
            if t_to == 'meter':
                sodadoi = socandoi * 0.0254
            elif t_to == 'yard':
                sodadoi = socandoi * 0.0277777778 
            elif t_to == 'mile':
                sodadoi = socandoi * 0.0000157828 
            elif t_to == 'foot':
                sodadoi = socandoi * 0.0833333333
            else:
                sodadoi = socandoi
        
        if t_from != 'Error':
            print("\nResult: ",socandoi,t_from,'=',sodadoi,t_to)
            print("Done Game!")
        else: print("\nWRONG input: starting measurement\nGame Over!")
    else: print("\nWRONG input: unit of measurement to convert to\nGame Over!")
else: print("\nWRONG input: staring unit of measurement\nGame Over!")


#Good job! But consider changing your own input error detection with Python try - except statements.