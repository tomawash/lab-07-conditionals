number1 = float(input("Please input a number "))

number2 = float(input("Please input another number "))

op = input("What type of operation would you like to do? (mul/div/mod) ")

if op == "mul":
	result = number1 * number2
	print(result)
elif op == "div":
	result = number1 / number2
	print(result)
elif op == "mod":
	result = number1 % number2
	print(result)
else:
	print("invalid operation")