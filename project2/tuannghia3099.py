def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def divi(a,b):
    return a / b
def modu(a,b):
    return a % b

print("Enter '+' for Addition.")
print("Enter '-' for Subtraction.")
print("Enter '*' for Multiplication.")
print("Enter '/' for Division.")
print("Enter '%' for Modulo.")

lst = ['first','second','third']
list_num = []

i = 0
while i < 3:
    num = int(input('Enter ' + str(lst[i]) + ' number: '))
    list_num.append(num)
    if i == 1:
        a = input("Press '=' to see the result or 'C' to continue: ")
        if a == '=':
            if choice1 == '+':
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), '=', add(list_num[0],list_num[1]))
                break
            elif choice1 == '-':
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), '=', sub(list_num[0],list_num[1]))
                break
            elif choice1 == '*':
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), '=', multi(list_num[0],list_num[1]))
                break
            elif choice1 == '/':
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), '=', divi(list_num[0],list_num[1]))
                break
            else:
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), '=', modu(list_num[0],list_num[1]))
                break
        else:
            choice2 = input('Enter Choice (+,-,*,/,%): ')
            i += 1
            num = int(input('Enter ' + str(lst[i]) + ' number: '))
            list_num.append(num)
            if choice2 == '+':
                if choice1 == '+':
                    value1 = add(list_num[0],list_num[1])
                elif choice1 == '-':
                    value1 = sub(list_num[0],list_num[1])
                elif choice1 == '*':
                    value1 = multi(list_num[0],list_num[1])
                elif choice1 == '/':
                    value1 = divi(list_num[0],list_num[1])
                else:
                    value1 = modu(list_num[0],list_num[1])
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      add(value1,list_num[2]))
                break
            elif choice2 == '-':
                if choice1 == '+':
                    value1 = add(list_num[0],list_num[1])
                elif choice1 == '-':
                    value1 = sub(list_num[0],list_num[1])
                elif choice1 == '*':
                    value1 = multi(list_num[0],list_num[1])
                elif choice1 == '/':
                    value1 = divi(list_num[0],list_num[1])
                else:
                    value1 = modu(list_num[0],list_num[1])
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      sub(value1,list_num[2]))
                break
            elif choice2 == '*':
                if choice1 == '+':
                    value1 = multi(list_num[1],list_num[2])
                    print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      add(list_num[0],value1))
                    break
                elif choice1 == '-':
                    value1 = multi(list_num[1],list_num[2])
                    print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      sub(list_num[0],value1))
                    break
                elif choice1 == '*':
                    value1 = multi(list_num[0],list_num[1])
                elif choice1 == '/':
                    value1 = divi(list_num[0],list_num[1])
                else:
                    value1 = modu(list_num[0],list_num[1])
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      multi(value1,list_num[2]))
                break
            elif choice2 == '/':
                if choice1 == '+':
                    value1 = divi(list_num[1],list_num[2])
                    print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      add(list_num[0],value1))
                    break
                elif choice1 == '-':
                    value1 = divi(list_num[1],list_num[2])
                    print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      sub(list_num[0],value1))
                    break
                elif choice1 == '*':
                    value1 = multi(list_num[0],list_num[1])
                elif choice1 == '/':
                    value1 = divi(list_num[0],list_num[1])
                else:
                    value1 = modu(list_num[0],list_num[1])
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      divi(value1,list_num[2]))
                break
            else:
                if choice1 == '+':
                    value1 = modu(list_num[1],list_num[2])
                    print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      add(list_num[0],value1))
                    break
                elif choice1 == '-':
                    value1 = modu(list_num[1],list_num[2])
                    print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      sub(list_num[0],value1))
                    break
                elif choice1 == '*':
                    value1 = multi(list_num[0],list_num[1])
                elif choice1 == '/':
                    value1 = divi(list_num[0],list_num[1])
                else:
                    value1 = modu(list_num[0],list_num[1])
                print('Result: ', str(list_num[0]), str(choice1), str(list_num[1]), str(choice2), str(list_num[2]), '=',
                      modu(value1,list_num[2]))
                break
    choice1 = input('Enter Choice (+,-,*,/,%): ')
    i += 1
#Good job!
#Eval() is allowed, I recommend looking through it!