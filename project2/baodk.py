class Operator:
  def __init__(self, name, apply_func=None, precedence=0):
    self.name = name
    self.apply = apply_func
    self.precedence = precedence

class Calculator:
  # Declare the functions for all allowed operators
  operators = {"+": Operator("+", lambda a,b: a + b, 1)
              ,"-": Operator("-", lambda a,b: a - b, 1)
              ,"x": Operator("x", lambda a,b: a * b, 2)
              ,"/": Operator("/", lambda a,b: a / b, 2)
              ,"%": Operator("%", lambda a,b: a % b, 3)}
  
  def __init__(self):
    pass

  def get_operator(self, op):
    """
    The function return operator object.
    """
    return self.operators.get(op)

  def is_operator(self, op):
    """
    The function returns op string is an operator or not.
    """
    return self.get_operator(op) is not None

  def evaluate(self, expression):
    """
    This is the core function that evaluates a mathematical expression given as a string.
    """
    i, stack = 0, []
    expression = expression.lower()
    while i<len(expression):
      # handling space characters
      if expression[i]==' ':
        i += 1
        continue
      # handling group open by recursive and multiply op
      elif expression[i]=='(':
        val, j = self.evaluate(expression[i+1:])
        op = self.get_operator('x')
        if isinstance(stack[-1], Operator):
          op = stack.pop()
        stack.append(op.apply(stack.pop(), val))
        i += j
      # handling digits
      elif expression[i].isdigit() or expression[i] == '.':
        start = i
        decimalCount = 0
        # handling decimal points in number string
        while (i<len(expression) and 
          (expression[i].isdigit() or expression[i] == '.' or expression[i] == ' ')):
          if expression[i] == '.':
            decimalCount += 1 
          if decimalCount > 1:
            raise SyntaxError('Invalid input: more than one decimal point in number string!')
          i+=1
        # handling space inside number string
        numStr = expression[start:i]
        if ' ' in numStr.strip():
          raise SyntaxError('Invalid input: space found within number string!')
        # add number into stack
        val = float(numStr)
        if len(stack)==0:
          stack.append(val)
        elif isinstance(stack[-1], Operator):
          op = stack.pop()
          stack.append(op.apply(stack.pop(), val))
        # handling number with number without operator
        else:
          raise SyntaxError('Invalid input: number following group without operator!')
        i-=1
      # handling closing group
      elif expression[i]==')':
        return stack[-1], i+1
      # check & add operator into stack
      elif self.is_operator(expression[i]):
        op = self.get_operator(expression[i])
        stack.append(op)
      # unspecified character
      else:
        raise SyntaxError(f"Invalid input: '{expression[i]}' is invalid input expression!")
      i+=1
    

    return stack[-1]

  def has_one_operator(self, expression):
    """
    This function check whether has allowed operator in expression.
    """
    if len(expression)==0:
      return False
    ops = self.operators.keys()
    for op in ops:
      if op in expression:
        return True
    return False

  def has_continue_operator(self, expression):
    """
    This function check whether next string is allowed operator.
    """
    if expression[0] not in self.operators.keys():
      return False
    return True

  def start(self):
    """
    examples for input expression:
    - "eg1: 1(2x4)5 = [!]Invalid input: number following group without operator!"
    - "eg2: 11+(99x(89+1)/2) = 4466"
    """
    result = ""
    while True:
      evalText = input(f'[i]Enter expression for calculator: {result}').strip()
      if not self.has_one_operator(evalText):
        print('[!]Invalid expression: No operator found in expression!')
      elif not isinstance(result, str) and not self.has_continue_operator(evalText):
        print('[!]Invalid expression: No operator for continue expression!')
      else:
        evalText = f"{result}{evalText}"
        try:
          result = self.evaluate(evalText)
          result = int(result) if int(result) == result else result
          print(f'[o]Result: {evalText} = {result}')
        except Exception as e:
          print(f"[!]{e}")
      if input('[?]Do you wish to continue calculate base on the current result? [y(es)/n(o)]: ').strip().lower() not in ('yes', 'y'):
        break

  def welcome(self):
    """
    This function is used to display a list of menu items of basic calculator.
    """
    calculatorName = 'Basic calculator - Self study data - group#74'
    menuItems = ["Allowed operators: ['+', '-', 'x', '/', '%' (modulo)]"
                ,"Also allowed group operations input: '(',')'"
                ,"Allowed enter expression for calculator input (eg: '11+12/3' ..)"
                ,"Allowed break expression for calculation (e.g., A + B = AB, AB + C = ABC)"]
    menuWidth = max([len(menuItem) for menuItem in menuItems])
    # print(calculatorName)
    print("{:^{width}}".format('*', width=menuWidth+5).replace(' ', '='))
    print("   {:<{width}}".format(calculatorName, width=menuWidth+2))
    print("{:^{width}}".format('Notes', width=menuWidth+5).replace(' ', '='))
    for it, menuItem in enumerate(menuItems):
      print(" {:02d}. {:<{width}}".format(it+1, menuItem, width=menuWidth))
    print("{:^{width}}".format('*', width=menuWidth+5).replace(' ', '='))
    self.start()

if __name__ == '__main__':
  Calculator().welcome()