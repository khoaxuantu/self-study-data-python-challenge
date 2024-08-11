express = " "
Ans = 0
while True:
    express = input("> type quit to exit. \nEnter your expression: ").strip()
    if express.lower() == "quit":
        break
    if not express: 
        print("Enter a valid math equation.")

    else:
        if express[0] in {'+', '-', '*', '/', '%'}:
            express = str(Ans) + express
        try: 
            print("Result: ", eval(express))
            Ans = eval(express)
        except Exception as e:
            print("Invalid expression. Please try again.", str(e))

#You nailed it!