expression = input("Enter your calculation: ")
try:
    print("Result:", eval(expression))
except:
    raise Exception("Something went wrong with your input!")