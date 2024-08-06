def calculate (*args, operation):
  result = str (args [0] [0])
  for i in range (1, len (*args)):
    result += " " + operation + " " +str (args [0] [i])
  return result 

def ask_input (operation):
  input_list = []
  i = 1
  if operation not in ['%','/']:
    while True:
      user_input = input (f"Enter number {i} (press 'q' to quit): ")
      if user_input.lower() == "q" and i != 1:
        break
      elif user_input.lower() == "q" and i == 1:
        print ("Enter at least 1 number.")
      else:
        try:
          number = float (user_input.strip())
          input_list.append (int (number) if str(number).endswith(".0") else number)
          i += 1
        except:
          print ("Please enter a valid number")
  else: #for modulus and divide should be only 2 nums
    while i <= 2:
      user_input = input (f"Enter number {i} (press 'q' to quit): ")
      if user_input.lower() == "q" and i != 1:
        break
      elif user_input.lower() == "q" and i == 1:
        print ("Enter at least 1 number.")
      else:
        try:
          number = float (user_input.strip())
          input_list.append (number)
          i += 1
        except:
          print ("Please enter a valid number")

  return input_list

def clean_str (string):
  clean_str = ""
  operation_list = ["+", "-", "*", "/", "(",")"]
  string = string.strip()
  for i in string:
    if i != " " and i not in operation_list:
      clean_str += i
    elif i in operation_list:
      clean_str += " " + i + " " 
  return clean_str

def continuous_cal (*args):
  result = str (args [0] [0])
  for i in range (1, len (*args)):
    result +=str (args [0] [i])
  return result 
#MAIN 
while True:
  #ask for type
  while True:
    type_list = ['1','2','3','q']
    print ("Type of Calculator: ")
    print ("\t Press '1' for one-operation.")
    print ("\t Press '2' for various operations.")
    print ("\t Press '3' for continuous calculation.")
    type_ = input ("Enter your type of Calculator (press 'q' to quit): ")
    if type_.lower() not in type_list:
      print ("Please enter valid type of calcuation.")
      print ()
    else:
      print ()
      break
  #stop program
  if type_.lower()== 'q':
    break
  #one-operation calculation
  elif type_ == '1':
    while True:
      operation_list = ["+", '-', "*", "/", "%", "q"]
      print ("Operation list: + - * / % ")
      operation = input ("Enter operation in the list (press 'q' to quit): ")
      if operation.strip() not in operation_list:
        print ("Please enter valid operation( + , - , * , / , % ).")
        print ()
      else:
        break
    user_input_list = ask_input (operation)
    equation = calculate (user_input_list, operation = operation)
    result = eval(equation)
    print ("Result: {0} = {1}\n".format (equation, int(result) if str(result).endswith(".0") else result))
  #various calculaton
  elif type_ == '2':
    while True:
      try:
        user_input = input ("Enter the entire calculation (eg. 1+2*7): ")
        equation = clean_str (user_input)
        result = eval(equation)
        print ("Result: {0} = {1} \n".format (equation, int(result) if str(result).endswith(".0") else result))
        break
      except: 
        print ("Please enter valid value.")
  #continuos calculation
  elif type_ == '3':
    user_input_list = ask_input (operation = '+')
    result = calculate (user_input_list, operation = '+')
    print (f"Result: {result} = {continuous_cal(user_input_list)} \n")
print ("Thank you so much!")