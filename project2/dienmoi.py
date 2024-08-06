def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Cannot divide by zero")
        return None
    else:
        return x / y

def modulo(x, y):
    return x % y

def calculator():
    print("'A' for Addition ")
    print("'S' for Subtraction ")
    print("'M' for Multiplication ")
    print("'D' for Division ")
    print("'%' for Modulo ")
        
while True:
    choice = input("Enter (A, S, M, D, %): ")
        
    if choice in ['A', 'S', 'M', 'D', '%']:
        numbers = input("Enter numbers are separated by space: ").split()
        numbers = [float(num) for num in numbers]

        if len(numbers) != 2:
            print("You have to enter exactly 2 numbers")
            continue

        num1, num2 = numbers[0], numbers[1]

        if choice == 'A':
            result = add(num1, num2)
            operation = '+'
        elif choice == 'S':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == 'M':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == 'D':
            result = divide(num1, num2)
            operation = '/'
        elif choice == '%':
            result = modulo(num1, num2)
            operation = '%'

        if result is None:
            continue
        else:
            print(f"Result: {num1} {operation} {num2} = {result}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    calculator()
