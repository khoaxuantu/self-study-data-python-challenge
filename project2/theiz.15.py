print("Enter 'A' for addition.")
print("Enter 'S' for subtraction.")
print("Enter 'M' for multiplication.")
print("Enter 'D' for division.")
print("Enter 'MOD' for modulo.")

arr = ['A','S','M','D','MOD']
cin = input("Enter choice (A,S,M,D,MOD) :")
num1 = eval(input("Enter first number :"))
num2 = eval(input("Enter second number :"))
def check(cin,num1,num2):
    for x in arr :
        if(cin == 'A'):
            result = num1+num2
            print(f"Result: {num1}+{num2} = {result}")
            return result
        elif(cin == 'S'):
            result = num1-num2
            print(f"Result: {num1}-{num2} = {result}")
            return result
        elif(cin == 'M'):
            result = num1*num2
            print(f"Result: {num1}*{num2} = {result}")
            return result
        elif(cin == 'D'):
            result = num1/num2
            print(f"Result: {num1}/{num2} = {result}")
            return result
        elif(cin == 'MOD'):
            result = num1%num2
            print(f"Result: {num1}%{num2} = {result}")
            return result
result1 = check(cin,num1,num2)
while True :
    con = input("Please choice to continue(Y/N) :")
    if(con == 'Y'):
        num3 = eval(input("Enter number :"))
        cin2 = input("Enter choice (A,S,M,D,MOD) :")
        check(cin2,result1,num3)
    if(con == 'N'):
        print("SEE YOU AGAIN !!!!")
        break