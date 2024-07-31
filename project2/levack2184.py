#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate (operation, first_num, second_num, **kwargs):
    if operation == "/":
        division = input("Choose your division - Enter: % for modulus, // for floor division and / for normal division: ")
    if operation == "+":
        result = first_num + second_num
        print("The sum of numbers is:", result)
    elif operation == "-":
        result = first_num - second_num
        print("The difference of numbers is:", result)
    elif operation == "*":
        result = first_num * second_num
        print("The product of numbers is:", result)
    elif division == "%":
        result = first_num % second_num
        print("The modulus of numbers is:", result)
    elif division == "//":
        result = first_num // second_num
        print("The floor division of numbers is: ", result)
    else:
        result = round(first_num / second_num,2)
        print("The division of numbers is: ", result)
    return result 
def continous_calculation():
    operation = input("Enter your operator (+, -, *, /): ").strip()
    first_num = int(input("Enter your first number: "))
    second_num = int(input("Enter your second number: "))
    result = calculate(operation, first_num, second_num)  
    
    while result is not None:
        cont_cal = input("Do you want to continue your calculation? yes or no: ").strip().lower()
        if cont_cal == "no":
            print("Your final result is:", result)
            break
        elif cont_cal == "yes":
            operation = input("Enter your next operator (+, -, *, /): ").strip()
            new_num = int(input("Enter the next number: "))
            result = calculate(operation, result, new_num)
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
    
    if result is None:
        print("Calculation stopped due to an error.")
continous_calculation()


