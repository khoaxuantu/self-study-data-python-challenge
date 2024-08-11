def calculate():
    while True:
        print("Enter 'A' for Addition.")
        print("Enter 'S' for Subtraction.")
        print("Enter 'M' for Multiplication.")
        print("Enter 'D' for Division.")
        print("Enter '%' for Modulo.")
        choice = input("Enter Choice (A,S,M,D,%): ").upper()
        
        if choice not in ('A', 'S', 'M', 'D', '%'):
            print("Invalid Input")
            continue
        
        num_count = int(input("Enter the number of values: "))
        nums = []
        for i in range(num_count):
            num = input(f"Enter value {i+1}: ")
            try:
                nums.append(float(num))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
            
        if choice == "A":
            result = sum(nums)
            operation = "+"
        elif choice == "S":
            result = nums[0] - sum(nums[1:])
            operation = "-"
        elif choice == "M":
            result = 1
            for num in nums:
                result *= num
            operation = "*"
        elif choice == "D":
            try:
                result = nums[0]
                for num in nums[1:]:
                    result /= num
                operation = "/"
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                continue
        elif choice == "%":
            result = nums[0] % nums[1]
            operation = "%"
        
        result_string = f"{nums[0]}"
        for num in nums[1:]:
            result_string += f" {operation} {num}"
        print(f"Result: {result_string} = {result}")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != "yes":
            break

calculate()

#Gud job! But the 3rd requirement requires you to do more than 2 pairs of numbers with different operations. E.g: 5+2-8
#Keep up the good works! Feel free to look through others' projects or ask us if you have any questions
