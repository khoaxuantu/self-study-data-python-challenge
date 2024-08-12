import math

def calculate(expression):
    try:
        allowed_globals = {"__builtins__": None, "math": math}
        allowed_locals = {}
        result = eval(expression, allowed_globals, allowed_locals)
        return result
    except Exception as e:
        return f"Error: {e}"
    
# main function
print("""
      You can perform the following operations:
      + for Addition
      - for Subtraction
      * for Multiplication
      / for Division
      % for Modulo
      Use parenthese for grouping operations, e.g., (A + B) * C.
      Type 'exit' to quit the calculator.
    """)

continuous_result = None # Variable to store the result of continuous calculations
while True:
    if continuous_result is not None:
        # Ask the user if they want to continue calculating with the previous result or start a new calculation
        choice = input("Do you want to countinue with the previous result? (yes/no): ")
        if choice == 'yes':
            expression = input(f"{continuous_result} ")
            if expression.lower() == 'exit':
                break
            expression = str(continuous_result) + expression
        elif choice == 'no':
            continuous_result = None # Reset if starting a new calculation
            expression = input("Enter your calculation: ")
            if expression.lower() == 'exit':
                break
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue

    else:
        # Get the calculation expression from the user
        expression = input("Enter your calculation: ")
        if expression.lower() == 'exit':
            break

    # Calculate the expression
    result = calculate(expression)

    if "Error" not in str(result):
        continuous_result = result # Save the result for the next calculation 
    else:
        continuous_result = None # Reset if there was an error

    # Display the result
    print(f"Result: {expression} = {result}")
#Keep up the good works!!!