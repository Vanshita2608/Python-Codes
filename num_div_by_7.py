#wap to display and count numbers divisible by 7 from 1 to 50 using while loop 
#num_div_by_7

count = 0
i = 1
while(i<=50):
	if(i%7==0):
		count+=1
		print(i)
	i+=1
print("Total numbers divisible by 7 are :" , count)
