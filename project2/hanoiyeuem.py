# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/134eMWLn9uDnc6GpjJ2J4ynuoMb4dLGIA
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
        return "Division by zero error"

def modulo(a, b):
    return a % b

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def main():
    print("Enter 'A' for Addition.")
    print("Enter 'S' for Subtraction.")
    print("Enter 'M' for Multiplication.")
    print("Enter 'D' for Division.")
    print("Enter 'Mod' for Modulo.")
    print("Enter 'E' to enter a custom expression.")
    print("Enter 'Q' to Quit.")

    continuous_result = None

    while True:
        choice = input("Enter Choice (A,S,M,D,Mod,E,Q): ").strip().upper()

        if choice == 'Q':
            print("Exiting...")
            break

        if choice in ['A', 'S', 'M', 'D', 'MOD']:
            if continuous_result is None:
                try:
                    num1 = float(input("Enter first number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue
            else:
                num1 = continuous_result

            try:
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == 'A':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == 'S':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == 'M':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == 'D':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            elif choice == 'MOD':
                result = modulo(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")

            continuous_result = result

        elif choice == 'E':
            expression = input("Enter your expression: ")
            result = calculate_expression(expression)
            print(f"Result: {expression} = {result}")
            continuous_result = result

        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()
