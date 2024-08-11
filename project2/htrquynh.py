# # Requirement 1, 2
# def calculate():
#     print("Enter A for Addition.")
#     print("Enter S for Subtraction.")
#     print("Enter M for Multiplication.")
#     print("Enter D for Division.")
#     print("Enter Mod for Modulo.")
#     Choice = input("Enter choice(A, S, M, D, Mod) : ")
#     First_num = int(input("Enter number: "))
#     Second_num=int(input("Enter number: "))
#     if Choice == 'A':
#         return print(f"Result: {First_num} + {Second_num} = {First_num+Second_num}")  
#     elif Choice =='S':
#          return print(f"Result: {First_num} - {Second_num} = {First_num-Second_num}")
#     elif Choice == 'M':
#         return print(f"Result: {First_num} * {Second_num} = {First_num*Second_num}")
#     elif Choice =='D': 
#          return print(f"Result: {First_num} / {Second_num} = {First_num/Second_num}")
#     else: 
#         return print(f"Result: {First_num} mod {Second_num} = {First_num%Second_num}")

# Requirement 3:
def calculate():
   
    Number_list =[]
    while True:
        number = input ("Enter numbers (ok to finish): ")
        if number =='ok':
            break
        try:
            number=int(number)
            Number_list.append(number)
        except:
            print("Invalid input. Please enter a valid number.")
        
    print("Enter A for Addition.")
    print("Enter S for Subtraction.")
    print("Enter M for Multiplication.")
    print("Enter D for Division.")
    print("Enter Mod for Modulo.")
    Choice = input("Enter choice(A, S, M, D, Mod) : ")
 
    result = Number_list[0]
    for Number in Number_list[1:]:
        if Choice == 'A':
            Cal='Addition'
            result += Number
        elif Choice == 'S':
            Cal='Subtraction'
            result -= Number
        elif Choice == 'M':
            Cal='Multiplication'
            result *= Number
        elif Choice == 'D':
            if Number == 0:
                print("Error: Division by zero.")
                return
            else:
                Cal='Division'
                result /= Number
        elif Choice == 'Mod':
            if Number == 0:
                print("Error: Modulo by zero.")
                return
            else:
                Cal='Modulo'
                result %= Number
        else:
            print("Invalid operation choice.")
            return
    
    print(f"Result {Cal}: {result}")
calculate()

#Good job! But beware that the 3rd requirements requires you to calculate 3 or more numbers with different operation, e.g 3+5-3/2