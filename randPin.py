#Generates a pseudo-random numerical code from 1 to 20 digits long.

from random import randint

isDigit = False
while isDigit == False:
	digits = input("How many digits should the code be? ")
	try:
		digits = int(digits)
	except:
		pass
	if type(digits) != int:
		print("Not an integer. Please give me an integer. ")
	else:
		isDigit = True

while digits < 1:
	digits = input("Please choose at least 1 digit in length: ")
	digits = int(digits)
while digits > 20:
	digits = input("That's a long code, how about one that's no more than 20 digits long: ")
	digits = int(digits)

if digits == 1:
	print(randint(0,9))

else:
	pin = []
	for x in range(0,digits):
		pin.append(randint(0,9))
	for i in range (0,len(pin)):
		print(pin[i], end="")
	print("\n")
