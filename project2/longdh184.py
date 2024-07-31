def parse_expression(expression):
    tokens = []
    num = ""
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if char in "+-*/%":
                tokens.append(char)
    if num:
        tokens.append(num)
    return tokens

def evaluate(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    operands = []
    operators = []
    for token in tokens:
        if token.isdigit() or '.' in token:
            operands.append(float(token))
        elif token in precedence:
            while operators and precedence[operators[-1]] >= precedence[token]:
                print(precedence[operators[-1]])
                print(precedence[token])
                apply_operator(operands, operators.pop())
            operators.append(token)

    while operators:
        apply_operator(operands, operators.pop())

    return operands[0]

def apply_operator(operands, operator):
    right = operands.pop()
    left = operands.pop()
    if operator == '+':
        operands.append(left + right)
    elif operator == '-':
        operands.append(left - right)
    elif operator == '*':
        operands.append(left * right)
    elif operator == '/':
        operands.append(left / right)
    elif operator == '%':
        operands.append(left % right)

def calculator():
    print("Welcome to the calculator!")
    while True:
        expression = input("Enter your calculation (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        tokens = parse_expression(expression.replace(" ", ""))
        result = evaluate(tokens)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
