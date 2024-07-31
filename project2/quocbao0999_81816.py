# This code will create a Calculator
    # +: represents addition
    # -: represents substraction
    # *: represents multiplication
    # /: represents division (result will be a QUOTIENT)
    # %: represents division (result will be a REMAINDER)

import re
import pprint

def replace_percentages(expression):
    # Define a function to convert a percentage to its decimal representation
    def percent_to_decimal(match):
        number = float(match.group(1))  # Get the number from the match
        return str(number / 100)  # Convert to decimal and return as string
    
    # Use a regular expression to find all instances of numbers followed by '%'
    modified_expression = re.sub(r'(\d+)%', percent_to_decimal, expression)
    
    return modified_expression



def Calculator(expression):
    # Remove spaces from the expression
    expression = "".join(expression.split())
    # Find the innermost parentheses and evaluate the expression within them
    while '(' in expression:
        start = expression.rfind('(')
        end = expression.find(')', start)
        if start == -1 or end == -1:
            break
        sub_expr = expression[start + 1:end]
        try:
            result = eval(sub_expr)
        except ZeroDivisionError:
            print('Error: Division by zero detected. Please try again!')
            return  # Exit the function on error
        expression = expression[:start] + str(result) + expression[end + 1:]
            
    # Evaluate the final expression
    try:    
        result = eval(expression)
        pprint.pprint(f"{expression} = {result}")
    except ZeroDivisionError:
        print ('Error: Division by zero detected. Please try again!')
        return # Exit the function on error
    except Exception as e:
        print (f'Error: {e}. Please try again!')
        return

    
            
    # Ask the user if they want to continue calculating
    continue_calculating = input("Do you want to continue calculating (Yes/No): ")
    if continue_calculating.capitalize() == "Yes":
        while True: # An infinite loop prompts the user to enter an expression without happening ZerodivisonError
            continue_expression = input('Expression you want to continue calculating: ').strip()
            continue_expression = replace_percentages(continue_expression)
            continue_expression = "".join(continue_expression.strip().split()) # remove spaces between the expression
            if "/0" in continue_expression or "%0" in continue_expression:
                print("Error: Division by zero detected. Please try again!")
            else:
                new_expression = str(result) + continue_expression
                Calculator(new_expression)
                break
    else:
        print(f"Final result: {result}")
        


# Start the calculation
while True: # An infinite loop prompts the user to enter an expression without happening ZerodivisonError
    initial_expression = input("Enter an expression: ").strip()
    initial_expression = replace_percentages(initial_expression)
    initial_expression = "".join(initial_expression.split()) # remove spaces between the expression
    if "/0" in initial_expression or "%0" in initial_expression:
        print ('Error: Division by zero detected. Please try again!')
    else:
        Calculator(initial_expression)
        break

