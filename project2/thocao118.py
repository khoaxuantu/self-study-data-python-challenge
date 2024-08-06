# Lời chào
print("\n\U0001F4D0 CHÀO MỪNG TỚI CALCULATOR \U0001F4D0\n")

# Hướng dẫn 
huong_dan = '''
________________________________
Những phép toán hệ thống hỗ trợ
'(' for mở ngoặc.
')' for đóng ngoặc.
'+' for Addition.
'-' for Subtraction.
'*' for Multiplication.
'/' for Division.
'%' for Modulo.

'Q' for Quit.
________________________________
Vui lòng chỉ nhập số và các phép toán trên, theo các công thức toán bình thường. 
Trường hợp nhập phép tính ngoài có thể dẫn tới sai kết quả.

Ví dụ: 
Nhập phép tính: 1/5-2*0*3%8+9
Kết quả: 1/5-2*0*3%8+9 = 9.2

________________________________
'''
print(huong_dan)


# Tính toán ________________________________________________________________
result = ''
while True:
    phep_tinh = input('Nhập phép tính: ',).replace(' ','')
    
    if phep_tinh == 'Q' or phep_tinh == 'q':
        print('\nCảm ơn bạn đã sử dụng CALCULATOR này !')
        break
    
    else:
        result = result + phep_tinh
        if ('/0' in phep_tinh) or ('%0' in phep_tinh):
            print(f'kết quả: {result} = NaN')
            print('\n' + '\033[91m' + 'ZeroDivisionError:' + '\033[0m' + 'integer division or modulo by zero')
            print(result.replace('/0', '\033[91m'+'/0'+'\033[0m').replace('%0', '\033[91m'+'%0'+'\033[0m'))
            print('\nHãy tính lại từ đầu\n\n')
    
            result = ''
            continue

        else:
            print(f"kết quả: {result} = {eval(result)}")    
            result = str(eval(result))