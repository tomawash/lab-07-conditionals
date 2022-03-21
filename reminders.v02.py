import datetime

# usertime = float(input("What hour of the day is it? (0 - 23) "))

now = datetime.datetime.now() # this gives us the current time
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

usertime = now.hour

if usertime <= 5:
	print("It's early. You should be sleeping!")
elif usertime <= 7:
	print("Wake up, brew that coffee, get that mile run in, and get that breakfast...")
elif usertime <= 9:
	print("Time to go to work.")
elif usertime <= 12:
	print("You should be working!")
elif usertime <= 13:
	print("Take your lunch break!")
elif usertime <= 17:
	print("Do you feel that afternoon lull?")
elif usertime <= 19:
	print("Time to hit the gym...")
elif usertime <= 21:
	print("Gotta eat that dinner.")
elif usertime <= 23:
	print("Get that SLEEP. And rePEAT!")
else:
	print("You didn't type an acceptable value! (0-23)")