def perform_operation(operation, numbers):
    if operation == 'A':
        return sum(numbers)
    elif operation == 'S':
        return numbers[0] - sum(numbers[1:])
    elif operation == 'M':
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == 'D':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
        return result
    elif operation == '%':
        if len(numbers) != 2:
            return "Error: Modulo operation requires exactly two numbers"
        if numbers[1] == 0:
            return "Error: Modulo by zero"
        return numbers[0] % numbers[1]

def calculator():
    operations = {
        'A': 'Addition',
        'S': 'Subtraction',
        'M': 'Multiplication',
        'D': 'Division',
        '%': 'Modulo'
    }
    
    while True:
        print("\nCalculator Menu:")
        for key, value in operations.items():
            print(f"Enter '{key}' for {value}")
        print("Enter 'Q' to Quit")
        
        choice = input("Enter Choice (A,S,M,D,%,Q): ").upper()
        
        if choice == 'Q':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue
        
        numbers = []
        while True:
            num = input("Enter a number (or press Enter to finish): ")
            if num == "":
                break
            try:
                numbers.append(float(num))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if len(numbers) < 2:
            print("Error: At least two numbers are required for calculation.")
            continue
        
        result = perform_operation(choice, numbers)
        
        operation_symbol = {
            'A': '+', 'S': '-', 'M': '*', 'D': '/', '%': '%'
        }[choice]
        
        numbers_str = f" {operation_symbol} ".join(map(str, numbers))
        print(f"Result: {numbers_str} = {result}")

calculator()