import re

def calculate(expression):
    try:
        # Replace 'x' with '*' for multiplication
        expression = expression.replace('x', '*')

        # Remove spaces and validate input
        expression = re.sub(r'\s+', '', expression)
        if not re.match(r'^[0-9+\-*/().%]+$', expression):
            return "Invalid input"

        result = eval(expression)
        return result
    except (SyntaxError, ZeroDivisionError):
        return "Invalid input"

print("Hi, welcome to Calculator")
print("Enter an expression (e.g., 2 + 3 - 4 or (4 * 5) % 6):")

while True:
    expression = input(">>> ")
    result = calculate(expression)
    print("Result:", result)

    another_calculation = input("Do another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        print ("ok, bye bye" )
        break

#Good job! Keep it up!