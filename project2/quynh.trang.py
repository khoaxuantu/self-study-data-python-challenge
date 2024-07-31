print("Enter the entire calculation on one line and press enter to see the result.")
print("If you want to continue with the previous result, you will need to start with operators.")

# Generate result variable
result = None

while True:
    
    # Take input from users

    if result is not None:
        cal1 = input(f"Enter your calculation using the previous result ({result}): ")
    else:
        cal1 = input("Enter your calculation: ")

    if result is not None:
        cal1 = str(result) + cal1  # Append the result to the calculation expression

    try:
        result = eval(cal1)
        print(f"{cal1} = {result}")
    except Exception as e:
        print("Invalid input. Please try again.")
        continue

    continue_cal = input("Do you want to continue with the result? (Y/N): ")
    if continue_cal.lower() == "y":
        continue

    elif continue_cal.lower() == "n":
        next_calculation = input("Let's do next calculation? (Y/N): ")
        if next_calculation.lower() == "n":
            break
        elif next_calculation.lower() == "y":
            result = None
            continue
        else:
            print("Invalid input, Please try again!")
    else:
            print("Invalid input, Please try again!")
