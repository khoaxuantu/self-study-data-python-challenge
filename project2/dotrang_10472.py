def calculate_expression(expression):
    try:
        expression = expression.replace("^", "**")
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error. Cannot divide by zero"
    except Exception as e:
        return f"Error. Invalid expression({str(e)})."

def main():
    while True:
        print("Enter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        
        operator = input("Enter choice (A,S,M,D): ").strip().upper()
        if operator not in ['A', 'S', 'M', 'D']:
            print("Invalid choice. Please try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        initial_expression = f"{a} {operator} {b}"
        result = calculate_expression(initial_expression.replace("A", "+").replace("S", "-").replace("M", "*").replace("D", "/"))
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {a} {operator} {b} = {result:.2f}")

        while True:
            next_step = input(f"{result:.2f} ").strip()
            if next_step.lower() == 'exit':
                print("Starting a new expression.")
                break

            new_expression = f"{result} {next_step}"
            result = calculate_expression(new_expression)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {new_expression} = {result:.2f}")

if __name__ == "__main__":
    main()
