def add(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number
    return result

def subtract(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result

def multiply(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return result

def divide(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        if number != 0:
            result /= number
        else:
            return "Error! Division by zero."
    return result

def modulo(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result %= number
    return result

def continuous_calculation():
    print("Welcome to the Calculator!")
    print("You can use +, -, *, /, %, and parentheses for grouping.")
    print("Enter 'q' to quit at any time.")
    
    current_result = 0
    while True:
        if current_result == 0:
            expression = input("Enter your calculation: ")
        else:
            expression = input(f"Enter your calculation (current result is {current_result}): ")
            expression = f"{current_result}{expression}"
        
        if expression.lower() == 'q':
            break
        
        # Check for multiple operations and handle them
        if '+' in expression:
            parts = expression.split('+')
            numbers = [float(part) for part in parts]
            current_result = add(numbers)
        elif '-' in expression:
            parts = expression.split('-')
            numbers = [float(part) for part in parts]
            current_result = subtract(numbers)
        elif '*' in expression:
            parts = expression.split('*')
            numbers = [float(part) for part in parts]
            current_result = multiply(numbers)
        elif '/' in expression:
            parts = expression.split('/')
            numbers = [float(part) for part in parts]
            current_result = divide(numbers)
        elif '%' in expression:
            parts = expression.split('%')
            numbers = [float(part) for part in parts]
            current_result = modulo(numbers)
        else:
            current_result = evaluate_expression(expression)
        
        print(f"Result: {current_result}")

continuous_calculation()
