import operator

def calculator():
    print("\n               CALCULATOR \n")
    print("Can perform calculations: +, -, *, /, % \n")

    def calculate(op, x, y):
            operators = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv,
                '%': operator.mod
                }
            return operators[op](x, y)

    while True:
        expression = input("Enter your expression (or 'q' to quit): ")
        if expression.lower() == 'q':
            print("Thanks!")
            break

        try:
            result = eval(expression)
            print(result)
            operation = input("Enter operation (+, -, *, /, %, or 'q' to quit): ")
            if operation == 'q':
                print("Thanks!")
                break
            num = float(input("Enter a number: "))
            result = calculate(operation, result, num)
            print("Result:", result)
        except (SyntaxError, ZeroDivisionError) as e:
            print("Error:", e)

calculator()