Calculate = input("Enter the expression: ") #Example input: 5, 1-2, (4%2),...
Expression = Calculate
try:
    result = eval(Calculate)
    while True:
        i = input("Press 'Y' to continue calculating the expression or any button to quit ")
        if i == 'Y':
            Expression = '(' + Expression + ')'
            Calculate_next = input("Enter the next expression: ") #Example input: *5+2, +(3/4), %3,...
            result = eval(str(result) + Calculate_next) 
            Expression += Calculate_next 
        else:
            break
    print("Result: {} = {}".format(Expression, result))
except:
    print("Error Expression!")

#Good job!
#However, beware of validiating input values. Eg: input value is string would crash the code
# also division by zero case was not included.