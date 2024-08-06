def ultimate_eval(args):
    args = args.split(',')
    for arg in args:
        print(eval(arg))

calculations = input("Enter your calculation: ")
ultimate_eval(calculations)