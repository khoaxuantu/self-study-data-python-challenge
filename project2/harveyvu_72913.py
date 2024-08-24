# Math Logic
def cong(x,y):
    return x+y
def cong1(x,y,z):
    return x+y+z
def cong2(x,y,z):
    return x+y-z
def cong3(x,y,z):
    return (x+y)*z
def cong4(x,y,z):
    return (x+y)/z
def tru(x,y):
    return x-y
def tru1(x,y,z):
    return x-y+z
def tru2(x,y,z):
    return x-y-z
def tru3(x,y,z):
    return (x-y)*z
def tru4(x,y,z):
    return (x-y)/z
def nhan(x,y):
    return x*y
def nhan1(x,y,z):
    return x*y+z
def nhan2(x,y,z):
    return x*y-z
def nhan3(x,y,z):
    return x*y*z
def nhan4(x,y,z):
    return x*y/z
def chia(x,y):
    return x/y
def chia1(x,y,z):
    return x/y+z
def chia2(x,y,z):
    return x/y-z
def chia3(x,y,z):
    return x/y*z
def chia4(x,y,z):
    return x/y/z
def phantram(x,y):
    return x*(y/100)
# Chia chức năng tính calculator
input_type = input('Chọn chức năng tính (Tính 2 biến, Tính 3 biến, Tính %): ')
if input_type.lower() in ('tính 2 biến','tinh 2 bien','2','2 bien','2 biến',
                          '2bien','2b','hai bien','haibien','hai biến'):
# Loop
    while True:
        input1 = input('Nhập phép tính cần tính (Cộng/Trừ/Nhân/Chia): ')

        if input1.lower() in ('cộng','trừ','nhân','chia','cong','tru','nhan',
                              'c','tr','nh','ch','+','-','x','*','/'):
            num1 = float(input('Nhập số thứ nhất: '))
            num2 = float(input('Nhập số thứ hai: '))

            if input1.lower() in ('cộng','cong','c','+'):
                print('Kết quả: ',num1,' + ',num2,' = ',cong(num1,num2))
            elif input1.lower() in ('trừ','tru','tr','-'):
                print('Kết quả: ',num1,' - ',num2,' = ',tru(num1,num2))
            elif input1.lower() in ('nhân','nhan','nh','x','*'):
                print('Kết quả: ',num1,' x ',num2,' = ',nhan(num1,num2))
            elif input1.lower() in ('chia','ch','/'):
                print('Kết quả: ',num1,' / ',num2,' = ',chia(num1,num2))

        else:
            print('Bạn đã nhập sai, hãy nhập phép tính cần tính!')

        next_one = input('Bạn có muốn tiếp tục tính toán không? (Có/Không): ')
        if next_one.lower() in ('không','khong','kh','k','ko',):
            break
elif input_type.lower() in ('tính 3 biến','tinh 3 bien','3','3 bien','3 biến'
                            ,'3bien','3b','ba bien','babien','ba biến'):
# Loop phép tính nhiều 3 biến
    while True:
        input1 = input('Nhập phép tính cho hai số đầu (Cộng/Trừ/Nhân/Chia): ')

        if input1.lower() in ('cộng', 'trừ', 'nhân', 'chia', 'cong', 'tru', 'nhan', 'c', 'tr',
                              'nh', 'ch', '+', '-', 'x', '*', '/'):
            num1 = float(input('Nhập số thứ nhất: '))
            num2 = float(input('Nhập số thứ hai: '))
            num3 = float(input('Nhập trước số thứ ba: '))

            if input1.lower() in ('cộng', 'cong', 'c', '+'):
                input_cong = input('Nhập phép tính tiếp theo (Cộng/Trừ/Nhân/Chia): ')
                if input_cong.lower() in ('cộng', 'cong', 'c', '+'):
                    print('Kết quả: ', num1, ' + ', num2, ' + ', num3, ' = ', cong1(num1, num2, num3))
                elif input_cong.lower() in ('trừ', 'tru', 'tr', '-'):
                    print('Kết quả: ', num1, ' + ', num2, ' - ', num3, ' = ', cong2(num1, num2, num3))
                elif input_cong.lower() in ('nhân', 'nhan', 'nh', 'x', '*'):
                    print('Kết quả: (', num1, ' + ', num2, ') x ', num3, ' = ', cong3(num1, num2, num3))
                elif input_cong.lower() in ('chia', 'ch', '/'):
                    print('Kết quả: (', num1, ' + ', num2, ') / ', num3, ' = ', cong4(num1, num2, num3))
                else:
                    print('Bạn đã nhập sai, vui lòng nhập giá trị đúng!')
            elif input1.lower() in ('trừ', 'tru', 'tr', '-'):
                input_tru = input('Nhập phép tính tiếp theo (Cộng/Trừ/Nhân/Chia): ')
                if input_tru.lower() in ('cộng', 'cong', 'c', '+'):
                    print('Kết quả: ', num1, ' - ', num2, ' + ', num3, ' = ', tru1(num1, num2, num3))
                elif input_tru.lower() in ('trừ', 'tru', 'tr', '-'):
                    print('Kết quả: ', num1, ' - ', num2, ' - ', num3, ' = ', tru2(num1, num2, num3))
                elif input_tru.lower() in ('nhân', 'nhan', 'nh', 'x', '*'):
                    print('Kết quả: (', num1, ' - ', num2, ') x ', num3, ' = ', tru3(num1, num2, num3))
                elif input_tru.lower() in ('chia', 'ch', '/'):
                    print('Kết quả: (', num1, ' - ', num2, ') / ', num3, ' = ', tru4(num1, num2, num3))
                else:
                    print('Bạn đã nhập sai, vui lòng nhập giá trị đúng!')
            elif input1.lower() in ('nhân', 'nhan', 'nh', 'x', '*'):
                input_nhan = input('Nhập phép tính tiếp theo (Cộng/Trừ/Nhân/Chia): ')
                if input_nhan.lower() in ('cộng', 'cong', 'c', '+'):
                    print('Kết quả: ', num1, ' x ', num2, ' + ', num3, ' = ', nhan1(num1, num2, num3))
                elif input_nhan.lower() in ('trừ', 'tru', 'tr', '-'):
                    print('Kết quả: ', num1, ' x ', num2, ' - ', num3, ' = ', nhan2(num1, num2, num3))
                elif input_nhan.lower() in ('nhân', 'nhan', 'nh', 'x', '*'):
                    print('Kết quả: ', num1, ' x ', num2, ' x ', num3, ' = ', nhan3(num1, num2, num3))
                elif input_nhan.lower() in ('chia', 'ch', '/'):
                    print('Kết quả: ', num1, ' x ', num2, ' / ', num3, ' = ', nhan4(num1, num2, num3))
                else:
                    print('Bạn đã nhập sai, vui lòng nhập giá trị đúng!')
            elif input1.lower() in ('chia', 'ch', '/'):
                input_chia = input('Nhập phép tính tiếp theo (Cộng/Trừ/Nhân/Chia): ')
                if input_chia.lower() in ('cộng', 'cong', 'c', '+'):
                    print('Kết quả: ', num1, ' / ', num2, ' + ', num3, ' = ', chia1(num1, num2, num3))
                elif input_chia.lower() in ('trừ', 'tru', 'tr', '-'):
                    print('Kết quả: ', num1, ' / ', num2, ' - ', num3, ' = ', chia2(num1, num2, num3))
                elif input_chia.lower() in ('nhân', 'nhan', 'nh', 'x', '*'):
                    print('Kết quả: ', num1, ' / ', num2, ' x ', num3, ' = ', chia3(num1, num2, num3))
                elif input_chia.lower() in ('chia', 'ch', '/'):
                    print('Kết quả: ', num1, ' / ', num2, ' / ', num3, ' = ', chia4(num1, num2, num3))
                else:
                    print('Bạn đã nhập sai, vui lòng nhập giá trị đúng!')

        else:
            print('Bạn đã nhập sai, hãy nhập phép tính cần tính!')

        next_one = input('Bạn có muốn tiếp tục tính toán không? (Có/Không): ')
        if next_one.lower() in ('không', 'khong', 'kh', 'k', 'ko',):
            break
elif input_type.lower() in ('tính %','tinh %','tính phần trăm','tinh phan tram','%','tinh%',
                            'phan tram','phần trăm','tinhphantram','phantram'):
# Loop tính %
    while True:
        num1 = float(input('Nhập số cần tính: '))
        num2 = float(input('Số phần trăm của số đó: '))

        print('Kết quả: ', num2,'% của ',num1,' là: ', phantram(num1,num2))
        next_one = input('Bạn có muốn tiếp tục tính toán không? (Có/Không): ')
        if next_one.lower() in ('không', 'khong', 'kh', 'k', 'ko',):
            break
else:
    print('Bạn đã nhập sai, vui lòng nhập chức năng tính!')

# You did a good work, but too hardcode which makes your code not very good-looking.
# - You just created a calculator that allows an equation with 2 or 3 operands, and this project requires 3 or more than
# - For the modulo, you misunderstood, the modulo returns the remainder of the division, not get percentage.