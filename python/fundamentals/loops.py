for i in range(10):
	print(i)
else:
	# There was no break in the for loop so the print statement will run
	print("These are ten numbers")


for i in range(20, 30):
	print(i)
	if i == 25:
		break
else:
	print("I can only do up to 25")


for i in range(50, 60):
	print(i)
	if i == 55:
		print("Hey I got 25!")
		continue
else:
	print("55 is the midpoint")
