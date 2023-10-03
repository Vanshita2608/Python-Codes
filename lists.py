#lists
print("\nBasic List")
le=[]
print(le)

inr = [10,20,30,10]
print(inr)

list_1 = [1,2,'hi',5,True,7,'all']
print(list_1)
print(list_1[0])
print(list_1[2])
print(list_1[-1])
print(list_1[-3])

#multidimensional lists

l = ['Welcome' , ['all' , 'friends']]
print("\n\nMultidimensional Lists :")
print(l)
#indexing
print(l[0])
print(l[1])
print(l[1][0])
print(l[1][1])

#slicing in lists
print("\n\nSlicing in lists")
m = ['P' , 'y' , 't' , 'h' , 'o' , 'n']
print(m[2:5])
print(m[:-3])
print(m[2:])
print(m[:])

#add/change list elements
print("\n\nAdd/Change List Elements")
a = [2,4,6,8]
a[0] = 1
print(a)
a[1:4] = [3,5,7]
print(a)

#List Methods
print("\n\n\nList Methods")
fruits = ['apple' , 'orange']
print(fruits)
print("append()")
fruits.append('fig')
print(fruits)
summer = ['grapes' , 'mango']
fruits.append(summer)
print(fruits)
print("\nextend()")
f1 = ['plum' , 'kiwi']
fruits.extend(f1)
print(fruits)

#insert and remove
print("\ninsert()  &  remove()")
vowel = ['a','e','i','u']
vowel.insert(3,'o')
print(vowel)
vowel.remove('a')
print(vowel)

#pop
print("\npop()")
databases = ['MySQL' , 'MsSQL' , 'SQLite' , 'FireBase']
ret_val = databases.pop(1)
print(ret_val)
ret_val1 = databases.pop()
print(ret_val1)
print("Updated = " , databases)

#clear() & count()
print("\nclear()  &  count()")
l = [1,2,3]
l.clear()
print(l)
del l[:]
print(l)
demo = ['t','h','e','r','e']
print("Occurrance of e = " , demo.count('e'))

#reverse()
print("\nreverse()")
sys = ['windows' , 'MACos' , 'Linux']
sys.reverse()
print(sys)
print("_______other way_______")
reversed = sys[::-1]
print(reversed)

#sort() sorted()
print("\nsort()  &  sorted()")
lang = ['C' , 'Java' , 'C++' , 'VB' , 'Python' , 'PHP']
lang.sort()
print(lang)
print("__sorted()___")
lang = ['C' , 'Java' , 'C++' , 'VB' , 'Python' , 'PHP']
asl = sorted(lang)
print(asl)

#index()
print("\nindex()")
l1 = [1,2,'hi',5,True,'all']
id = l1.index('hi')
print(id)
print(l1.index(True))

