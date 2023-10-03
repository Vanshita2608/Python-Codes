#wap to check whether the given email id is valid or not
#email_check.py

'''
if '@' in email:
	print("Valid")
else:
	print("Not Valid")
'''

email = input("Enter your email address :")
#print('@' in email)

if '.' and '@' not in email:
	print("Invalid")
elif '@' and 'com' not in email:
	print("Invalid")
else:
	print("Valid")