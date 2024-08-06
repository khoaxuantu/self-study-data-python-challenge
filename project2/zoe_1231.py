#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero is not allowed."

def modulo(x, y):
    return x % y if y != 0 else "Error: Modulo by zero is not allowed."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")
            
print("Enter 'A' for Addition.")
print("Enter 'S' for Subtraction.")
print("Enter 'M' for Multiplication.")
print("Enter 'D' for Division.")
print("Enter 'MOD' for Modulo.")

operations = {
    'a': ('+', add),
    's': ('-', subtract),
    'm': ('*', multiply),
    'd': ('/', divide),
    'mod': ('%', modulo)
}

while True: 
    while True:
        operation = input("Enter Choice (A, S, M, D, MOD): ").lower()
        if operation in operations:
            break
        else: 
            print("Invalid input, please enter A, S, M, D, or MOD!")

    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")
    symbol, func = operations[operation]        
    result = func(first_number, second_number)
    print(f"Result: {first_number} {symbol} {second_number} = {result}")
    
    continue_calculate = input("Do you want to perform another calculation? (Yes/No): ").lower()
    if continue_calculate != 'yes':
        break

