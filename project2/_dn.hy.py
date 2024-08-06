import sympy as sp

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Denominator cannot be zero."

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error! Denominator cannot be zero."

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input! Please enter a number.")

def evaluate_expression(expression):
    try:
        # Parse and evaluate the expression using sympy
        expr = sp.sympify(expression)
        result = expr.evalf()
        return result
    except (sp.SympifyError, ZeroDivisionError):
        return "Invalid expression or division by zero."

def main():
    while True:
        print("\nEnter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        print("Enter 'R' for Modulus.")
        print("You can also enter a mathematical expression using +, -, *, /, and %.")
        print("For example: (2 + 3) * 4")
        
        choice = input("Enter Choice (A,S,M,D,R) or an expression: ").upper()

        if choice in ['A', 'S', 'M', 'D', 'R']:
            numbers = []
            while True:
                num = get_number("Enter a number (or type 'done' to finish): ")
                numbers.append(num)
                if input("Do you want to add another number (yes/no)? ").lower() == 'no':
                    break

            if len(numbers) < 2:
                print("You must enter at least two numbers.")
                continue

            result = numbers[0]
            for num in numbers[1:]:
                if choice.upper() == 'A':
                    result = addition(result, num)
                elif choice.upper() == 'S':
                    result = subtraction(result, num)
                elif choice.upper() == 'M':
                    result = multiplication(result, num)
                elif choice.upper() == 'D':
                    if num == 0:
                        print("Error! Division by zero.")
                        result = "undefined"
                        break
                    result = division(result, num)
                elif choice.upper() == 'R':
                    if num == 0:
                        print("Error! Modulus by zero.")
                        result = "undefined"
                        break
                    result = modulus(result, num)

            if result != "undefined":
                operations = {'A': '+', 'S': '-', 'M': '*', 'D': '/', 'R': '%'}
                operation = operations[choice]

                expression = f"{numbers[0]}"
                for num in numbers[1:]:
                    expression += f" {operation} {num}"

                print(f"Result: {expression} = {round(result,2)}")
        else:
            result = evaluate_expression(choice)
            print(f"Result: {choice} = {round(result,2)}")

        if input("Do you want to perform another calculation (yes/no)? ").lower() == 'no':
            break

if __name__ == "__main__":
    main()