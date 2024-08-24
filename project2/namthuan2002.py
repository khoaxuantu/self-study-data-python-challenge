expression = input("Enter your calculation: ")
try:
    print("Result:", eval(expression))
except:
    raise Exception("Something went wrong with your input!")


#We know that eval() is a strong function and can do mostly of our requirement but it does not mean you can code 5 lines and submit it as a project.
#You didn't handle validating your inputs or other cases like Division by 0. So we decide to minus you 1 point for this.
#Keep it up next time!