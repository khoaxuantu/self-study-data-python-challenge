import re

def evaluate_expression(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {e}"

def get_input():
    expression = input("Enter a calculation: ")
    return expression

def main():
    print("Welcome to the Calculator!")
    print("You can perform Addition (+), Subtraction (-), Multiplication (*), Division (/), and Modulo (%)")
    print("You can use parentheses for grouping operations, e.g., (A+B)*C")
    print("You can input calculations with 3 or more number pairs, e.g., A + B + C")
    print("Type 'exit' to quit the calculator")

    result = None
    while True:
        if result is not None:
            expression = input(f"Result: {result}\nContinue with: {result} ")
            expression = str(result) + expression
        else:
            expression = get_input()

        if expression.lower() == 'exit':
            print("Goodbye ^^")
            break

        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
#Because u used built-in function, which is `eval()`, I evaluate your work more strict. Here you have not handled the case where I input something that is runnable via `eval` function, for example: sorted([3, 2, 1])