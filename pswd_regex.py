#pswd_regex.py

import re
count = 0
pswds = ['Password1' , 'Password2' , 'PasswordThree', 'P4' , 'myPassworD1!!']
for pwd in pswds:
	dmo = re.search(r'\d',pwd)
	if len(pwd)>=5 and len(pwd)<10:
		if dmo:
			count += 1
			cmo = re.search(r'[A-Z]+' , pwd)
			if cmo:
				count += 1
				scmo = re.search(r'\w\W+' , pwd)
				if scmo:
					count += 1
		if count==3:
			print(pwd,"->","OK")
		else:
			print(pwd,"->","NOT OK")
	else:
		print("Password Length Inavlid")
	count = 0