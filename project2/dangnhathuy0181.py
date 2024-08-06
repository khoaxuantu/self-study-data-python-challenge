def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

def percentage(a, b):
    return (a / b) * 100

def result(str1,a,b):
    return operation2[str1](a,b)

operation1 = {'+':'Addition', '-':'Subtraction', '*':'Multiplication', '/':'Division', '%':'Percentage', '(' : 'Open Bracket', ')': 'End Bracket'}
operation2 = {'+':addition, '-': subtraction, '*': multiplication, '/': division , '%': percentage}
for key, value in operation1.items():
    print(f"Enter {key} for {value}.")

num1 = float(input("Enter number: "))
while True:
    opr = input(f"Enter operation ({','.join(operation1.keys())}): ", )
    if opr == 'Exit':
        break
    num2 = float(input("Enter number: "))
    print(f"Result: {num1} {opr} {num2} = {result(opr,num1,num2)}")
    num1 = result(opr,num1,num2)