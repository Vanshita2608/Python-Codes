#lambda functions (Anonymous functions)

twice = lambda x: x*2
print(twice(5))
x = lambda a,b: a*b
print(x(2,4))

print("\n\n_____FILTER with lambda_____")
myL = [1,-9,0,5,-8,2,-3]
pos_l = list(filter(lambda x: (x>0) , myL))
print(pos_l)

print("\n\n_____MAP withlambda_____")
myL2 = [1,3,5,7,9]
sq_l = list(map(lambda x: x**2 , myL2))
print(sq_l)

print("\n\n_____REDUCE with lambda_____")
from functools import reduce
li = [5,8,1,7,2,10]
sum = reduce((lambda x,y: x+y),li)
print(sum)
print("__________OR__________")
import functools
li_1 = [1,3,5,7,9,10]
print("max = " , end = " ")
print((functools.reduce(lambda a,b: a if a>b else b, li_1)))
