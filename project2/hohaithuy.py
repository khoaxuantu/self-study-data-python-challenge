def evaluate_expression(op_str):
    stack = []
    num = 0
    sign = 1  # 1 means positive, -1 means negative
    while len(op_str) > 0:
        token = op_str.pop(0)
        if token.isdigit():
            num = int(token)
            while len(op_str) > 0 and op_str[0].isdigit():
                num = num * 10 + int(op_str.pop(0))
            stack.append(sign * num)
            sign = 1  # Reset sign
            
        elif token == '+':
            sign = 1
            
        elif token == '-':
            sign = -1
            
        elif token == '(':
            stack.append(sign * evaluate_expression(op_str))
            sign = 1
            
        elif token == ')':
            break
        
        elif token in '*/%':
            op = token
            next_num = 0
            if len(op_str) > 0 and op_str[0].isdigit():
                next_num = int(op_str.pop(0))
                while len(op_str) > 0 and op_str[0].isdigit():
                    next_num = next_num * 10 + int(op_str.pop(0))
            elif len(op_str) > 0 and op_str[0] == '(':
                op_str.pop(0)
                next_num = evaluate_expression(op_str)
            if op == '*':
                stack[-1] = stack[-1] * next_num
            elif op == '/':
                stack[-1] = int(stack[-1] / next_num)  # Use int() to do floor division
            elif op == '%':
                stack[-1] = stack[-1] % next_num
    return sum(stack)

print("************************ Simple calculator ************************")
print("Available options: [+, -, *, /, %, (, ) , ans, Exit]")
print("\tans is the result of the last operation")
print("\tExample1: 2 + 3 * 4")
print("\tExample2: (2 + 3) * 4")
print("\tExample3: ans * 4")
print("*" * 67)

ans = None
while True:
    op_str = input("Enter an expression: ")
    if op_str == "Exit":
        break
    
    if "ans" in op_str:
        if ans is None:
            print("Error: ans is not defined yet")
            continue
        op_str = op_str.replace("ans", str(ans))
    
    raw_op_str = op_str
    op_str = op_str.replace(" ", "")
    
    ans = evaluate_expression(list(op_str))
    print(f"Result: {raw_op_str} = {ans}")
    