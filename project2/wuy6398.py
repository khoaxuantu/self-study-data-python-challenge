#Hướng dẫn sử dụng
print('''Enter '+' for Addition.
Enter '-' for Subtraction.
Enter '*' for Multiplication.
Enter '/' for Division.
Enter '%' for Modulus.
Enter '=' for Result.
''')

#Hàm kiểm tra ngoặc đóng
check_bracket = lambda x: 0 if x == 0 else 1

#Hàm kiểm tra số nhập vào có hợp lệ không
check_digit = lambda x: float(x) if x.isdigit() else check_digit(input('Invalid Number! Enter Again:'))

#Nhập số đầu tiên
result = check_digit(input('Enter Number:'))

#Các biến hỗ trợ khác
ope = ''
count = 0
result_str = '{}'.format(result)

while ope != '=':

    #Nhập ký hiệu mong muốn
    ope = input('Enter Operator of Choice (+, -, *, /, %, =):')

    #Kiểm tra tính hợp lệ của ký hiệu
    if ope not in '+-*/%=':
        print('Invalid Operator Input!')
    elif ope in '+-*/%':
        #Nhập số tiếp theo
        number = check_digit(input('Enter Next Number:'))
        
        #Thực hiện tính toán
        if ope == '+':
            result += number
            result_str += ')'*check_bracket(count) + ' + {}'.format(number)
            count += 1
        elif ope == '-':
            result -= number
            result_str += ')'*check_bracket(count) + ' - {}'.format(number)
            count += 1
        elif ope == '*':
            result *= number
            result_str += ')'*check_bracket(count) + ' * {}'.format(number)
            count += 1
        elif ope == '/':
            result /= number
            result_str += ')'*check_bracket(count) + ' / {}'.format(number)
            count += 1
        elif ope == '%':
            result %= number
            result_str += ')'*check_bracket(count) + ' % {}'.format(number)
            count += 1

    #In kết quả
    else:
        print(f'\nResult: {"("*(count-1)}{result_str} = {result}')
#Nice job!
#Python is famous for its large number of built-in functions!
#In this project it is allowed to use the eval() function. I recommend looking through it!