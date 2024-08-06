import os

def calculator_menu(name: str):
    print(f"Welcome {name} to the calculator!!!")
    print("Please choose the function using as described below:")
    print("1. Enter 'A' for Addition.")
    print("2. Enter 'S' for Substraction.")
    print("3. Enter 'M' for Mulitplication.")
    print("4. Enter 'D' for Division.")
    print("5. Enter 'O' for Modulo.")

def handle_operation(choice: str, val1: float, val2: float):
    if choice == 'A':
        return val1 + val2, "+"
    elif choice == 'S':
        return val1 - val2, "-"
    elif choice == 'M':
        return val1 * val2, "*"
    elif choice == 'D':
        return val1 / val2, "/"
    elif choice == 'O':
        return val1 % val2, "%"
    
def get_user_input():
    val_input = input("Please enter your choice (A, S, M, D, O): ")
    first_num = float(input("Please enter the 1st number: "))
    second_num = float(input("Please enter the 2nd number: "))
    return val_input, first_num, second_num

if __name__ == "__main__":
    username = os.getlogin()
    calculator_menu(name=username)
    val_input, first_num, second_num = get_user_input()
    result, sign = handle_operation(choice=val_input, val1=first_num, val2=second_num)
    print(f"Result: {first_num} {sign} {second_num} = {result}")