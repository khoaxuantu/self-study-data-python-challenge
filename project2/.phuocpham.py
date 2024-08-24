def ultimate_eval(args):
    args = args.split(',')
    for arg in args:
        print(eval(arg))

calculations = input("Enter your calculation: ")
ultimate_eval(calculations)

#Using eval directly on user input is very risky as it can execute arbitrary code.
#Implement error handling to manage invalid inputs, division by zero, and other potential issues.
#Try to implement grouping of operations and continuous calculations for a more robust calculator.