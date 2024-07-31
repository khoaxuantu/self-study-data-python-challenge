
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ValueError("Phép chia cho số 0 không được thực hiện.")
     
def main():
    print("Chào mừng đến với Máy tính Python!")
    print("Bạn có thể sử dụng các phép toán sau: +, -, *, /, %")
    print("Bạn cũng có thể sử dụng dấu ngoặc để nhóm.")
    print("Ví dụ: (2 + 3) * 4")
    
    while True:
        expression = input("Nhập phép tính của bạn (hoặc 'quit' để thoát): ").strip()
        if expression.lower() == 'quit':
            print("Goodbye!")
            break
        result = calculate(expression)
        print(f"Kết quả: {result}")
        
        while True:
            continue_calc = input("Bạn có muốn tiếp tục với kết quả này không? (y/n): ").strip().lower()
            if continue_calc == 'y':
                next_expression = input("Nhập phép tính tiếp theo: ").strip()
                expression = next_expression.replace('result', str(result))
                result = calculate(expression)
                print(f"Kết quả: {result}")
            elif continue_calc == 'n':
                break
            else:
                print("Đầu vào không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")

if __name__ == "__main__":
    main()
