# -*- coding: utf-8 -*-
"""nhungle_20519_project2_20240729.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16gcWveA2lbve8duY8cnjlAFkcoEX24bE

Các tính năng của 'My Calculator':
- Mỗi lần nhập chỉ được nhập 1 ký tự số 0 đến 9 và các dấu '+', '-', '*', '/', '%', '(', ')'
VD: Muốn nhập 12 thì nhấn '1' -> enter -> '2'. Nếu nhấn '12' sẽ bị báo lỗi

- Chọn 'd' (tương ứng DELETE) nếu muốn xóa ký tự cuối cùng
  
- Chọn 'a' (tương ứng AC) nếu muốn xóa toàn bộ biểu thức
  
- Chọn '=' để ra kết quả cuối cùng
  
- Chọn 'y|n' để tiếp tục tính toán. Nếu chọn ký tự khác sẽ bị báo lỗi
  
- Và nếu trong trường hợp nhập các phép tính không hợp lệ cũng sẽ bị báo lỗi
VD: 1+/5 hoặc (2-9)*6) hoặc (*3)-6
"""

def check_group_operations(lst):
    a = ''
    b = ''
    for key, value in enumerate(lst):
        if key < len(lst)-1 and value == '(' and lst[key+1] == ')':
            return 'ERROR'
        elif key < len(lst)-1 and value in ('+', '-', '*', '/', '%') and lst[key+1] in ('+', '-', '*', '/', '%'):
            return 'ERROR'
        elif key < len(lst)-1 and value == '(' and lst[key+1] in ('+', '-', '*', '/', '%'):
            return 'ERROR'
        elif key < len(lst)-1 and value in ('+', '-', '*', '/', '%') and lst[key+1] == ')':
            return 'ERROR'
        elif value == '(':
            a += value
        elif value ==')':
            b += value
    if len(a) != len(b):
        return 'ERROR'


q = 'Y'
while q == 'Y':
    print("***********CALCULATOR***********")
    print("Enter '0|1|2|3|4|5|6|7|8|9' to choose number")
    print("Enter '.'                   to choose '.'")
    print("Enter '+'                   to choose '+'")
    print("Enter '-'                   to choose '-'")
    print("Enter '*'                   to choose '*'")
    print("Enter '/'                   to choose '/'")
    print("Enter '%'                   to choose '%'")
    print("Enter '('                   to choose '('")
    print("Enter ')'                   to choose ')'")
    print("Enter 'd'                   to choose 'DEL'")
    print("Enter 'a'                   to choose 'AC'")
    print("Enter '='                   to choose '='")

    expression = []
    val = ''

    while val != '=':

        print('________________')
        print('|',1,2,3,'DEL','AC','|')
        print('|',4,5,6,'+','  -',' |')
        print('|',7,8,9,'*','  /',' |')
        print('|',1,2,3,'(','  )',' |')
        print('|',0,'.','  %','  =',' |')

        val = str(input("Enter: "))
        if len(val) == 1:
            if val == '=':
                if check_group_operations(expression) == 'ERROR':
                    print('ERROR')
                    break
                else:
                    print(''.join(expression), ' = ', float(eval(''.join(expression))))
                    break
            elif val.lower() == 'd':
                if expression:
                    expression.pop()

                    print(''.join(expression))
                    continue
                else:
                    break
            elif val.lower() == 'a':
                expression.clear()
                break


            expression.append(val)
            print(''.join(expression))

        else:
            print('Only one character.')
    while True:
        q = input("Continue? Y/N: ").upper()
        if q in ['Y', 'N']:
            break
        else:
            print('No Valid! Please enter y or n.')
    print("************************************************************************")
else:
    print('Thanks for watching!!!')