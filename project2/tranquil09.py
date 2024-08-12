# 1. create an input-output for
    #   the 4 basic operations: addition, subtraction, multiplication, and division.

# Add the modulo (%) operation: the remainder of the division

# Allow inputting calculations with 3 or more number pairs, e.g., aa + bb + cc.

# Group operations together, e.g., (A+b) x c

# Include all the above bonus requirements and add continuous calculation functionality, e.g., A + B = AB, AB + C = ABC

def calculator():
    try:
        user_input = input("Enter your operation: ")
        result = eval(user_input)
        print(f"Result: {result:.2f}")
    except:
        print("Invalid input or syntax error. Please check your expression.")

# Example usage:
calculate_expression()

#You mistyped the function name when calling it.
#Be more careful next time!
