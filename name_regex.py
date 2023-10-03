#name_regex.py

import re

name = '''
Abcd
Xyz
'''
nm = re.compile(r'Mr\.\s\w+')
nm = re.compile(r'Mr\.?\s\w+')
matches = nm.finditer(name)
for m in matches:
	print(m.group(0))
