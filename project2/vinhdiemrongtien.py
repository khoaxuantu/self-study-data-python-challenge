#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Project 2 - Calculator

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, *args):
        self.result = sum(args)
        return "+".join(map(str, args)) + f" = {self.result}"

    def subtract(self, *args):
        self.result = args[0]
        for num in args[1:]:
            self.result -= num
        return "-".join(map(str, args)) + f" = {self.result}"

    def multiply(self, *args):
        self.result = args[0]
        for num in args[1:]:
            self.result *= num
        return "*".join(map(str, args)) + f" = {self.result}"

    def divide(self, *args):
        self.result = args[0]
        for num in args[1:]:
            if num != 0:
                self.result /= num
            else:
                return "Lỗi, không chia được cho 0"
        return "/".join(map(str, args)) + f" = {self.result}"

    def modulo(self, *args):
        self.result = args[0]
        for num in args[1:]:
            self.result %= num
        return "%".join(map(str, args)) + f" = {self.result}"

# Main

if __name__ == "__main__":
    calc = Calculator()
    while True:
        print("Enter 'A' for Addition")
        print("Enter 'S' for Subtraction")
        print("Enter 'M' for Multiplication")
        print("Enter 'D' for Division")
        choice = input("Enter choice (A, S, M, D): ").upper()

        if choice in ['A', 'S', 'M', 'D']:
            try:
                num_inputs = int(input("How many numbers do you want to enter? "))
                numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_inputs)]

                if choice == 'A':
                    print("Result:", calc.add(*numbers))
                elif choice == 'S':
                    print("Result:", calc.subtract(*numbers))
                elif choice == 'M':
                    print("Result:", calc.multiply(*numbers))
                elif choice == 'D':
                    print("Result:", calc.divide(*numbers))
            except ValueError:
                print("Lỗi: Định dạng đầu vào không hợp lệ")
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


# In[ ]:
#Nice work!
#Eval() is allowed, I recommend looking through it!


