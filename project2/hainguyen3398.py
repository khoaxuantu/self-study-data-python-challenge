def is_operator(character):
    return character in ['+', '-', '*', '/','%']

def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/' or operator == '%':
        return 2
    return -1

def process_operator(result, operator):
    right = result.pop()
    left = result.pop()
    if operator == '+':
        result.append(left + right)
    elif operator == '-':
        result.append(left - right)
    elif operator == '*':
        result.append(left * right)
    elif operator == '%':
        result.append(left % right)
    elif operator == '/':
        if right == 0:
            print('Biểu thức có phép chia cho 0: ' + str(left) + '/' + str(right))
            result.append(float("inf"))
        else:
            result.append(left / right)
    return result

def evaluate(string):
    results = []
    operators = []
    check_number = [False] * len(string)
    i = 0
    while i < len(string):
        if string[i] == ' ':
            i += 1
            continue
        elif string[i] == '(':
            operators.append('(')
        elif string[i] == ')':
            while operators[-1] != '(':
                results = process_operator(results, operators[-1])
                operators.pop()
            operators.pop()
        elif is_operator(string[i]):
            cur_operator = string[i]
            if i == 0 or string[i-1] == '(' or is_operator(string[i-1]):
                if cur_operator == '-' and (i == 0 or string[i-1] == '(' or is_operator(string[i-1])):
                    i += 1
                    num = 0
                    decimal_found = False
                    decimal_place = 1
                    while i < len(string) and (string[i].isnumeric() or string[i] == '.'):
                        if string[i].isnumeric():
                            if decimal_found:
                                decimal_place *= 10
                                num += float(string[i]) / decimal_place
                            else:
                                num = num * 10 + float(string[i])
                        elif string[i] == '.':
                            if not decimal_found:
                                decimal_found = True
                            else:
                                break
                        i += 1
                    results.append(-num)
                    continue
            while len(operators) != 0 and priority(operators[-1]) >= priority(cur_operator):
                results = process_operator(results, operators[-1])
                operators.pop()
            operators.append(cur_operator)
        else:
            num = 0
            decimal_found = False
            decimal_place = 1
            while i < len(string) and (string[i].isnumeric() or string[i] == '.'):
                if string[i].isnumeric():
                    if decimal_found:
                        decimal_place *= 10
                        num += float(string[i]) / decimal_place
                    else:
                        num = num * 10 + float(string[i])
                elif string[i] == '.':
                    if not decimal_found:
                        decimal_found = True
                    else:
                        break
                i += 1
            results.append(num)
            continue
        i += 1
        if float("inf") in results:
            break
        print("st=",results,"op=",operators,"mst=",check_number)
    while operators:
        results = process_operator(results, operators[-1])
        if float("inf") in results:
            break
        operators.pop()
    return results[0]

cont = True
ans = 0
while cont:
    formula = input('Nhập biểu thức cần tính (gồm các phép tính cộng, trừ, nhân, chia, lấy dư và dấu ngoặc đơn): ')
    formula = formula.replace('ans', str(ans))
    result = evaluate(formula)
    if result != float("inf"):
        print('Kết quả của biểu thức là: %s' % str(result))
        ans = result
    tiep = input('Bạn có muốn tiếp tục không (Y/N)? ')
    if tiep.upper() == 'Y':
        print('Dùng ans để sử dụng kết quả trước đó nếu muốn')
        cont = True
    else:
        cont = False

#Noice! You nailed it! Keep it up
