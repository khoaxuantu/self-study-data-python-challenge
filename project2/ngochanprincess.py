operation = input("Input expression: ")
calculation = operation
result = eval(operation)
try:
    while True:
        choice = input("Enter 'NEXT' to continue or 'END' to finish: ").upper()

        if choice == 'NEXT':
            operation_next = input("Input expresstion_next: ")
            calculation = '(' + calculation + ')'
            result = eval(str(result) + operation_next)
            calculation += operation_next
        else:
            break
    print ("Result: {} = {}".format(calculation, result))
except:
    print ("Error!")

# We know that eval() is a strong function and can do mostly of our requirement but be more careful because you didn't handle validating your input or other cases like Division by 0. 
# We would strictly score people who use the eval function.
# Keep it up next time!