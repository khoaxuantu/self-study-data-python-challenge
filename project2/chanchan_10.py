class Calculator:
    def __init__(self):
        pass

    def evaluate(self, expression):
        try:
            expression = expression.replace(' ', '')
            return self._evaluate_expression(expression)
        except Exception as e:
            return f"Error: {str(e)}"

    def _evaluate_expression(self, expression):
        while '(' in expression:
            start = expression.rfind('(')
            end = expression.find(')', start)
            if end == -1:
                raise ValueError("Mismatched parentheses")
            inner_result = self._evaluate_expression(expression[start+1:end])
            expression = expression[:start] + str(inner_result) + expression[end+1:]

        return self._calculate(expression)

    def _calculate(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        def apply_operator(operators, values):
            operator = operators.pop()
            right = values.pop()
            left = values.pop()
            if operator == '+':
                values.append(left + right)
            elif operator == '-':
                values.append(left - right)
            elif operator == '*':
                values.append(left * right)
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                values.append(left / right)
            elif operator == '%':
                values.append(left % right)

        operators = []
        values = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                values.append(float(expression[i:j]))
                i = j
            elif expression[i] in precedence:
                while (operators and
                       operators[-1] in precedence and
                       precedence[operators[-1]] >= precedence[expression[i]]):
                    apply_operator(operators, values)
                operators.append(expression[i])
                i += 1
            else:
                raise ValueError(f"Unknown character: {expression[i]}")

        while operators:
            apply_operator(operators, values)

        return values[0]

def main():
    calculator = Calculator()
    print("Simple Calculator")
    while True:
        expression = input("Enter your calculation (or type 'exit' to quit): ")
        if expression.lower() == 'exit':
            break
        result = calculator.evaluate(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
#Keep up the good works!