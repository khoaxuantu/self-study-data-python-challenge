def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def calculate_expression(expression, result):
    try:
        return eval(expression)
    except Exception as e:
        return str(e)

def main():
    result = 0
    print("Welcome to Summoner's rift")
    print("Enter 'exit' to lose this game.")

    operations = {
        'A': add,
        'S': subtract,
        'M': multiply,
        'D': divide,
        '%': modulo
    }

    while True:
        print("\nChoose an operation:")
        print("Enter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        print("Enter '%' for Modulo.")
        print("Enter 'E' for evaluating an expression.")
        print("Enter 'C' for continuous calculation.")

        choice = input("Enter Choice (A,S,M,D,%,E,C): ").strip().upper()

        if choice == 'EXIT':
            break

        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            result = operations[choice](num1, num2)
            op_symbols = {'A': '+', 'S': '-', 'M': '*', 'D': '/', '%': '%'}
            print(f"Result: {num1} {op_symbols[choice]} {num2} = {result}")

        elif choice == 'E':
            expression = input("Enter expression (use +, -, *, /, %): ").strip()
            result = calculate_expression(expression, result)
            print(f"Result: {expression} = {result}")

        elif choice == 'C':
            expression = input("Enter expression with 'result' as a variable (e.g., result + 2): ").strip()
            if 'result' not in expression:
                print("Expression must include 'result' for continuous calculation.")
                continue
            expression = expression.replace('result', str(result))
            result = calculate_expression(expression, result)
            print(f"Result: {expression} = {result}")

        else:
            print("Invalid choice. Please enter a valid option.")

        # Ask the user if they want to continue
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Nhẹ tay thôi các thầy ơi")
            break            

if __name__ == "__main__":
    main()

#Gud job! 
#But I hope you should utilize the eval() function more, since you have already used it.
#Keep up the good works!