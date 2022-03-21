move = input("Does it move? (yes/no) ")

if move == "yes":
	move1 = input("Should it move? (yes/no) ")
	if move1 == "yes":
		print("No problem then")
	elif move1 == "no":
		print("Tape it down")
	else:
		print("I'm sorry but I don't understand")
elif move == "no":
	move2 = input("Should it move? (yes/no) ")
	if move2 == "yes":
		print("Spray it")
	elif move2 == "no":
		print("No problem then")
	else:
		print("I'm sorry but I don't understand")
else:
	print("You didn't answer my question! Yes or no!")