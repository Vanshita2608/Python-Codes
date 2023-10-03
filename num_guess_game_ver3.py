#number guessing game
#num_guess_game_ver3.py

class Error(Exception):
	pass
class ValueTooSmallError3(Exception):
	pass
class ValueTooLargeError3(Exception):
	pass

import random

number = random.randint(1,20)
count = 0
win_stat = False

while(count<3):
	try:
		i_num = int(input("\nEnter the number in the range of 1-20 = "))
		if i_num < number:
			raise ValueTooSmallError3
		elif i_num > number:
			raise ValueTooLargeError3
		else: 
			win_stat = True
			print("_____Congratulations....You Won :)_____")
		break
		
	except ValueTooSmallError3:
		print("Your value is too small...Try again...!! :(")
		print()
	except ValueTooLargeError3:
		print("Your value is too big...Try again...!! :(")
		print()
	count += 1
if win_stat == False:
	print("_____OOPS....You Lost :(_____")
