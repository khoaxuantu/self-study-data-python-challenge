def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		raise ZeroDivisionError("Division by zero is not allowed.")
	return a / b

operation = {
	'A' : ('+', add),
	'S' : ('-', subtract),
	'M' : ('*', multiply),
	'D' : ('/', divide),
}

intro = '\n'.join([f'Enter "{key}" for {name}.' for key, (name, _) in operation.items()])
print(intro)

input0 = input("Enter Choice (A, S, M, D): ").upper()

if input0 in operation:
	try:
		input1 = float(input('Enter first number: '))
		input2 = float(input('Enter second number: '))

		operation_name, operation_func = operation[input0]
		result = operation_func(input1, input2)

		print(f"Result: {input1} {operation_name[0]} {input2} = {result}")

	except ValueError:
		print("Please enter valid number")

	except ZeroDivisionError as e:
		print(e)


else:
	print("Please enter valid choice (A, S, M, D)")


#Gud job on finishing this project! '
#However, just to let you know, Python is famous for many convinient built-in functions: e.g: eval() and also other ways to think out of the box to finish this project.
#I hope you can look through other projects to improve yours. Feel free to ask us!