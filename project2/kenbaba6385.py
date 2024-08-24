while True:
    a = input("Enter the calculation: ")
    result = eval(a)
    print("Result:", a, "=", result)

    ask = input("Countinue? (Y/N)").upper()
    if ask == "N":
        break

    elif ask == "Y":
        b = result 
        while True:
            a = input("Enter the calculation to continue with the previous result:(EX:-+*%3+2/2...)")
            result = eval(str(b) + a)
            print("Result:", str(b) + a + "=", result)

            ask = input("Countinue? (Y/N)").upper()
            if ask == "N":
                break
            elif ask == "Y":
                continue
        break
#Good job! But beware to validate your inputs, it will be important in any project!