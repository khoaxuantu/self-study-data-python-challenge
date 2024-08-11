def calculator():
    """
    A calculator that supports basic arithmetic operations.
    """

    print("Available operations:")
    print('"A": Addition')
    print('"S": Subtraction')
    print('"M": Multiplication')
    print('"D": Division')
    print('"%": Modulo')
    print('"PO": Opening parenthesis')
    print('"PC": Closing parenthesis')
    print('"E": End the expression and print out the result')
    
    operations = {
        "A": "+",
        "S": "-",
        "M": "*",
        "D": "/",
        "%": "%",
        "PO": "(",
        "PC": ")"
    }

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def input_validation(expression, current_input):
      if not expression:
        return is_number(current_input)
    
      if is_number(current_input):
        return True
    
      current_input = current_input.upper()
      if current_input in operations:
        if expression and is_number(expression[-1]):
          return True
        elif expression and expression[-1] in operations:
          if current_input != "(":
            print("Invalid input: Operator cannot follow another operator.")
            return False
        return True
    
      if current_input == "(":
        if expression and is_number(expression[-1]):
          return True
        elif expression and expression[-1] == "(":
          print("Invalid input: Opening parenthesis cannot follow opening parenthesis.")
          return False
        return True
    
      if current_input == ")":
        if expression and (is_number(expression[-1]) or expression[-1] == ")"):
          return True
        elif expression and expression[-1] == "(":
          print("Unbalanced parentheses.")
          return False
        else:
          print("Invalid input: Closing parenthesis without opening parenthesis.")
          return False
    
      print("Invalid input.")
      return False


    expression = ""
    previous_result = None
    
    while True:
        input_str = input("Enter number or operator: ")
        if input_str.upper() == "E":
            try:                
                result = eval(expression)
                print(f"Result: {expression} = {result}")
                choice = input("Press C to continue on the previous result, N for new calculation, or any other key to exit: ").upper()
                if choice == "C":
                    previous_result = result
                    expression = ""
                elif choice == "N":
                    previous_result = None
                    expression = ""
                else:
                    break
            except SyntaxError:
                print("Invalid expression.")
            except ZeroDivisionError:
                print("Division by zero.")
                
        else:
            if previous_result and expression == "":
                if input_str.upper() not in ["A", "S", "M", "D", "%"]:
                    print("Next input must be an operator.")
                    continue
                else:
                    expression += str(previous_result)
            elif expression == "":
                if not is_number(input_str) and input_str.upper() != "PO":
                    print("First input must be a number or an opening parenthesis.")
                    continue
            elif not input_validation(expression[-1], input_str):
                continue
              
            expression += input_str if is_number(input_str) else operations[input_str.upper()]

calculator()

#You nailed it! Really like the way you carefully thought about different cases!