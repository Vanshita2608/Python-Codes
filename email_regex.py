#email_regex.py

import re
email = '''
pythonengineer@gmail.com
'''
nm = re.compile(r'([a-zA-z0-9\.]+)@([a-z]+)(\.[a-z]+)')
matches = nm.finditer(email)
for m in matches:
	print(m.group(0))
	print(m.group(1))
	print(m.group(2))
	print(m.group(3))