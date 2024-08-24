#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(numbers):
    for a in range(len(numbers)):
        if a == 0:
            print(f"The result: {numbers[a]}", end="")
        elif a < len(numbers) - 1:
            print(f" + {numbers[a]}", end="")
        elif a == len(numbers) - 1:
            print(f" + {numbers[a]} =", end=" ")
    result = sum(numbers)
    print(result)
def subtraction(numbers):
    for a in range(len(numbers)):
        if a == 0:
            print(f"The result: {numbers[a]}", end="")
        elif a < len(numbers) - 1:
            print(f" - {numbers[a]}", end="")
        elif a == len(numbers) - 1:
            print(f" - {numbers[a]} =", end=" ")
    result=numbers[0]
    for num in numbers[1:]:
        result-=num
    print(result)
def multiplication(numbers):
    for a in range(len(numbers)):
        if a == 0:
            print(f"The result: {numbers[a]}", end="")
        elif a < len(numbers) - 1:
            print(f" * {numbers[a]}", end="")
        elif a == len(numbers) - 1:
            print(f" * {numbers[a]} =", end=" ")
    result=1
    for num in numbers:
        result*=num
    print(result)
def division(numbers):
    for a in range(len(numbers)):
        if a == 0:
            print(f"The result: {numbers[a]}", end="")
        elif a < len(numbers) - 1:
            print(f" / {numbers[a]}", end="")
        elif a == len(numbers) - 1:
            print(f" / {numbers[a]} =", end=" ")
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            return "Division by zero"
        result/=num
    print(result)
def modulo(numbers):
    for a in range(len(numbers)):
        if a == 0:
            print(f"The result: {numbers[a]}", end="")
        elif a < len(numbers) - 1:
            print(f" % {numbers[a]}", end="")
        elif a == len(numbers) - 1:
            print(f" % {numbers[a]} =", end=" ")
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            return "Division by zero"
        result%=num
    print(result)
def input_number():
    while True:
        try:
            count = int(input("Enter the number of variables you want: "))
            if count <= 0:
                print("The number must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("The value is invalid. Please input an integer.")
    numbers = []
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter the {i + 1}th number: "))
                numbers.append(num)
                break
            except ValueError:
                print("The value is invalid. Please input a number.")
    return numbers
def calculation():
    print("Enter 'A' for Addition.\nEnter 'S' for Subtraction.\nEnter 'M' for Multiplication.\nEnter 'D' for Division.\nEnter 'Mo' for Modulo\n Enter 'Q' for Quit ")
    while True:
        operation=input("Enter Choice (A,S,M,D,L,G): ").upper()
        if operation in ('A','S','M','D','L','Q'): 
            numbers1=input_number()
            if operation=='A':
                return add(numbers1)
            elif operation=='S':
                return subtraction(numbers1)
            elif operation =='M':
                return multiplication(numbers1)
            elif operation =='D':
                return division(numbers1)
            elif operation =='L':
                return modulo(numbers1) 
            elif operation =='Q':
                break
        else:
            print("Invalid operation. Please try again")
        
        next_calculation = input("Do you want to perform another calculation? (Y/N): ").upper()
        if next_calculation != 'Y':
            print("Exiting the calculator. Goodbye!")
            break
calculation()

#Gud job! But the 3rd requirement requires you to do more than 2 pairs of numbers with different operations. E.g: 5+2-8
#Besides, I think your guide about modulo operation is not totally consistent, you mention 'Mo' but user have to type 'L' for the function to work
#Keep it up!