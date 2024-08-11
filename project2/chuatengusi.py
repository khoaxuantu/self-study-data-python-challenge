def cal_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Zero Division Error. Please enter new expression. "

def main():
    cur_expression = ""
    print("Calculator")
    print("Please enter your expression. Enter 'E' for end.")
    while True:
        new_expression = input("Enter your expression: ").strip()
        if new_expression.upper() == 'E':
            if cur_expression:
                final_result = cal_expression(cur_expression)
                print(f"Final Result: {final_result}")
            break        
        if cur_expression:
            cur_expression = f"({cur_expression}) {new_expression}"
        else:
            cur_expression = new_expression
        result = cal_expression(cur_expression)
        if result == "Zero Division Error. Please enter new expression. ":
            print(result)
            cur_expression = ""
            continue
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
#You nailed it!!