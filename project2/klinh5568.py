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