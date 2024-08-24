def calculator():
    print("+ for Addition.")
    print("- for Subtraction.")
    print("* for Multiplication.")
    print("/ for Division.")
    print("% for Modulo.")

    last_result = None
    last_expression = ""

    while True:
        try:
            if last_result is None:
                expression = input("Enter expression: ")
                last_expression = expression
            else:
                operation = input("Enter next operation: ")
                if operation.startswith(('+', '-', '*', '/', '%')):
                    expression = f"{last_result}{operation}"
                else:
                    print("Error! Please start with an operator (+, -, *, /, %).")
                    continue

            result = eval(expression)
            print(f"Result: {expression} = {result}")
            last_result = result
            last_expression = expression

        except ZeroDivisionError:
            print("Error! Division by zero.")
        except Exception as e:
            print(f"Error! Invalid input: {e}")

        next_calculation = input("Do you want to continue? (y/n): ")
        if next_calculation.lower() != 'y':
            break

calculator()

#Good job!
#Consider writing a calculation system (which use the ANS keyword to refer to the lastest result) for more user choices!