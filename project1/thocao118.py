while 1==1:
    
    # Lời chào
    print("\n\U0001F4D0 WELCOME TO LENGTH CONVERTER \U0001F4D0\n")
    
    # Bước 1: Tạo danh mục, đối chiếu đơn vị đo
    dict_Length = {'meter':1, 'kilometer':0.001, 'centimeter':100, 'millimeter':1000, 'micrometer':10**6, 'nanometer':10**9 }
    
    
    # Bước 2: Nhập các biến đầu vào
    print('Available units of Length:                                      ') 
    print('meter, kilometer, centimeter, millimeter, micrometer, nanometer ')
    print('_____________________________\n')
    
    unit_in = str(input('Enter starting unit of Length: ')).lower()
    unit_out = str(input('Enter unit of Length to convert to: ')).lower()
    
    while 1==1:
        try:
            value_in = float(input(f'Enter the value to convert in {unit_in}: '))
            break
        except Exception:
            print(f'\n\u26A0 Please provide a valid number!')
    
    
    # Bước 3: Tính toán & đưa ra kết quả
    value_out = value_in * dict_Length[unit_out] / dict_Length[unit_in]
    print(f'\nResult: {value_in} {unit_in} = {value_out} {unit_out}')
    
    # Bước 4: Hỏi user còn muốn chuyển đổi đơn vị tiếp ko ?
    print('_____________________________\n')
    key = str(input('\nDo you want to perform another conversion? (Y/N): '))
    if key == 'N':
        print("Thank you for using this Length Converter! \U0001F33B\n\n\n")
        break
    else: 
        print('\n\n\n')

#Noice! Thanks for making your output beautiful, we love it <3