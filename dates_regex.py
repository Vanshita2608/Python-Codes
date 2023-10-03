#dates_regex.py

import re
dates = '''
01.05.2021
2021.04.15
2021.10.19
2021_05_16
'''
date = re.compile(r'(\d\d\d\d)\.(\d\d)\.(\d\d)')
date = re.compile(r'(\d\d\d\d)[_/_](\d\d)[_/_](\d\d)')
date = re.compile(r'(\d\d\d\d)[_/](0[4/5])[_/](\d\d)')
mo = date.finditer(dates)
for m in mo:
	print(m.group(0))
