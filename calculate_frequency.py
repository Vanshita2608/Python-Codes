'''   write a python script to count frequency of marks range out of 100 for n number of students.
      The range of marks is given as:
      0-39 , 40-49 , 50-59 , 60-69 , 70-70 , 80-100
       F       P       S       FC      D       E
'''

#calculate_frequency.py

fail = passs = successful = first_class = distinction = excellent = 0
print("___Enter marks out of 100___")
n = int(input("How many student's marks do you want to enter : "))
for i in range(1 , n+1):                       #range(0,n) bhi le sakte hai
	print("Enter the marks for student" , i)
	m = int(input())
	if m>=0 and m<=39:
		fail += 1
	elif m>=40 and m<=49:
		passs += 1
	elif m>=50 and m<=59:
		successful += 1
	elif m>=60 and m<=69:
		first_class += 1
	elif m>=70 and m<=79:
		distinction += 1
	else:
		excellent += 1
print("FAIL : " , fail)
print("PASS : " , passs)
print("SUCCESSFUL : " , successful)
print("FIRST CLASS : " , first_class)
print("DISTINCTION : " , distinction)
print("EXCELLENT : " , excellent)


#with dictionary
print("\n\n\n_____WITH DICTIONARY_____")
fd = {'0-39':0 , '40-49':0 , '50-59':0 , '60-69':0 , '70-79':0 , '80-100':0}

print("___Enter marks out of 100___")
n = int(input("How many student's marks do you want to enter : "))
for i in range(1 , n+1):                       #range(0,n) bhi le sakte hai
	print("Enter the marks for student" , i)
	m = int(input())
	if m>=0 and m<=39:
		fd['0-39'] += 1
	elif m>=40 and m<=49:
		fd['40-49'] += 1
	elif m>=50 and m<=59:
		fd['50-59'] += 1
	elif m>=60 and m<=69:
		fd['60-69'] += 1
	elif m>=70 and m<=79:
		fd['70-79'] += 1
	else:
		fd['80-100'] += 1
print(fd)