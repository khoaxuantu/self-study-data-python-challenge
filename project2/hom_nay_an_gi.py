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

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception as e:
        return f"Error! {str(e)}"

def main():
    while True:
        print("Enter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        print("Enter 'Mod' for Modulo.")
        print("Enter 'Q' to Quit.")
        
        choice = input("Enter Choice (A, S, M, D, Mod, Q): ").upper()
        
        if choice == 'Q':
            print("Calculator stopped.")
            break
        
        expression = input("Enter the expression (e.g., 20 + 40 * (2 - 1)): ")
        result = calculate(expression)
        if "Error" in str(result):
            print(result)
            print("Calculator stopped due to wrong input.")
            break
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
