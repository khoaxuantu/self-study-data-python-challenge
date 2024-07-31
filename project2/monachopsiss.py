def calculate(cal):
    try:
        result = eval(cal)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the advanced calculator!")
    print("You can use +, -, *, /, %, and parentheses for operations.")
    print("For continuous calculation, type 'c' to continue with the result.")
    print("Type 'q' to quit the program.")

    result = None
    while True:
        if result is None:
            cal = input("Enter your calculation: ")
        else:
            cal = input(f"Enter your calculation (or type 'c' to use {result}): ")
            if cal.lower() == 'c':
                cal = input(f"Continue calculation with {result}: ")
                cal = f"{result} {cal}"
        
        if cal.lower() == 'x':
            print("...")
            break

        result = calculate(cal)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
