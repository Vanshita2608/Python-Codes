#regex
#regex.py

import re

t1 = "Where there is a will there is a way in 590"
x = re.findall("there" , t1)
print(x)
x = re.findall("[a-e]" , t1)
print(x)
x = re.findall("\d" , t1)
print(x)
x = re.findall("\d+" , t1)
print(x)

t2 = 'hello world'
x = re.findall("he..o" , t2)
print(x)

t3 = "Python Programmers"
x1 = re.findall("^python" , t3)
print(x1)
x2 = re.findall("^Python" , t3)
print(x2)
x3 = re.findall("Programmers$" , t3)
print(x3)

t4 = "Spain Is a Country"
x = re.findall("aix*" , t4)
print(x)

t5 = "all People are Beautiful"
x = re.findall("al{2}" , t5)
print(x)

t6 = "code character"
x = re.findall("code|char" , t6)
print(x)