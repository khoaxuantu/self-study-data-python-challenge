def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulo(x, y):
    return x % y

def calculate(expression, prev_result):
    try:
        # Replace 'PREV' with the previous result in the expression
        expression = expression.replace('PREV', str(prev_result))
        return eval(expression)
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception as e:
        return f"Error! {str(e)}"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    result = None
    while True:
        print("\nCalculator Options:")
        print("Enter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        print("Enter 'Mod' for Modulo.")
        print("Enter 'E' to enter a full expression.")
        print("To use the previous result in a full expression, use 'PREV'.")
        print("To start a new calculation, simply choose an operation and enter new numbers.")

        choice = input("Enter choice (A, S, M, D, Mod, E): ").upper()

        if choice in ['A', 'S', 'M', 'D', 'MOD']:
            if result is None:
                num1 = get_number("Enter first number: ")
            else:
                use_prev = input("Do you want to use the previous result? (yes/no): ").lower()
                if use_prev == 'yes':
                    num1 = result
                    print(f"Using previous result: {num1}")
                else:
                    num1 = get_number("Enter first number: ")

            num2 = get_number("Enter second number: ")

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
        elif choice == 'E':
            expression = input("Enter the full expression (use 'PREV' for previous result): ")
            result = calculate(expression, result)
            print("Result:", result)
        else:
            print("Invalid choice! Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator! Have a great day!")
            break

if __name__ == "__main__":
    main()
#Keep up the good works!