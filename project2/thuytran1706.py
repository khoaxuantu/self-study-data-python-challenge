number_1 = input("Enter first number: ")
number_2 = input("Enter second number: ")
addition = int(number_1) + int(number_2)
subtract = int(number_1) - int(number_2)
multi = int(number_1) * int(number_2)
division = int(number_1) / int(number_2)
module = int(number_1) % int(number_2)

def func():
  choice = input("Enter Choice (A,S,M,D): ")
  if choice == "A":
    print("Result: "+ str(addition))
  elif choice == "S":
    print("Result: "+ str(subtract))
  elif choice == "M":
    print("Result: "+ str(multi))
  elif choice == "D":
    print("Result: "+ str(division))
    print("Module: "+str(module))
  else:
    print("wrong operator")

func()