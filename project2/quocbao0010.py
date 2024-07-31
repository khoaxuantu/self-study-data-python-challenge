def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return x ** 0.5

def cube_root(x):
    return x ** (1/3)

def percentage(x, y):
    return (x / y) * 100

print("Chọn phép toán:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")
print("5. Căn bậc 2")
print("6. Căn bậc 3")
print("7. Tính phần trăm")

choice = input("Nhập lựa chọn (1/2/3/4/5/6/7): ")

if choice in ('1', '2', '3', '4', '5', '6', '7'):
    num1 = float(input("Nhập số thứ nhất: "))
    if choice != '5' and choice != '6':
        num2 = float(input("Nhập số thứ hai: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"Căn bậc 2 của {num1} = {square_root(num1)}")
    elif choice == '6':
        print(f"Căn bậc 3 của {num1} = {cube_root(num1)}")
    elif choice == '7':
        print(f"{num1} là {percentage(num1, num2)}% của {num2}")
else:
    print("Lựa chọn không hợp lệ.")
