#tuple methods
#tuple_methods.py

print("\n___TUPLE METHODS___")
#index()
print("\nindex()")
a = ('A' , 'B' , 'C')
print(a.index('A'))
#print(a.index('D'))

#count()
print("\ncount()")
a = ('A' , 'B' , 'C')
print(a.count('A'))
print(a.count('D'))

#enumerate()
print("\nenumerate()")
a = ('A' , 'B' , 'C' , 'D')
for index,a in enumerate(a):
	print((index,a))

#max() min() sum() any()
print("\nmax() min() sum() any()")
lang = ('C' , 'Java' , 'C++' , 'VB' , 'PHP')
print(max(lang))
print(min(lang))
var = sorted(lang)
print(var)
nt = (1,2,3,4,5)
print(sum(nt))
print(any((1,)))