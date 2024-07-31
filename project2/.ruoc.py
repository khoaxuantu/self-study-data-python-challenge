# Vì e chưa biết cách nên hiện tại khi nhập biểu thức phải có dấu cách giữa các số và toán tử ví dụ như '1 + 2' hoặc '(1 + 2) * 3' mới thực hiện phép tính được ạ.
# Since I haven't found any way yet, currently when entering an expression, there must be a space between numbers and operators, for example '1 + 2' or '(1 + 2) * 3' to perform calculations.

operators = {
    '+': lambda a, b: a + b, 
    '-': lambda a, b: a - b, 
    '*': lambda a, b: a * b, 
    '/': lambda a, b: a / b, 
    '%': lambda a, b: a % b
    }

def set_up(expression):
    new_expression = []
    tmp_str = ''
    i = 0
    while i < len(expression):
        if '(' in expression[i]:
            tmp_str = expression[i].replace('(', '') + ' '
            i += 1
            while ')' not in expression[i]:
                tmp_str += expression[i] + ' '
                i += 1
            tmp_str += expression[i].replace(')', '')
            tmp = calculate(tmp_str.split())
            new_expression.append(tmp)
        else:
            new_expression.append(expression[i])
        i += 1
    return new_expression 
        
def calculate(expression):
    while '*' in expression or '/' in expression or '%' in expression:
        if '*' in expression:
            i = expression.index('*')
        elif '/' in expression:
            i = expression.index('/')
        elif '%' in expression:
            i = expression.index('%')
        if type(expression[i - 1]) == str:
            expression[i - 1] = expression[i - 1].replace('(', '').replace(')', '')
        if type(expression[i + 1]) == str:
            expression[i + 1] = expression[i + 1].replace('(', '').replace(')', '')
        result = operators[expression[i]](int(expression[i - 1]), int(expression[i + 1]))
        expression[i - 1] = result
        expression.pop(i)
        expression.pop(i)
    
    if type(expression[0]) == str:
        expression[0] = expression[0].replace('(', '').replace(')', '')
    result = int(expression[0])
    for i in range(1, len(expression) - 1, 2):
        if type(expression[i + 1]) == str:
            expression[i + 1] = expression[i + 1].replace('(', '').replace(')', '')
        result = operators[expression[i]](result, int(expression[i + 1]))
    return result


expression = input("Enter an expression (Please write your input in the form 'a + b' or '(a + b) * c)'): ")
while True:
    expression = expression.split()
    expression = set_up(expression)
    result = calculate(expression)

    print('Result:', result)
    ques1 = input("Do you want to continue? (y/n): ")
    while ques1.lower() not in ['y', 'n']:
        print('Invalid input. Please try again.')
        ques1 = input("Do you want to continue? (y/n): ")

    if ques1.lower() == 'n':
        break

    ques2 = input("Press 'c' to continue with the last result or 'n' to enter a new expression: ")
    while ques2.lower() not in ['c', 'n']:
        print('Invalid input. Please try again.')
        ques2 = input("Press 'c' to continue with the last result or 'n' to enter a new expression: ")
        
    if ques2.lower() == 'n':
        expression = input("Enter an expression (Please write your input in the form 'a + b' or '(a + b) * c)'): ")
    elif ques2.lower() == 'c':
        tmp = input(f"Enter an expression (Please write your input in the form 'a + b' or '(a + b) * c)'): {result} ")
        expression = str(result) + ' ' + tmp
