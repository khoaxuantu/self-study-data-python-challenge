def evaluate_expression(expression):
    elements = expression.split()
    if len(elements) < 3:
        raise ValueError("Invalid expression: must have at least 3 elements")
    
    result = float(elements[0])
    
    for i in range(1, len(elements), 2):
        operator = elements[i]
        operand = float(elements[i+1])
        
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if operand == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result /= operand
        elif operator == '%':
            if operand == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result %= operand
        else:
            raise ValueError(f"Invalid operator: {operator}")
    
    return result

def calculator():
    print("Welcome to the calculator program!")
    print("Please enter mathematical expressions in the format: 'number operator number'")
    print("Supported operators: +, -, *, /, %")
    print("For example, try entering: '2 + 3', '10 - 4', '5 * 6', '8 / 2', '7 % 3'")
    print("Type 'q' to quit the program.")

    while True:
        expression = input("Enter a mathematical expression (or 'q' to quit): ")
        if expression.lower() == 'q':
            break
        
        try:
            result = evaluate_expression(expression)
            print(f"{expression} = {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
#Nice work!
#Eval function is allowed, I recommend looking through it!