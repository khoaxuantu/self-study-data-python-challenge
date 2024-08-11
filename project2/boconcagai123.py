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

#Gud job on finishing this project! '
#However, just to let you know, Python is famous for many convinient built-in functions: e.g: eval() and also other ways to think out of the box to finish this project.
#I hope you can look through other projects to improve yours. Feel free to ask us!