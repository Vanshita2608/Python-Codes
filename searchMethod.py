#search method
import re

txt="I use Python Prog"
x=re.search(" ",txt)
print(x)
print(x.group())
print(x.span())
print(x.group())
print(x.start())

#split method
txt1="I like programming language"
x=re.split(" ",txt1)
print(x)
x=re.split(" ",txt1,1)
print(x)


#sub method
x=re.sub(" ","*",txt1)
print(x)

