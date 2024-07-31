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
