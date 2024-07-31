#!/usr/bin/env python
# coding: utf-8

# # Create a Calculator
# ## 1. Create an input-output for the four basic operations: addition, subtraction, multiplication, and division

# In[1]:


# Create de function of Addition, Substraction, Multiplication and Division
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Dictionary to map user input to functions
operations = {
    'A': ('+', add),
    'S': ('-', subtract),
    'M': ('*', multiply),
    'D': ('/', divide)
}

print("Enter 'A' for Addition.")
print("Enter 'S' for Subtraction.")
print("Enter 'M' for Multiplication.")
print("Enter 'D' for Division.")

choice = input("Enter Choice (A,S,M,D): ").upper()

if choice in operations:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operator, operation = operations[choice]
    result = operation(num1, num2)
    
    print(f"Result: {num1} {operator} {num2} = {result}")
else:
    print("Invalid input")


# ## 2. Add the modulo (%) operation

# In[2]:


# Create de function of Addition, Substraction, Multiplication, Division and Modulo
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

# Dictionary to map user input to functions
operations = {
    'A': ('+', add),
    'S': ('-', subtract),
    'M': ('*', multiply),
    'D': ('/', divide),
    '%': ('%', modulo)
}

print("Enter 'A' for Addition.")
print("Enter 'S' for Subtraction.")
print("Enter 'M' for Multiplication.")
print("Enter 'D' for Division.")
print("Enter '%' for Modulo.")

choice = input("Enter Choice (A,S,M,D,%): ").upper()

if choice in operations:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operator, operation = operations[choice]
    result = operation(num1, num2)
    
    print(f"Result: {num1} {operator} {num2} = {result}")
else:
    print("Invalid input")

