#deep copy

l1 = [1,2,3]
l2 = l1
print(id(l1))
print(id(l2))

l2[0] = 5
print(l2)
print(l1)