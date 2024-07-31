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
    expression = input("Enter calculation (ex: a + b + c or (a + b) * c): ")
    result = evaluate_expression(expression)
    print(f"Result: {result}")

print("Select operation.")
print("Enter 1 for Addition (+).")
print("Enter 2 for Subtract (-).")
print("Enter 3 for Multiply (*).")
print("Enter 4 for Divide (/).")
print("Enter 5 for Modulus (%).")
print("Enter 6 for Three Number Operations (a, b, c).")
print("Enter 0 for Exit.")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/0): ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
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
        
        next_calculation = input("Next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break

    elif choice == '6':
        three_number_operations()
        
        next_calculation = input("Next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    elif choice == '0':
        break
    else:
        print("Invalid Input")
