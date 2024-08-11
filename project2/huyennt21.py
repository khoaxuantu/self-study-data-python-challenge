def isnumber(num):
    """Checks the input is a valid number or not."""
    try:
        float(num)
        return True
    except:
        return False


def single_operator():
    """Prompts user to select a single mathematical operation (addition, subtraction, multiplication,
    division, or modulo). It then allows user to input numbers for continuous calculations with the
    chosen operation."""
    # Instructions
    print("----------")
    print("Enter 'A' for Addition")
    print("Enter 'S' for Subtraction")
    print("Enter 'M' for Multiplication")
    print("Enter 'D' for Division")
    print("Enter 'O' for Modulo (%)")

    # Input Operator and validate
    while True:
        operator = input("Enter choice Operator (A,S,M,D,O): ")
        if operator.upper() in ['A', 'S', 'M', 'D', 'O']:
            break
        else:
            print("--ERROR! Chose 'A'/'S'/'M'/'D'/'O', please!")

    # Instructions
    print("----------")
    print("Enter NUMBER for Operand")
    print("Enter 'R' to get Result")
    print("----------")

    # Input First Number and validate, Assign variable 'result'
    while True:
        try:
            first_number = float(input("Enter first number: "))
            result = first_number
            break
        except:
            print("--ERROR! Enter NUMBER, please!")

    # While loop for repeat
    while True:
        # Input Next Numbers and validate, Calculate variable 'result'
        while True:
            number = input("Enter next number: ")
            if isnumber(number):
                if operator.upper() == 'A':
                    result += float(number)
                elif operator.upper() == 'S':
                    result -= float(number)
                elif operator.upper() == 'M':
                    result *= float(number)
                elif operator.upper() == 'D':
                    if number != '0':
                        result /= float(number)
                    elif number == '0':
                        print("--ERROR! Enter NUMBER <> 0, please!")
                elif operator.upper() == 'O':
                    result %= float(number)
            elif number.upper() == 'R':
                break
            else:
                print("--ERROR! Enter NUMBER, please!")

        # Print result
        print(f"Result: {result}")
        repeat = input("Do you want to continue (Y/N)? ")
        if repeat.upper() != 'Y':
            break


def multi_operator1():
    """Allows user to input an entire mathematical expression using various operators and parentheses.
    The expression is then evaluated, and the result is displayed."""
    # Instructions
    print("----------")
    print("Enter NUMBER for Operand")
    print("Enter '+', '-', '*', '/', '%' for Operator")
    print("Enter '(' for Opening Parenthesis")
    print("Enter ')' for Closing Parenthesis")
    print("Press ENTER to get Result")
    print("----------")

    # While loop for repeat
    result = ''
    while True:
        # Input entire Operation, Calculate variable 'result'
        while True:
            operation = str(result) + input("Input entire Operation: ")
            try:
                result = eval(operation)
                break
            except:
                print("--SyntaxError!")
                # Print result
        print(f"Result: {operation} = {result}")
        repeat = input("Do you want to use this result to continue (Y/N)? ")
        if repeat.upper() == 'Y':
            print(
                f"Your next Operation start with {result}. So, your next input need to start with OPERATOR ('+', '-', '*', '/', '%')")
        else:
            break


def multi_operator2():
    """Similar to multi_operator1(), but the user inputs each element of the operation separately.
    It checks for syntax errors and validates the order of inputs."""
    # Instructions
    print("----------")
    print("Enter NUMBER for Operand")
    print("Enter '+', '-', '*', '/', '%' for Operator")
    print("Enter '(' for Opening Parenthesis")
    print("Enter ')' for Closing Parenthesis")
    print("Enter '=' to get Result")
    print("----------")

    # Input First Element and validate, Assign variable 'user_input', 'recorded_input', 'operation'
    while True:
        user_input = input("Input first element: ")
        if isnumber(user_input) or user_input == '(':
            recorded_input = user_input
            operation = recorded_input
            break
        else:
            print("--ERROR! Enter NUMBER or Opening Parenthesis, please!")

    # While loop for repeat
    while True:
        # Input Next Elements and validate, Calculate variable 'result'
        while True:
            user_input = input("Input next element: ")
            # Calculate variable 'result'
            if user_input.upper() == '=':
                try:
                    result = eval(operation)
                    break
                except:
                    print(f"--SyntaxError! Operation = {operation}. Enter next element, please!")
            # Check Syntax Error
            elif isnumber(recorded_input) and user_input not in ['+', '-', '*', '/', '%', ')']:
                if operation.count('(') == operation.count(')'):
                    print(f"--SyntaxError! Operation = {operation}. Enter OPERATOR, please!")
                else:
                    print(f"--SyntaxError! Operation = {operation}. Enter OPERATOR or ')', please!")
            elif recorded_input in ['+', '-', '*', '/', '%', '('] and not isnumber(user_input) and user_input != '(':
                print(f"--SyntaxError! Operation = {operation}. Enter NUMBER or '(', please!")
            elif recorded_input == '/' and user_input == '0':
                print(f"--SyntaxError! Operation = {operation}. Enter NUMBER <> 0 or '(', please!")
            elif recorded_input == ')' and user_input not in ['+', '-', '*', '/', '%', ')']:
                print(f"--SyntaxError! Operation = {operation}. Enter OPERATOR, please!")
            elif operation.count('(') == operation.count(')') and user_input == ')':
                print(f"--SyntaxError! Operation = {operation}. Enter OPERATOR, please!")
            # Assign variable 'recorded_input', 'operation'
            elif isnumber(user_input) or user_input in ['+', '-', '*', '/', '%', '(', ')']:
                recorded_input = user_input
                operation += recorded_input
            # Check Syntax Error
            else:
                print(f"--SyntaxError! Operation = {operation}. Enter next element, please!")

        # Print result
        print(f"Result: {operation} = {result}")
        repeat = input("Do you want to use this result to continue (Y/N)? ")
        if repeat.upper() == 'Y':
            operation = str(result)
        else:
            break


# Instructions
print("SELECT CALCULATOR:")
print("Enter 'S' for Single-Operator")
print("Enter 'M1' for Multi-Operator, Enter entire Operation")
print("Enter 'M2' for Multi-Operator, Enter each element of Operation")

# Input type of Calculator
while True:
    calculator = input('Enter choice Calculator (S,M1,M2): ')
    if calculator.upper() in ['S', 'M1', 'M2']:
        break
    else:
        print("--ERROR! Chose 'S'/'M1'/'M2', please!")

# Run function
if calculator.upper() == 'S':
    single_operator()
elif calculator.upper() == 'M1':
    multi_operator1()
elif calculator.upper() == 'M2':
    multi_operator2()

#Nice! You overkill this project! Keep it up!!