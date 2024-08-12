# -*- coding: utf-8 -*-
"""Calculation.BepKute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ve_XzivgTbn_815v2qYBSDvf-9xfwzep
"""

def calculator():
    print("1. Addition: +")
    print("2. Subtraction: -")
    print("3. Multiplication: *")
    print("4. Division: /")
    print("5. Modulo: %")
    print("6. Group: ( )")
    print("7. Enter 'E' to Exit.")

    result = None

    while True:
        if result is None:
            expression = input("Enter calculation (or 'E' to exit): ").strip()
        else:
            expression = input(f"Continue calculation with {result}. Enter next calculation (or 'E' to exit): ").strip()

        if expression.upper() == 'E':
            break

        if result is not None:
            expression = f"{result} {expression}"

        try:
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except SyntaxError:
            print("Error: Invalid syntax.")
        except Exception as e:
            print(f"Error in calculation: {e}")

    print("Calculator session ended.")

calculator()

#Good work! You nailed it!
#Only a little comment: Consider writing a calculation system (which use the ANS keyword to refer to the lastest result) for more user choices!



