def execute (calculation, last_result = None):
    if last_result != None:
        calculation = str (last_result) + ' ' + calculation
    
    try:
        result = eval (calculation)
        print ('Result: ', result)
        continuous = input ('''Do you want to continue?
        If Yes, input your continuous calculation (example: +4%5)
        If No, type Stop''')
        if continuous == 'Stop':  
            print ('End of the Calculator program!!!')
        else:
            execute (calculation=continuous, last_result = result)
    except:
        cal = input ('Oops! Invalid calculation. Enter your calculation again:')
        execute (calculation = cal, last_result = last_result)
        
    
print ('''Welcome to the Calculator program! Here are the operations you can use:
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
% for Modulo
''')
    
cal = input ('Please enter your calculation:')
execute (calculation = cal, last_result = None)

#Noiceee! You nailed it this time! Keep it up!!