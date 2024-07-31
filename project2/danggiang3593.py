def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

def evaluate_expression(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {e}"

def three_number_operations():
    print("You can enter calculations like 'a + b + c' or '(a + b) * c'.")
    expression = input("Enter your expression: ")
    result = evaluate_expression(expression)
    print(f"Result: {result}")

def continuous_calculation():
    result = None
    print("You can chain calculations. For example, '5 + 3' followed by ' * 2' will use the previous result.")
    while True:
        if result is not None:
            expression = input(f"Current result is {result}. Enter next calculation or type 'exit' to quit: ")
            if expression.lower() == 'exit':
                break
            expression = f"{result} {expression}"
        else:
            expression = input("Enter calculation or type 'exit' to quit: ")

        if expression.lower() == 'exit':
            break

        result = evaluate_expression(expression)
        print(f"Result: {result}")

def menu():
    print("Welcome to the Calculator!")
    print("Select an operation by entering the corresponding number.")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Three Number Operations (e.g., a + b + c or (a + b) * c)")
    print("7. Continuous Calculations (e.g., A + B = AB, AB + C = ABC)")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7 or 0): ")

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
            
            next_calculation = input("Would you like to make another calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                break

        elif choice == '6':
            three_number_operations()
            
            next_calculation = input("Would you like to make another calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                break

        elif choice == '7':
            continuous_calculation()
        
        elif choice == '0':
            break
        
        else:
            print("Invalid. Please enter a number between 0 and 7.")

if __name__ == "__main__":
    menu()