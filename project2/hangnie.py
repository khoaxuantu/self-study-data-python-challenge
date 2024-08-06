def calculate(operator, num1, num2, num3):
    if operator == 'A':
        return num1 + num2 + num3
    elif operator == 'S':
        return num1 - num2 - num3
    elif operator == 'M':
        return num1 * num2 * num3
    elif operator == 'D':
        if num2 == 0:
            return "Division by zero error"
        return num1 / num2 / num3
    elif operator == 'MOD':
        return num1 % num2 % num3
    else:
        return "Invalid operator"


# add continuous calculation functionality
def calculate_1(operator, result, num4):
    if operator == 'A':
        return result + num4
    elif operator == 'S':
        return result - num4
    elif operator == 'M':
        return result * num4
    elif operator == 'D':
        if num4 == 0:
            return "Division by zero error"
        return result / num4
    elif operator == 'MOD':
        return result % num4
    else:
        return "Invalid operator"


while True:
    dict = {'A': 'addition', 'S': 'subtraction', 'M': 'multiplication', 'D': 'division', 'MOD': 'Modulo'}
    user_input = str(input(
        'Enter Choice (A, S, M, D, MOD) represent for (Addition, Subtraction, Multiplication, Division, Modulo) correspondingly: ')).upper()
    if user_input in dict:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        num3 = float(input('Enter third number: '))
        result = calculate(user_input, num1, num2, num3)
        print(f"Result: {result}")

        user_input_2 = input("Continue enter choice (A, S, M, D, MOD) to continue calculate: ").upper()
        if user_input_2 in dict:
            num4 = float(input('Enter fourth number: '))
            result1 = calculate_1(user_input_2, result, num4)
            print(f"Result: {result1}")
        else:
            break
    else:
        print('Invalid operator, try again!')
