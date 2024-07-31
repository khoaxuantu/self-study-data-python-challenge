# Nice work! You did try to handle the errors may occur when using `eval()`, And because you used `eval()`, we also evaluate your work strictly.

# Here, you have not handled the case when user entries a function in python, because `eval()` can execute any python code. For example, if user enters `print('test')`, your program still executes it and returns the result of `None`. You should the errors may occur when using `eval()` detailedly.

import re


def cal(expression):
    try:
        # Evaluate the expression safely
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"


def caladd():
    previous_result = 0
    continuous_mode = False

    print("Welcome to the calculator!")
    print("You can perform calculations with +, -, *, /, % operators.")
    print("You can also use parentheses for grouping.")
    print("Type 'exit' to quit or 'clear' to reset the calculator.")

    while True:
        # Display the previous result if in continuous mode
        if continuous_mode:
            expression = input(
                f"Enter expression (previous result is {previous_result}): "
            )
        else:
            expression = input("Enter expression: ")

        if expression.lower() == "exit":
            print("Exiting calculator.")
            break
        elif expression.lower() == "clear":
            previous_result = 0
            continuous_mode = False
            print("Calculator reset.")
            continue

        # Check if continuous mode is enabled
        if continuous_mode:
            expression = f"{previous_result} {expression}"

        # Replace any multi-spaces with a single space for consistency
        expression = re.sub(r"\s+", " ", expression).strip()

        # Perform calculation
        result = cal(expression)

        if isinstance(result, str) and result.startswith("Error:"):
            print(result)
        else:
            print(f"Result: {result}")
            previous_result = result
            continuous_mode = True


if __name__ == "__main__":
    caladd()
