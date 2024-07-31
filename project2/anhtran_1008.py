#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def add_f(x, y):
    return x + y

def sub_f(x, y):
    return x - y

def mul_f(x, y):
    return x * y

def div_f(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def mo_f(x, y):
    return x % y

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {e}"

current_result = None

while True:
    print("------CALCULATOR------")
    print("A: Addition")
    print("S: Subtraction")
    print("M: Multiplication")
    print("D: Division")
    print("MO: Modulo")
    print("Enter 'exit' or 'quit' to stop the calculator.")
    
    if current_result is None:
        func = input("Please choose the function you want (or enter expression): ").upper()
    else:
        func = input(f"Current result: {current_result}. Enter next function or expression: ").upper()
    
    if func in ['EXIT', 'QUIT']:
        break

    if func in ['A', 'S', 'M', 'D', 'MO']:
        if current_result is None:
            first_number = float(input('Enter first number: '))
        else:
            first_number = current_result

        second_number = float(input('Enter second number: '))

        if func == 'A':
            current_result = add_f(first_number, second_number)
            print(f'{first_number} + {second_number} = {current_result}')
        elif func == 'S':
            current_result = sub_f(first_number, second_number)
            print(f'{first_number} - {second_number} = {current_result}')
        elif func == 'M':
            current_result = mul_f(first_number, second_number)
            print(f'{first_number} x {second_number} = {current_result}')
        elif func == 'D':
            if second_number == 0:
                print('Error: Division by zero')
                continue
            current_result = div_f(first_number, second_number)
            print(f'{first_number} / {second_number} = {current_result}')
        elif func == 'MO':
            current_result = mo_f(first_number, second_number)
            print(f'{first_number} % {second_number} = {current_result}')
    else:
        # If func is not a predefined function, assume it's a mathematical expression
        expression = func
        if current_result is not None:
            expression = f"{current_result}{expression}"
        current_result = evaluate_expression(expression)
        print(f'Result: {current_result}')

