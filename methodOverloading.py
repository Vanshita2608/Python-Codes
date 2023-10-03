from multipledispatch import dispatch 

@dispatch(int,int)
def multiply(a,b):
	print("2 params of int type")
	result=a*b

@dispatch(int,int,int)
def multiply(a,b,c):
	print("3 params of int type")
	return (a*b*c)

@dispatch(float,float,float)
def multiply(a,b,c):
	print("Float 3 params")
	print(a*b*c)

multiply(5,6)
multiply(2.2,3.3,3.6)
multiply(2,3,2)
