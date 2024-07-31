#v_7.3
#I gave up lolS

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero."

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    return 0

def infix_to_postfix(expression):
    output = []
    operators = []
    for token in expression:
        if token.isdigit() or '.' in token:
            output.append(float(token))
        elif token in ('+', '-', '*', '/', '%'):
            while (operators and precedence(operators[-1]) >= precedence(token)):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
    while operators:
        output.append(operators.pop())
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if isinstance(token, float):
            stack.append(token)
        elif token in ('+', '-', '*', '/', '%'):
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(add(left, right))
            elif token == '-':
                stack.append(subtract(left, right))
            elif token == '*':
                stack.append(multiply(left, right))
            elif token == '/':
                stack.append(divide(left, right))
            elif token == '%':
                stack.append(modulo(left, right))
    return stack[0] if stack else "Error in evaluation"

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            tokens.append(num)
        elif expression[i] in '+-*/%()':
            tokens.append(expression[i])
            i += 1
        else:
            i += 1  # Skip any other characters
    return tokens

def main():
    print(" Void Calculator Simulation Activated.")
    print("Type 'done' to exit sim.")

    result = None
    while True:
        if result is not None:
            print(f"Current result: {result}")

        expression = input("Enter an expression (valid operators(+,-,*,/, %) or 'done' to finish): ").strip()
        if expression.lower() == 'done':
            print(f"Final result: {result}")
            break

        # Tokenize the expression
        tokens = tokenize(expression)
        
        # Convert to postfix notation
        postfix = infix_to_postfix(tokens)

        # Evaluate the postfix expression
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")

        # they will have to input it themselves? how should i implement adding in the previous results?
    
        cont = input("Do you want to continue with the current result? (yes/no): ").strip().lower()
        if cont == 'yes':
            
            expression = str(result) + ' ' + expression
            tokens = tokenize(expression)
            postfix = infix_to_postfix(tokens)
            result = evaluate_postfix(postfix)
            print(f"Updated result: {result}")

if __name__ == "__main__":
    main()
