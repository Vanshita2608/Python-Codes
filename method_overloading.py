#method overloading
#method_overloading.py

from multipledispatch import dispatch 

@dispatch(int,int)
def multiply(a,b):
	print("2 parameters of int type")
	result = a*b
	print(result)

@dispatch(int,int,int)
def multiply(a,b,c):
	print("3 parameters of int type")
	print(a*b*c)

@dispatch(float,float,float)
def multiply(a,b,c):
	print("3 parameters of float type")
	print(a*b*c)

multiply(5,5)
multiply(2,3,4)
multiply(2.2 , 3.4 , 2.3)