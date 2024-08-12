# Calculator 1: Enter a single number
result = 0
number_1 = float(input('Enter the first number: '))
print(
    '''
        What your choice:
            A: Addition,
            S: Subtraction,
            M: Multiplication,
            D: Division
            MO: Modulo
            Q: exit the program
    '''
    )
while True:
    choose = input('What your choose is (A|S|M|D|MO) or exit (Q): ')
    if choose.upper() == 'A':
        number_2 = float(input('Enter the second|other numbers: '))
        result = number_1 + number_2
        number_1 = result
        print('Addition Result: ', result)
        continue
    elif choose.upper() == 'S':
        number_2 = float(input('Enter the second|other numbers: '))
        result = number_1 - number_2
        number_1 = result
        print('Subtraction Result: ', result)
        continue
    elif choose.upper() == 'M':
        number_2 = float(input('Enter the second|other numbers: '))
        result = number_1 * number_2
        number_1 = result
        print('Multiplication Result: ', result)
        continue
    elif choose.upper() == 'D':
        number_2 = float(input('Enter the second|other numbers: '))
        while number_2 == 0:
            nhap_lai = float(input('Nhap so khac 0: '))
            number_2 = nhap_lai
        result = number_1 / number_2
        number_1 = result
        print('Division Result: ', result)
        continue
    elif choose.upper() == 'MO':
        number_2 = float(input('Enter the second|other numbers: '))
        while number_2 == 0:
            nhap_lai = float(input('Nhap so khac 0: '))
            number_2 = nhap_lai
        result = number_1 % number_2
        number_1 = result
        print('Modulo Result: ', result)
        continue
    else:
        if choose.upper() == 'Q':
            break
print(f'Your final result is: {round(result,2)}')



# -------------------------------

# Calculator 2: Enter an expression or a single number and single operator
expression = ''
while True:
    ex = input('Enter the expression or number or operator: ')
    # if ex == '=':
    #     break
    expression += ex
    print(expression)
    end = input('Do you want to finish? Press =. If continue, press A: ')
    if end == '=':
        break
    else:
        enter = input('Enter operator: ')
        expression +=enter
        continue
calculate = eval(expression)
print(calculate)

#Good work!
#Since you have already used the eval() function, I recommend finding ways to shorten the code!