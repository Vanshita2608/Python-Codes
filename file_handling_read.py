#file_handling_read.py

#normal
'''
try:
	file = open("f1.txt","r")
	for line in file:
		print(line,end="")
except:
	print("File Error")
finally:
	if file:
		file.close()
'''


#readline() method
'''
try:
	file = open("f1.txt","r")
	print(file.readline())
	print(file.readline(2))
	print(file.readlines())
	for line in file:
		print(line,end="")
except:
	print("File Error")
finally:
	if file:
		file.close()
'''

#read() method
try:
	file = open("f1.txt","r")
	print(file.read(1))
	for line in file:
		print(line,end="")
except:
	print("File Error")
finally:
	if file:
		file.close()