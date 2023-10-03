# special sequences

import re

txt="Unicode is a character set pincode is 400067 of a country"
x=re.findall("\AUnicode",txt)
print(x)
print()

x=re.findall(r"\bis",txt)
print(x)

print()
x=re.findall("country\Z",txt)
print(x)

print()
x=re.findall("\Bcod",txt)
print(x)

print()
x=re.findall("\d",txt)
print(x)

#variation
x=re.findall("\d+",txt)
print(x)

print()
x=re.findall("\D",txt)
print(x)

print()
x=re.findall("\s",txt)
print(x)

print()
x=re.findall("\S",txt)
print(x)

print()
x=re.findall("\w",txt)
print(x)

print()
x=re.findall("\W",txt)
print(x)
