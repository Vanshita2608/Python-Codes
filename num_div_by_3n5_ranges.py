'''     wap to display and count numbers divisible by 3 and 5 from 1 to 50 using while loop
        number from 1 to 50
        if num is multiple of 3 "fizz"
		if num is multiple of 5 "buzz"
		if num is multiple of 3&5 "fizzbuzz"
		else num itself       '''

#num_div_by_3n5_ranges


count = 0
i = 1
while(i<=50):
	if(i%3==0):
		count+=1
		print("Fizz" , i)

	elif(i%5==0):
		count+=1
		print("Buzz" , i)

	else:
		print("FizzBuzz" , i)
	i+=1
