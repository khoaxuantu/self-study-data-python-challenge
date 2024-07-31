def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulo(x, y):
    return x % y


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    while True:
        print("Enter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        print("Enter 'Mod' for Modulo.")

        while True:
            choice = input("Enter choice (A/S/M/D/Mod): ").upper()
            if choice in ['A', 'S', 'M', 'D', 'MOD']:
                break
            print("Invalid choice. Please enter 'A', 'S', 'M', 'D', or 'Mod'.")

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == 'A':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == 'S':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 'M':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 'D':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
        if another_calculation != 'y':
            print("Goodbye!")
            break
if __name__ == "__main__":
    calculator()
