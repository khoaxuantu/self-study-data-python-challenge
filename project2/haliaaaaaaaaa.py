def calculator(expression):
    try:
        result = eval(expression)
        print(f"Result of '{expression}' is: {result}")
    except Exception as e:
        print(f"Invalid expression: {e}")

def main():
    print("Welcome to the calculator program.")
    while True:
        expression = input("Enter the expression (e.g., A + B, A + B + C, (A * B + C)/D): ").strip()
        calculator(expression)
        
        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
#Nice! However, just my opinion but I hope you can mention which operations can your calculator perform.