# duongng_19_project2
# calculate 3 values
print("Welcome")
print(
"""
You can calculate up to 3 number with the following operator:
Addition: 1
Subtract: 2
Multiply: 3
Divide: 4
Module: 5
Exponential: 6
"""
)
# Create the function to calculate 2 number
def calculate(num1,num2,op):
    if op == '1':
        result = num1+num2
    elif op == '2':
        result = num1-num2
    elif op == '3':
        result =  num1*num2
    elif op == '4':
        result = num1/num2
    elif op=='5':
        result =  num1%num2
    elif op=='6':
        result =  num1**num2
    return result

# Create dictionary to print
op_dict = {'1': "+", '2':"-", '3':"*", '4':"/", '5':"%", '6':"^"}

# Calculation
continue_cal = True

while continue_cal == True:
    op = input("Enter your operator (1 to 7): ")
    if op in ['1','2','3','4','5','6']:
        try:
            num1 = float(input('Enter your first number: '))
        except ValueError: 
            print("Please enter number only")
            num1 = float(input('Enter your first number: '))
            num2 = float(input('Enter your second number: '))
        else:
            num2 = float(input('Enter your second number: '))
            print(f"""
            Your first number: {num1}
            Your second number: {num2}
            Your operator : {op_dict[op]}"""
            )
            result=calculate(num1,num2,op)
            print(f"Your calculation: {num1} {op_dict[op]} {num2}={result}")
            asking_3rd_num = input('Continue calculate 3rd number? (y/n): ').lower()
            if asking_3rd_num == "y":
                num3 = float(input('Enter your third number: '))
                op2 = input("Enter your operator (1 to 7): ")
                print(f"""
            Your next number: {num3}
            Your operator : {op_dict[op2]}"""
            )
                result2 = calculate(result,num3,op2)
                print(f"Your calculation: {num1} {op_dict[op]} {num2} {op_dict[op2]} {num3}={result2}")
                asking_continue_cal = input('Continue calculate new calculation? (y/n): ').lower()
                if asking_continue_cal == "y":
                    continue_cal = True
                else: 
                    continue_cal = False
            else: 
                continue_cal = False
    else: 
        print("Please re-enter the operator code form 1 to 7 only!")

#I think your statement from 1 to 7 is not really easy to understand, I think it should be from 1 to 6
#Overall, good job but I think you are misunderstanding a bit about the requirements.
#The 3rd requirement need you to calculate 3 numbers with any different operations. For example: 2 + 4 * 6
#The 5th requires you to continue calculating based on the result you already have. That means you can continue calculate till you want to stop. Not only 3
#Keep up the good work!


