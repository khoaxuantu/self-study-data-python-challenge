#!/usr/bin/env python
# coding: utf-8

# In[26]:


def addition(arg):
    summation = arg.split('+')
    num_list = [int(i) for i in summation]
    result = num_list[0]
    for arg in range (1, len(num_list)):
        result += num_list[arg]
    return result
def subtraction(arg):
    summation = arg.split('-')
    num_list = [int(i) for i in summation]
    result = num_list[0]
    for arg in range (1, len(num_list)):
        result -= num_list[arg]
    return result
def multiplication(arg):
    summation = arg.split('*')
    num_list = [int(i) for i in summation]
    result = num_list[0]
    for arg in range (1, len(num_list)):
        result *= num_list[arg]
    return result
def division(arg):
    summation = arg.split('/')
    num_list = [int(i) for i in summation]
    result = num_list[0]
    for arg in range (1, len(num_list)):
        result /= num_list[arg]
    return result
def modulo(arg):
    summation = arg.split('%')
    num_list = [int(i) for i in summation]
    result = num_list[0]
    for arg in range (1, len(num_list)):
        result %= num_list[arg]
    return result
print("Enter 'A' for Addition\nEnter 'S' for Subtraction\nEnter 'M' for Multiplication\nEnter 'D' for Division\n'Enter MD' for Modulo\n")
choice = input("Enter Choice (A,S,M,D,MD): ")
expression = input("Enter expression: ")
if(choice == 'A'):
    result = addition(expression)
    print(result)
elif(choice == 'S'):
    result = subtraction(expression)
    print(result)
elif(choice == 'M'):
    result = multiplication(expression)
    print(result)
elif(choice == 'D'):
    result = division(expression)
    print(result)
elif(choice == 'MD'):
    result = modulo(expression)
    print(result)
else:
    print("Please input a valid operator")

#Gud job! But the 3rd requirement requires you to do more than 2 pairs of numbers with different operations. E.g: 5+2-8
#Keep it up!