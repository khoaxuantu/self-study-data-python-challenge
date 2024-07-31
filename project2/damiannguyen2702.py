# Project 2: Basic Calculator / damiannguyen2702.

def calculate(expression):
    try:
        # Evaluates the mathematical expression provided as a string
        result = eval(expression)
        return result
    except ZeroDivisionError:
        # Handles division by zero errors
        return "Error! Division by zero."
    except Exception as e:
        # Handles any other exceptions and returns the error message
        return f"Error! {str(e)}"

def main():
    prev_result = None  # Variable to store the previous calculation result
    while True:
        print("Enter 'exit' to end the program.")
        
        # Prompt the user for input, suggesting the use of the previous result if available
        if prev_result is not None:
            expression = input(f"Enter your calculation (or use the previous result {prev_result}): ")
        else:
            expression = input("Enter your calculation: ")
        
        # Check if the user wants to exit the program
        if expression.lower() == 'exit':
            break
        
        # Replace 'prev' in the expression with the previous result if it exists
        if prev_result is not None:
            expression = expression.replace("prev", str(prev_result))
        
        # Calculate the result of the expression
        result = calculate(expression)
        print(f"Result: {result}")
        
        # Update the previous result if the calculation was successful
        if isinstance(result, (int, float)):
            prev_result = result
        else:
            prev_result = None  # Reset previous result if the calculation failed

# Ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
