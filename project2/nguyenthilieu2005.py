#addition
def addition(n1,n2):
    return n1+n2

#subtraction
def subtraction(n1,n2):
    return n1-n2

#multiplication
def multiplication(n1,n2):
    return n1*n2

#division
def division(n1,n2):
    return n1/n2

print("Select Operations")
print (
    "Enter 'A' for Addition.\n"\
    "Enter 'S' for Subtraction.\n"\
    "Enter 'M' for Multiplication.\n"\
    "Enter 'D' for Division.\n")
#Choose the operation
operation = str(input("Enter choice (A,S,M,D): "))

#Take input
n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))

if operation == "A":
    print(n1,"+",n2,"=",addition(n1,n2))

elif operation == "S":
    print(n1,"-",n2,"=", subtraction(n1,n2))

elif operation == "M":
    print(n1,"*",n2,"=", multiplication(n1,n2))

elif operation == "D":
    print(n1,"/",n2,"=", division(n1,n2))

else:
    print("Invalid Input")