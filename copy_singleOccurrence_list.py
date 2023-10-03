#consider l1 , copy only single occurrence of element in another list
#copy_singleOccurrence_list.py

l1 = ['hi' , 'hello' , 'bye' , 'hi']
l2 = []
for e in l1:
	if e not in l2:
		l2.append(e)
print(l2)

