start_calulation = 1
count = 0
while start_calulation == 1:
    if count == 0:
        first_number = int(input("Enter the first number: "))
    else:
        first_number = result
    operation = input("Enter the operation:")
    if count == 0:
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the next number: "))
    
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number
    elif operation == '%':
        result = first_number % second_number
    else:
        raise ValueError(f"'{operation}' is not a valid operation. Please enter a valid operation")
    print(f"{first_number} {operation} {second_number} = {result}")
    start_calulation = int(input("Do you want to continue? (1 for yes, 0 for no)"))
    count += 1
print("Thank you for using the calculator")

#Gud job on completing the project! You are not far from completing the 4th and 5th requirements, feel free to ask us or take a look to others' projects for ideas.
#Keep it up!