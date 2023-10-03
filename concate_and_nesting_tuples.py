#concating and nesting of tuples
#concate_and_nesting_tuples.py

print("\nConacte 2 tuples")
t1 = (10,20,30,40)
t2 = ('ten' , 'twenty')
t3 = t1+t2
print(t3)

print("\nNesting of tuples")
t3 = (t1,t2)
print(t3)

print("\nRepetition")
tr = ('logic' ,)*3
print(tr)

print("\nImmutablity")
t = (5,10,15,20)
t1[0] = 40
print(t1)