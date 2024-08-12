class Operator:
  def __init__(self, sign, apply_func=None, precedence=0):
    self.sign = sign
    self.apply = apply_func
    self.precedence = precedence
  def __str__(self):
    return self.sign
  def __repr__(self):
    return f"Op({self.sign})"

def modulo(a, b):
  if isinstance(b, int):
    return a%b
  if isinstance(b, float):
    if int(b)!=b:
      raise ValueError(f"{b} is not integer")
  return a%int(b)

class Number(float):
  def __str__(self):
    s = f"{self:f}"
    s = s.rstrip('0').rstrip('.')
    return s

class Calculator:
  # Declare the functions for all allowed operators
  operators = {"+": Operator("+", lambda a,b: a + b, 1)
              ,"-": Operator("-", precedence=1)
              ,"x": Operator("x", lambda a,b: a * b, 2)
              ,"/": Operator("/", lambda a,b: a / b, 2)
              ,"%": Operator("%", lambda a,b: a % b, 3)}
  
  def __init__(self):
    pass

  def get_operator(self, sign):
    """The function return operator object."""
    return self.operators.get(sign)

  def is_operator(self, sign):
    """The function returns op string is an operator or not."""
    return bool(sign in self.operators.keys())
  
  def no_minus(self, factors):
    it = 0
    length = len(factors)
    while it<length:
      factor = factors[it]
      if isinstance(factor, Operator):
        if factor.sign == '-' and it<length and isinstance(factors[it+1], Number):
          factors[it+1] = Number(-factors[it+1])
          factors.pop(it)
          length-=1
          if it>0 and not isinstance(factors[it-1], Operator):
            factors.insert(it, self.get_operator('+'))
            length+=1
          continue
        if it==0 and factor.precedence>1:
          raise SyntaxError(f"Invalid input: expression might not starts with '{factor}'!")
      it+=1
    return factors

  def factoring(self, expr):
    """The function is used to parse numbers, operators, opens, closes from an expression."""
    it = 0
    factors = []
    length = len(expr)
    while it<length:
      char=expr[it]
      if char==' ':
        pass
      elif self.is_operator(char):
        factors.append(self.get_operator(char))
      elif char in ('(', ')'):
        factors.append(char)
      elif char.isdigit() or char=='.':
        start=it
        while it<length and (char.isdigit() or char=='.' or char==' '):
          it+=1
          if it<length: char=expr[it]
        numStr = expr[start:it].strip()
        if not numStr.replace('.', '', 1).isnumeric():
          raise SyntaxError(f"Invalid input: '{numStr}' is not a valid number!")
        factors.append(Number(numStr))
        it-=1
      else:
        raise SyntaxError(f"Invalid input: '{expr[it]}' is invalid input expression!")
      it+=1
    return self.no_minus(factors)
  
  def evaluate(self, expression):
    """
    This is the core function that evaluates a mathematical expression given as a string.
    """
    factors = self.factoring(expression.lower())

    def apply_op_from_left(ops, values):
      """This sub-function is used to apply operators from left to right once
      that expression has no higher precedence inside."""
      op = ops.pop(0)
      lVal, _ = values.pop(0)
      rVal, _ = values.pop(0)
      res = Number(op.apply(lVal, rVal))
      print(f"apply: {lVal}{op}{rVal}={res}") # print for debugging
      values.insert(0, (res, _))

    def sub_evaluate(facts, start_prec=1):
      """This sub-function supports grouping and higher precedence operating."""
      values, ops = [], []
      it = 0
      length = len(facts)
      while it<length:
        fact = facts[it]
        # print(f">expr: {' '.join(map(str,facts))}") # debug expr print
        # print(f"[sub]: fact={fact},ops={ops},vals={values},it={it},prec={start_prec}") # debug iterator print
        if isinstance(fact, Number):
          if it>1 and facts[it-1]==')':
            raise SyntaxError(f"Invalid input: number '{fact}' follows group without operator!")
          values.append((fact, it))
        elif isinstance(fact, Operator):
          if fact.precedence>start_prec:
            # start child eval from previous number iterator
            _, idx = values.pop()
            subVal, subLen = sub_evaluate(facts[idx:], start_prec=fact.precedence)
            it += subLen-2
            values.append((subVal, it-1))
          elif start_prec>fact.precedence:
            # break point for higher precedence handling
            break
          else: ops.append(fact)
        elif fact=='(':
          # add 'x' operator if before '(' have no operator
          if it>0 and not isinstance(facts[it-1], Operator):
            facts.insert(it, self.get_operator('x'))
            length+=1
            continue
          # start child eval from iterator + 1
          subVal, subLen = sub_evaluate(facts[it+1:])
          it += subLen+1
          values.append((subVal, it))
        elif fact==')':
          # break point for closing group
          break
        it+=1
        
      # same precedences handling, perform operators from left to right
      while ops:
        apply_op_from_left(ops, values)
      val, _ = values.pop()
      return val, it
    
    result, _ = sub_evaluate(factors)
    return result

  def has_one_operator(self, expression):
    """This function check whether has allowed operator in expression."""
    if len(expression)==0:
      return False
    ops = self.operators.keys()
    for op in ops:
      if op in expression:
        return True
    return False

  def has_continue_operator(self, expression):
    """This function check whether next string is allowed operator."""
    if expression[0] in ('(', ')'):
      return True
    if expression[0] not in self.operators.keys():
      return False
    return True

  def start(self):
    """
    examples for input expression:
    - eg1: 1(2x4)5 = Invalid input: number '5' follows group without operator!
    - eg2: 11+(99x(89+1)/2) = 4466
    - eg3: 14+(1+4%3)-2 = 14
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
          print(f'[o]Result: {evalText} = {result}')
        except Exception as e:
          print(f"[!]{e}",)
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
#Overkill this small project!
#Keep fighting!