def basic_calculator():
    def evaluate_expression(expression):
        try:
            # Evaluate the expression while handling parentheses, order of operations, etc.
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    print("Welcome to the Basic Calculator!")
    print("Enter 'exit' to quit the calculator.")
    print("Supported operations: +, -, *, /, %")
    print("You can use parentheses for grouping operations.")
    print("You can perform continuous calculations.")

    previous_result = None
    while True:
        if previous_result is not None:
            expression = input(f"Continue with {previous_result}, enter next operation: ")
            if expression == "exit":
                break
            expression = f"{previous_result}{expression}"
        else:
            expression = input("Enter your expression: ")
            if expression == "exit":
                break


        result = evaluate_expression(expression)
        if "Error" not in str(result):
            previous_result = result
        else:
            previous_result = None
    
        print(f"Result: {result}")

basic_calculator()

#Noiceee! You nailed it this time! Keep it up!!