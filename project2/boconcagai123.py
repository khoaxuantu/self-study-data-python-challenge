print('+ - Add')
print('- - Subtract')
print('* - Multiply')
print('/ - Divide')
print('% - Modulo')
option = input('Choose an operation: ')

if option in ['+', '-', '*', '/', '%']:
    try:
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
    else:
        if option == '+':
            result = num_1 + num_2
        elif option == '-':
            result = num_1 - num_2
        elif option == '*':
            result = num_1 * num_2
        elif option == '/':
            if num_2 == 0:
                result = "Error: Division by zero"
            else:
                result = num_1 / num_2
        elif option == '%':
            result = num_1 % num_2    

    print('The result is {}.'.format(result))
else:
    print('Invalid operation')
