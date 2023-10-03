#frozensets

print("\n")
x = frozenset(['is' , 'are' , 'were'])
print(x)
print(len(x))
print(x & {'is' , 'what'})

print("\n")
f = frozenset(['I' , 'We' ,  'Were'])
s = {'We' , 'They' , 'I'}
f &= s   
print(f)

print("\n\nNesting of frozenset")
x1 = frozenset(['Hello'])
x2 = frozenset(['Bolo'])
x3 = frozenset(['Chalo'])
new_x = {x1 , x2 , x3}
print(new_x)

'''
print("\n\nNesting of set")
x1 = set(['Hello'])
x2 = set(['Bolo'])
x3 = set(['Chalo'])
new_x = {x1 , x2 , x3}
print(new_x)
'''

print("\n\nDictionary in frozenset")
a = frozenset({1,2,3})
b = frozenset({'a' , 'b' , 'c'})
d = {a : 'hiiii' , b : 'byeee'}
print(d)