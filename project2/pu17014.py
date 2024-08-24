def Caculation(num1, num2, operation):
    if operation == 'A':
        return num1 + num2
    elif operation == 'S':
        return num1 - num2
    elif operation == 'M':
        return num1 * num2
    elif operation == 'D':
        return num1 / num2
    elif operation == 'Mo':
        return num1 % num2
        
print("Enter 'A' for Addition.\n")
print("Enter 'S' for Subtraction.\n")
print("Enter 'M' for Multiplication.\n")
print("Enter 'D' for Division.\n")
print("Enter 'Mo' for Modulo.\n")

operation_dict = {'A':'+', 'S':'-', 'M':'x', 'D':'/', 'Mo':'%'}

expression = ''
value = 0
cnt = 0
previous_choice = ''
while True:
    choice = input('Enter Choice (A,S,M,D,Mo): ')
    while choice not in operation_dict.keys():
        choice = input('Choice does not exist in the available list. \nPlease, enter again: ')
    if cnt == 0: 
        num1 = float(input('Enter first number: '))
        expression = str(num1)
    else:
        num1 = value
        if previous_choice in ['A', 'S'] and choice in ['M', 'D', 'Mo']:
            expression = '(' + expression + ')'       
    num2 = float(input('Enter second number: '))
    if choice in ['D', 'Mo'] and num2 == 0:
        print('Division by zero.')
        break
    value =  Caculation(num1, num2, choice)
    expression = '{0} {1} {2}'.format(expression, operation_dict[choice], num2)
    print('Result:', expression, '=', value)
    again = input('Continue? (y/n) ')
    if again == 'n':
        break
    cnt = 1
    previous_choice = choice

#Good job on finishing this project! However, just note that our 4th requirement requires a full expression, e.g: you can write: (5+2)*8 at the same time.
#Besides, the 5th requirement requires you to have an answer saved before calculating any further calculations
#Feel free to ask us any questions, keep it up!!