def calculator():
    print ("Enter 'A' for Addition")
    print("Enter 'S' for Subtraction")
    print("Enter 'M' for Multiplication and 'MOD' for modulo")
    print("Enter 'D' for Division")
    print("Enter 'Q' for Quit")
    result = 0
    
    while True:
        choice = input('Enter your choice: ')
        if choice in ['A', 'S', 'M', 'D', 'MOD']:
            expression = input('Enter your expression (A + B + C, (A + B) * C,...): ')
            result = eval(expression)
            print(f"Result: {expression} = {result}")
            if(input("Do you want to continue? (Y/N)") == 'Y'):
                new_expression = input("Add more calculation(*3, -5, %10,...)")
                new_cal = f"({expression}) {new_expression}"
                result = eval(new_cal)
                print(f"Result: {new_cal} = {result}")        
            else:
                break
        else:
            break
            
if __name__ == '__main__':
    calculator()

# Nice work! FYI, because you used `eval()`, we also evaluate your work strictly.

# What is the purpose of the `choice` variable, where you just need to check if the users want to continue or not? And after I enter 'A', and calculate the expression '4 - 2', does it make sense? So when you use eval, you don't need to check the `choice` variable, just check if the user wants to continue or not. Beside that, you can also check the `choice` by upper case so that when the user enters 'a', it still works.

# And you should handle the errors may occur when using `eval()` detailedly. For example, if user mistakenly enters a wrong expression, your program should handle it and return the error message instead of crashing (try `3 5`). This is not enough to handle the errors may occur when using `eval()`, it needs more than that.
