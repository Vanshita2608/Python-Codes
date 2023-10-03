#write a python script to find the roots of a quadratic equation

import math

a = int(input("Enter the value for a :"))
b = int(input("Enter the value for b :"))
c = int(input("Enter the value for c :"))

d = b**2-4*a*c 

if d>0:
	root_1 = (-b + math.sqrt(d))/(2*a)
	root_2 = (-b - math.sqrt(d))/(2*a)
	print("root_1 = " , root_1)
	print("root_2 = " , root_2)

elif d==0:
	root_1 = root_2 = (-b)/(2*a)
	print("root_1 = " , root_1)
	print("root_2 = " , root_2)

elif d<0:
	print("Roots are imaginary")

else:
	print("Invalid")