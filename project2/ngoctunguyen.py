# -*- coding: utf-8 -*-
"""Calculator - Ngoc Tu Nguyen Phan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bnr6Ux4eumHQfnlHg30wQbWyKp9IzVRN
"""

def calculate(expression):
    return eval(expression)

def main():
    print("Welcome to the Advanced Calculator!")
    print("You can perform operations with +, -, *, /, % and use parentheses for grouping.")
    print("Type 'exit' to end the calculator.")

    while True:
        expression = input("Enter your calculation: ")
        if expression.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        result = calculate(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()