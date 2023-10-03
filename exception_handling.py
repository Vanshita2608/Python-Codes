#exception handling
#exception_handling.py

'''
print("\n\n_____Exception Handling by Python(language)_____")
a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = a/b
print("a/b = %d" %c)
'''


'''
print("\n\n_____Exception Handling by Programmer_____")
a = int(input("Enter a = "))
b = int(input("Enter b = "))
try:
	c = a/b
	print(c)
except:
	print("Divisor can not be zero")
print("End of program")
'''


'''
print("\n\n_____To print desciption of an exception_____")
a = int(input("Enter a = "))
b = int(input("Enter b = "))
try:
	c = a/b
	print(c)
except Exception:
	print("Divisor can not be zero")
	print(Exception)
print("End of program")
#-----------OR-------------
except Exception as e:
	print("Divisor can not be zero")
	print(e)
print("End of program")
'''


'''
print("\n\n_____else block_____")
a = int(input("Enter a = "))
b = int(input("Enter b = "))
try:
	c = a/b
	print(c)
except:
	print("Divisor can not be zero")
else:
	print("No exception")
print("End of program")
'''


'''
print("\n\n_____Handling multiple exceptions_____")
try:
	fileptr = open("file1.txt" , "r")
	a = 5/0 
except ArithmeticError:
	print("Division by 0")
except IOError:
	print("File not found")
else:
	print("No exception")
	fileptr.close()
'''


'''
print("\n\n_____Declaring multiple exceptions_____")
try:
	fileptr = open("file1.txt" , "r")
	#a = 10/0
except(ArithmeticError , IOError) as e:
	print(type(e) , e)
else:
	print("Successfuly Done")
'''


'''
print("\n\n_____finally_____")
try:
	ans = 15/0
	print(ans)
except ZeroDivisionError:
	print("Denominator must not be zero")
finally:
	print("finally block executed")
'''


'''
print("\n\n_____finally_____")
f = None
try:
	f = open("file1.txt" , encoding = "utf-8")
except:
	print("You are trying to open non existing file")
finally:
	if f:
		f.close()
		print("File closed successfully")
	print("All resources closed...")
'''

print("Sab comment me hai, pehle comment hata :>")