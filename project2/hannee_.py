
def enter_your_cal():
    print("Enter 'A' for Addition")
    print("Enter 'S' for Subtraction")
    print("Enter 'M' for Multiplication")
    print("Enter 'D' for Division")
    x = input("Enter you choice (A, S, M, D): ")
    return x
cal = enter_your_cal()   

def your_num():
    y = int(input("Enter your first number: "))
    z = int(input("Enter your second number: "))
    if cal == "A" or cal == "a":
        print("Result: " , y, " + ", z, " = ", y+z)
    elif cal == "S" or cal == "s":
        print("Result: " , y, " - ", z, " = ", y-z)
    elif cal == "M" or cal == "m":
        print("Result: " , y, " * ", z, " = ", y*z)
    elif cal == "D" or cal == "d":
        if z != 0:
            print("Result: " , y, " / ", z, " = ", y/z)
        else:
            print("Can not divide by 0")
    else:
        print("Your input is not correct")

your_num()
