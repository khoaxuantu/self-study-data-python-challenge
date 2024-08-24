
def calculator():
    exp = input('''
Enter a expression with +,-,*,/,%,(,)
Enter expression: ''')
    try:
        print(f'{exp} = {eval(exp)}')
    except:
        print('You are not typed a valid expression, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
ENTER HERE:  ''')

    if calc_again.upper() == 'Y':
        calculator()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculator()

#Noice!! Beware to validate your inputs so your program don't crash when user input different value than int or float 
#Keep up the good works!