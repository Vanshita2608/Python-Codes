	#write a python script to check duplicate element in the list
#check_duplicate_lists.py

l1 = [1,2,3,4,5,6,7,8,9,10,1,3,5,7,9]
element = int(input("Enter your element to be checked : "))
c = l1.count(element)
if c==0:
	print("Element doesn't exist")
elif c==1:
	print("One occurrence")
else:
	print("Duplication")