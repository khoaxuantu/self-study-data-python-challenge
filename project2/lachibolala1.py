import operator
def calculator():
    operators ={
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod
    }
    def evaluate_expression(expression):
        try:
            result = eval(expression, {"__builtins__": None}, operators)
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Division by zero is not allowed!"
        except Exception as e:
            return f"Error: {e}"
        
        print("Welcome to the Calculator!")
    result = None
    while True:
        try:
            if result is None:
                expression = input("Enter the expression or 'exit' to quit: ")
                if expression.lower() == 'exit':
                    break
                result = eval(expression, {"__builtins__": None}, operators)
            else:
                expression = input(f"Result: {result}. Enter next operation or 'exit' to quit: ")
                if expression.lower() == 'exit':
                    break
                result = eval(f"{result}{expression}", {"__builtins__": None}, operators)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Division by zero is not allowed!")
            result = None
        except Exception as e:
            print(f"Error: {e}")
            result = None

calculator()
#Gud job! However, I believe you can imporve your code by make it more user-friendly! Guide your user how to use it, not everyone read the code like us.
#Keep it up!!