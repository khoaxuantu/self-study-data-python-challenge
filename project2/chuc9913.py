def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def modulo(num1, num2):
    return num1 % num2

print("Enter 'A' for Addition.")
print("Enter 'S' for Subtraction")
print("Enter 'M' for Multiplication.")
print("Enter 'D' for Division.")
print("Enter 'Mod' for Modulo.")

select = input("Enter Choice (A, S, M, D, Mod): ")

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

if select == 'A':
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 'S':
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 'M':
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 'D':
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
elif select == 'Mod':
	print(number_1, "%", number_2, "=",
					modulo(number_1, number_2))
else:
	print("Invalid input")
