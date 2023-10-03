#built-in functions
#built_in_funcs.py

print("\nBuilt-in functions")
print("1. any()")
print(any([1,]))
print(any((1,)))
print(any({1:1}))
print(any({}))
print(any(set()))

print("\n2. all()")
m1 = [1,1,1]
x = all(m1)
print(x)
m2 = [True,True,True]
print(all(m2))
m3 = [0,1,1]
print(all(m3))

print("\n3. chr()")
print(chr(65))
print(chr(97))
print(chr(21325))
print(chr(128512))

print("\n4. ord()")
print(ord('A'))
print(ord('a'))
print(ord(' '))

print("\n\n\n_____FILTER_____")
print("\nTheory:")
print("Inside filter function (function being invoked by filter()) , we can return only boolean values")
print("filter, map and reduce sab me 1st arugument will be function and 2nd one will be an iterable")
print("Note: when function is defined (element for element in iterable if function(element))")
print("\n")
def fun(variable):
	#print(variable)
	letter = ['a','e','i','o','u']
	if(variable in letter):
		return True
	else:
		return False

sequence = ['P','y','t','h','o','n','i','c']
filtered = filter(fun , sequence)
print(filtered)
print("The filtered letters are: ")
for s in filtered:
	print(s)



print("\n\n\n_____MAP_____")
print("Theory:")  
print("Here every element of an iterable will be transformed (some operation will be performed on each element)")
'''
numbers = [1,2,3,4,5]
squared = []
for num in numbers:
	squared.append(num**2)
print(squared)
'''
print("\n\nvariation 1 :")
def square(number):
	return number**2
numbers = [1,2,3,4,5]
squared = map(square , numbers)
print(list(squared))

print("\n\nvariation 2 :")
str_nums = ["6" , "7" , "8" , "9"]
int_nums = map(int , str_nums)
print(list(int_nums))

numbers = [-4 , -3 , 0 , 4 , 3]
abs_values = list(map(abs , numbers))
print(abs_values)
from math import sqrt
sqrt_values = list(map(sqrt , numbers))
print(sqrt_values)


words = ["Working" , "of" , "Python" , "map()" , "function"]
print(list(map(len , words)))


print("\n\nvariation 3 :")
first_it = [1,2,3]
second_it = [4,5,6]
print(list(map(pow , first_it , second_it)))


print("\n\n\n_____REDUCE_____")
print("Theory:")
print("It applies a mathematical technique on the elements of an iterable and returns a _cumulative answer_ ")
print("Syntax : functools.reduce(myFinc , iterable , initializer")
def myAdd(a,b):
	result = a + b
	print(f"{a} + {b} = {result}")
	return result
from functools import reduce
numbers = [0,1,2,3,4]
print(reduce(myAdd , numbers))
print("\n")
print(reduce(myAdd , numbers , 100))