def continue_exp(ans, expression):
    expression_2 = str(ans)+  str(expression)
    return eval(expression_2)

expression = str(input('Type in the expression: '))
try:
    result = eval(expression)
    result_0 = result
    print(f'Result: {expression} = {result}')
except Exception:
    print(f"Invalid expression !!!")
choose = 1
while choose == 1:
    print('Do you want to continue with the results obtained ?')
    choose = int(input('(Type 1 = "yes", 2 = "no"): ').strip())
    if choose != 1:
        print('Doneeeee')
        break
    expression = str(input('Type in the expression: '))
    result = continue_exp(result_0, expression)
    print(f'Result: {result_0} {expression} = {result}')

#Nice! You overkill this project.