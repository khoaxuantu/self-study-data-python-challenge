print("Enter 'A' for addition")
print("Enter 'S' for subtraction")
print("Enter 'M' for multiplication")
print("Enter 'D' for division")
print("Enter '%' for modulo")
print("Enter 'end' for end of the calculation")

print()

array = ''
choice_1 = input('Enter first choice (A,S,M,D,%): ')
if choice_1.lower() in ['a','s','m','d','%']:
    first_number = input('Enter first number: ')
    second_number = input('Enter second number: ')
    array = array + first_number + choice_1.lower() + second_number
    answer = input('Do you want more calculation? Yes/No ')
    if answer.lower() in ['yes','ye']:
        next_choice = input("Enter another choice (A,S,M,D,%,end): ")
        
        while next_choice.lower() != 'end':
            if next_choice.lower() not in ['a','s','m','d','%']:
                print()
                print('The previous syntax is not true.')
                break
            else:
                array = array + next_choice.lower()
                next_number = input('Enter next number: ')
                array = array + next_number
                next_choice = input("Enter another choice (A,S,M,D,%,end): ")              
    else: pass 
    array = array.replace('a','+').replace('s','-').replace('m','*').replace('d','/')

    print()

    print('The result is: ', array, '=', eval(array))
    
else: 
    print()
    print('The syntax is not true.')  
    
