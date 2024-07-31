import re

def is_valid_expression(expression):
  valid_characters = re.compile(r'^[\d+\-*/%().\s]+$')
  # Check for invalid characters
  if not valid_characters.match(expression):
    return False

  # Tokenize the expression
  tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/%()]', expression)
    
  operators = set('+-*/%')
  prev_token = ''
  for token in tokens:
    if token in operators:
      if prev_token in operators:
        return False
    prev_token = token
  return True

def calculate_expression(expression, last_result):
  expression = expression.replace('ans', str(last_result))
  
  if not is_valid_expression(expression):
    return "Error: Invalid expression"
    
  try:
    result = eval(expression)
    return result
  except (ZeroDivisionError) as e:
    return f'Error: {e}'
  except (SyntaxError, NameError, TypeError) as e:
    return f'Error: Invalid expression'

last_result = 0
while True:
  print('---------------')
  print('Supported operators: + - * / %')
  print('Use . for decimal numbers. Use "ans" for the last result')
  expression = input('Enter an expression (or "exit" to quit): ')
  if expression.lower() == 'exit':
    print("Exiting...")
    break

  result = calculate_expression(expression, last_result)
  if isinstance(result, str) and result.startswith("Error"):
    print(result)
  else:
    last_result = result
    print(f"Result: {result}")