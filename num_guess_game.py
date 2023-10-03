#number guessing game
#num_guess_game.py

class Error(Exception):
	pass
class ValueTooSmallError(Error):
	pass 
class ValueTooBigError(Error):
	pass  

number = 10

while True:
	try:
		i_num = int(input("\nEnter the number = "))
		if i_num < number:
			raise ValueTooSmallError
		elif i_num > number:
			raise ValueTooBigError
		break

	except ValueTooSmallError:
		print("Your value is too small...Try again...!! :(")
		print()
	except ValueTooBigError:
		print("Your value is too big...Try again...!! :(")
		print()

print("_____Congratulations....You Won :)_____")



