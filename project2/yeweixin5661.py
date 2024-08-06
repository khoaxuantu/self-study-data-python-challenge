valid_chars = "0123456789-+*/%() .\n"
current_val = None

while True:
    if current_val is not None:
        print(f"Current value: {current_val}")
        y = input("Continue your calculation (or type 'end' to finish): ")
        if y.lower() == "end": #end calculating
            break
        expression = str(current_val) + " " + y  # Use previous value
    else:
        y = input("Type your math here (or type 'end' to finish): ")
        if y.lower() == "end":
            break
        expression = y

    if any(c not in valid_chars for c in expression):
        print("WARNING: Invalid Equation")
        continue

    try:
        current_val = eval(expression)
        print(f"Value: {current_val}")
    except Exception as e:  
        print(f"Error in calculation: {e}")  