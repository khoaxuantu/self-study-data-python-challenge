# -*- coding: utf-8 -*-
"""
Projec2 : Creat a Caculator


"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def modulo(a, b):
    return a % b



def calculator():
    print("Enter 'A' for Addition.")
    print("Enter 'S' for Subtraction.")
    print("Enter 'M' for Multiplication.")
    print("Enter 'D' for Division.")
    print("Enter 'MOD' for Modulo.")
    

    while True:
        choice = input("Enter Choice (A,S,M,D,MOD,): ").upper()

        if choice in ['A', 'S', 'M', 'D', 'MOD']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 'A':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == 'S':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 'M':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 'D':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == 'MOD':
                print(f"Result: {num1} % {num2} = {modulo(num1, num2)}")

        

        else:
            print("Invalid Input")

        continue_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != 'yes':
            break
   
if __name__ == "__main__":
    calculator()
#Good job!
#You can look through the Python built in eval() function as it is allowed!