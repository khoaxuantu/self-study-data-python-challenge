def calculator():
    while True:
        print("Chọn phép toán:")
        print("  A: Cộng")
        print("  S: Trừ")
        print("  M: Nhân")
        print("  D: Chia")
        print("  %: Modulo")
        print("  Q: Thoát")
        choice = input("Nhập lựa chọn (A, S, M, D, %, Q): ").upper()
        if choice == 'Q':
            break
        numbers = []
        while True:
            num = input("Nhập số (hoặc để trống để kết thúc): ")
            if not num:
                break
            numbers.append(float(num))
        if not numbers:
            print("Bạn chưa nhập số nào!")
            continue
        result = numbers[0]
        for i in range(1, len(numbers)):
            if choice == 'A':
                result += numbers[i]
            elif choice == 'S':
                result -= numbers[i]
            elif choice == 'M':
                result *= numbers[i]
            elif choice == 'D':
                if numbers[i] == 0:
                    print("Không thể chia cho 0!")
                    break
                result /= numbers[i]
            elif choice == '%':
                if len(numbers) != 2:
                    print("Phép tính phần trăm cần đúng 2 số!")
                    break
                part, whole = numbers
                result = (part / whole) * 100
        print("Kết quả:", result)
if __name__ == "__main__":
    calculator()
#Nice work!
#Python built-in function is allowed, I recommend looking through it!
#The 3rd bonus point requires the operations can be different!