#functions

print("\n3 types of functions")
print("1. Built-in (library functions) : print() , help() , type() etc...")
print("2. User defined functions : developed by users as per the requirements using def keyword")
print("3. Anonymous functions : also called as lambda function, cuz they arte not declared with the standard def keyword")

print("\nNo parameter , No return value")
def Hello():
	print("Hello Hello Hello Hello Hello")
Hello()

print("\nWith parameter , without return value")
def name(name):
	print("Hello" , name)
name("Vanhsita")

print("\nWith parameter and return value")
def add(a,b):
	c = a+b
	return(c)
x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
z = add(x,y)
print("Addition of x & y is: " , z)


print("\n\n_____Functions with multiple return values_____")
def swap(a,b):
	x=a
	a=b
	b=x
	return(a,b)
a=5
b=2
print("Before swap :- a = " , a , " b = " , b)
a,b = swap(a,b)
print("After swap :- a = " , a , " b = " , b)

print("\n\n_____Functions with default arguments_____")
def simple_i(p,n, r=4):
	si = p*r*n/100
	return(si)
p = int(input("Enter principal amount = "))
n = int(input("Enter no. of years = "))
print("SI = " , simple_i(p,n,5))
#without passing interest rate
print("SI = " , simple_i(p,n))

print("\n\n_____Functions with keyword arguments_____")
def add(a,b):
	return(a+b)
print(add(1,2))
print(add(b=2 , a=1))

print("\n\n_____Functions with variable arguments_____")
def add(*args):
	print(type(args))
	total = 0
	for i in args:
		total += i
	return total
print(add(10,20,30,40,50))