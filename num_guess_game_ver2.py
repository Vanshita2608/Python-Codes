#number guessing game
#num_guess_game_ver2.py

import random

class Error(Exception):
	pass
class ValueTooSmallError2(Error):
	pass 
class ValueTooBigError2(Error):
	pass  

number = random.randint(1,20)

while True:
	try:
		i_num = int(input("Enter the number in the range of 1-20 = "))
		if i_num < number:
			raise ValueTooSmallError2
		elif i_num > number:
			raise ValueTooBigError2
		break

	except ValueTooSmallError2:
		print("You value is too small...Try again...!! :(")
		print()
	except ValueTooBigError2:
		print("You value is too big...Try again...!! :(")
		print()

print("_____Congratulations....You Won :)_____")