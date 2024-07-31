# -*- coding: utf-8 -*-
"""huynhkhanhlinh_project2 - Linh Huỳnh.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GEyBcOOEwrM2mYTSVOyxrsCcPVPa6lkN
"""

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b != 0:
        return a/b
    else:
        print("??? denominator can't be 0")
        return None

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        print("Error: Denominator can't be 0.")
        return None

basic_operations = {
    '+': addition,
    '-': subtraction,
    'x': multiplication,
    ':': division,
    '%': modulo}

print('Choose only these operators please:')
for key, function in basic_operations.items():
    print(f"{key}: {function.__name__}")
print("\n Enter 'break' whenever you want to stop")

while True:
    try:
        x = input('\n Enter the first number: ')
        if x == 'break':
            break
        x = float(x)

        operator = input('Enter the wanted operator: ')
        if operator == 'break':
            break

        y = input('Enter the second number: ')
        if y == 'break':
            break
        y = float(y)

        if operator in basic_operations:
            basic_operation_function = basic_operations[operator]
            result = basic_operation_function(x,y)
            print(f"{x} {operator} {y} = {result}")
        else:
            print("I said: Choose only available operators")
    except ValueError:
        print("wtf i said 'number'. can you read???")