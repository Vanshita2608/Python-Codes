#write a python program/script to multiply each element by 2 in a list
#multiply_by_2_lists.py

l1 = [1,2,3,4,5]
mult = 0
for i in range (0,len(l1)):
	l1[i] = l1[i] * 2
print(l1)
