#sets

s = {}
print(type(s))

s = set()
print(type(s))
print(s)

#the set() method
print("\n\nThe set() method")
x = set(['pen' , 'pencil' , 'paper'])
print(x)
y = set(('pen' , 'pencil' , 'paper'))
print(y)
z = set('hello')
print(z)

#size and membership of set
print("\n\nSize and membership of set")
a = ('first' , 'second' , 'third')
print(len(a))
print('first' in a)
print('abcd' in a)




#Set operators and methods
print("\n\n\nSet operators and methods")
x1 = {1,2,3,4,5}
x2 = {1,3,6,7,8}
print("\nUnion")
print(x1 | x2)
print(x1.union(x2))

print("\nIntersection")
print(x1 & x2)
print(x1.intersection(x2))

print("\nDifference")
print(x1 - x2)
print(x1.difference(x2))

print("\nSymmetric Difference")
print(x1 ^ x2)
print(x1.symmetric_difference(x2))

print("\nDisjoint")
print(x1.isdisjoint(x2))

x3 = {1,2,3}
x4 = {1,2,3}
print("\nSubset")
print(x3 <= x4)
print(x3.issubset(x4))

print("\nProper Subset")
print(x3 < x4)

print("\nSuperset")
print(x3 >= x4)
print(x3.issuperset(x4))

print("\nProper Superset")
print(x3 > x4)

 
#Set methods
print("\n\n\nSet methods")
print("\n1. add()\n2. remove()\n3. discard()")
abc = {'Flash Drive' , 'HDD' , 'SSD'}

abc.add('DVD')
print(abc)

abc.remove('Flash Drive')
print(abc)

print(len(abc))
abc.discard('RAM')
print(abc)
print(len(abc))

print("\n4. clear()\n5. pop()")
abc.pop()
print(abc)
abc.clear()
print(abc)

print("\n6. update()\n7. intersection_update()\n8. difference_update()\n9. symmetric_difference_update()")
xyz = {1,2,3,4}

xyz.update([3,5])
print(xyz)

xyz.intersection_update([3,4])
print(xyz)

xyz.difference_update([1,2])
print(xyz)

xyz.symmetric_difference_update([1,2])
print(xyz)