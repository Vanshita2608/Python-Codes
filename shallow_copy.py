#shallow copy

l1 = [1,2,3]
l2 = l1.copy()
print(id(l2))
print(id(l1))

l2[0] = 5
print(l2)
print(l1)