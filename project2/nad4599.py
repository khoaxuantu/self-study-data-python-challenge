import math

class AdvancedCalculator:
    def __init__(self):
        self.result = 0
        self.memory = 0
        self.first_input = True

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    def modulo(self, a, b):
        return a % b

    def square_root(self, a):
        return math.sqrt(a)

    def percentage(self, a, b):
        return (a / b) * 100

    def exponent(self, a, b):
        return a ** b

    def pi(self):
        return math.pi

    def round_2(self, a):
        return round(a, 2)

    def round_0(self, a):
        return round(a, 0)

    def plus_minus_toggle(self, a):
        return -a

    def memory_clear(self):
        self.memory = 0

    def memory_recall(self):
        return self.memory

    def memory_add(self, a):
        self.memory += a

    def memory_subtract(self, a):
        self.memory -= a

    def clear_entry(self):
        self.result = 0

    def all_clear(self):
        self.result = 0
        self.memory = 0

    def sanitize_expression(self, expression):
        sanitized_expression = []
        i = 0

        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                num = []
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num.append(expression[i])
                    i += 1
                sanitized_expression.append(str(float(''.join(num))))
            else:
                sanitized_expression.append(expression[i])
                i += 1

        return ''.join(sanitized_expression)

    def calculate_expression(self, expression):
        try:
            # Sanitize and evaluate the expression
            expression = self.sanitize_expression(expression)
            # Use eval to compute the result of the expression
            return eval(expression, {"math": math, "pi": math.pi})
        except Exception as e:
            raise ValueError(f"Error: {e}")

    def continuous_calculation(self):
        while True:
            if self.first_input:
                prompt = "Enter the expression (e.g., (20+30)*2, √25, 4 ^ 2, 10 % 2, π) or 'exit' to quit: "
                self.first_input = False
            else:
                prompt = "Enter the expression (e.g., + 30, /30, %30, -40) or 'exit' to quit: "

            expression = input(prompt)
            expression = expression.replace(' ', '').replace('√', 'math.sqrt').replace('^', '**').replace('π', 'math.pi')

            if expression.lower() == 'exit':
                break
            if expression.lower() == 'mc':
                self.memory_clear()
                print("Memory cleared.")
                continue
            if expression.lower() == 'mr':
                print(f"Memory recall: {self.memory_recall()}")
                continue
            if expression.lower() == 'm+':
                num = float(input("Enter number to add to memory: "))
                self.memory_add(num)
                print(f"Added {num} to memory.")
                continue
            if expression.lower() == 'm-':
                num = float(input("Enter number to subtract from memory: "))
                self.memory_subtract(num)
                print(f"Subtracted {num} from memory.")
                continue
            if expression.lower() == 'ce':
                self.clear_entry()
                print("Entry cleared.")
                continue
            if expression.lower() == 'ac':
                self.all_clear()
                print("All cleared.")
                continue

            try:
                # Handle expressions with '=' and continuous calculations
                if '=' in expression:
                    expression = expression.replace('=', '')
                    self.result = self.calculate_expression(expression)
                    print(f"Result: {self.result}")
                else:
                    if self.result == 0 and self.first_input:
                        self.result = self.calculate_expression(expression)
                    else:
                        self.result = self.calculate_expression(f'{self.result}{expression}')
                    print(f"Result: {self.result}")
            except ValueError as e:
                print(e)
                break

# Instantiate the calculator
calculator = AdvancedCalculator()

# Perform continuous calculation
calculator.continuous_calculation()

# Your current implementation of the AdvancedCalculator class does not correctly handle expressions like (a+b)*c in its calculate_expression method. 
# Specifically, the sanitize_expression method only processes the expression to handle individual numbers and basic operators, but it doesn't correctly preserve or handle the order of operations involving parentheses.
# Since our 5th requirement requires to complete all other requirement so you can get only 3 score.
# Keep it up! I believe be more careful will help you in your next project.


