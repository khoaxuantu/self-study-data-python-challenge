# Basic Operations
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
        return "Division by zero error"

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Division by zero error"

# Choose operation
operations = ['A', 'S', 'M', 'D', 'O']

def basic_calculator():
    choice = input("Enter 'A' for Addition\n"
                   "Enter 'S' for Subtraction\n"
                   "Enter 'M' for Multiplication\n"
                   "Enter 'D' for Division\n"
                   "Enter 'O' for Modulo\n"
                   "Enter choice (A/S/M/D/O): ").upper()

    if choice not in operations:
        print("Invalid operation. Please enter choice (A/S/M/D/O).")
    else:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 'A':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 'S':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 'M':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 'D':
                print(num1, "/", num2, "=", divide(num1, num2))
            elif choice == 'O':
                print(num1, "%", num2, "=", modulo(num1, num2))
        except ValueError:
            print("Invalid input. Please enter a number.")

def advanced_calculator():
    def calculate(expression):#expression is expected to be a mathematical string
        try:
            result = eval(expression)#eval function takes a string expression and evaluates it as a Python expression
            return result
        except Exception as e:# handling invalid like "2 + 3 *"
            return str(e)

    result = None
    while True:
        if result is None:
            expression = input("Enter your calculation (e.g., 2 + 3 * 4) or 'exit' to quit: ")
        else:
            expression = input(f"Current result: {result}. Enter next calculation (e.g., + 3 * 4) or 'exit' to quit: ")
            expression = str(result) + expression
        
        if expression.lower() == 'exit':
            break
        
        result = calculate(expression)
        print(f"Result: {result}")

while True:
    mode = input("Choose calculator mode:\n1. Basic Operations\n2. Advanced Calculator\nEnter choice (1/2) or 'exit' to quit: ")
    
    if mode == '1':
        basic_calculator()
    elif mode == '2':
        advanced_calculator()
    elif mode.lower() == 'exit':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 'exit'.")
