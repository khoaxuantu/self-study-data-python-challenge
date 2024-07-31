import re

def calculate(expression):
    # Replace '^' with '**' for exponentiation
    expression = expression.replace('^', '**')
    
    # Evaluate the expression safely
    try:
        result = eval(expression)
        return result
    except (SyntaxError, NameError, ZeroDivisionError):
        return "Error: Invalid expression"

def main():
    print("Welcome to the Advanced Calculator!")
    print("Enter 'q' to quit.")
    
    result = 0
    while True:
        user_input = input(f"Enter calculation (current result: {result}): ")
        
        if user_input.lower() == 'q':
            print("Thank you for using the Advanced Calculator!")
            break
        
        # Replace result placeholder with actual result
        user_input = user_input.replace('result', str(result))
        
        # Evaluate the expression
        result = calculate(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()