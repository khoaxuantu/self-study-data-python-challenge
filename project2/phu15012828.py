def Calculator():
    calculate = True
    result = None
    print("Welcome to the calculator!")
    print("You can enter operations like +, -, *, /, or %.")
    print("You can also input numbers in pairs, e.g., aa + bb + cc, and group them together, e.g., (A+b) x c.")
    print("The previous result can be used in the next calculation.")

    while calculate:
        try:
            if result == None:
                expression = input("Enter your calculation:")
    
            else:
                print("You can refer previous result as 'ans' ")
                expression = input(f"Enter your calculation: ")
                expression = expression.replace('ans',str(result))

            result = eval(expression)
            print("Result:",result)

            continue_calculation = input("Do you want to enter another expression? (Y/N): ").strip().upper()
            if continue_calculation != "Y":
                calculate = False
        except :
            print("Error: Please enter a valid expression.")

Calculator()

#Looks like you nailed this project! Keep up the good works!!

