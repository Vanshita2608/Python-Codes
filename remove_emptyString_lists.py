#remove empty strings from the list of strings
# list1 = ['Mike' , "" , 'Emma' , "" , 'Kelly' , "" , 'Brad']

#write a python script to remove all the occurrences of a particular element in the list

#remove_emptyString_lists.py

l1 = ['Mike' , ' ' , 'Emma' , ' ' , 'Kelly' , ' ' , 'Brad']
element = str(input("Enter your element to be removed: "))
for e in l1:
	if e==element:
		l1.remove(e)
print(l1)

'''
l1 = [1,2,3,4,5,6,7,8,9,10,1,3,5,7,9]
element = int(input("Enter your element to be removed: "))
for e in l1:
	if e==element:
		l1.remove(e)
print(l1)

l1 = [1,2,3,4,5,6,7,8,9,10,1,3,5,7,9]
element = int(input("Enter your element to be removed: "))
c = l1.count(element)
for i in range(1,c+1):
	l1.remove(element)
print(l1)
'''