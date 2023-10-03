#file_handling_write.py

#w waala
'''
try:
	file = open("f2.txt" , "w")
	file.write("Writing to f2\n")
	file.write("Writing..........\n")
	print("Data")
except:
	print("Error")
finally:
	file.close()
''' 

#BYTE
bytes = b"0x410x420x43"
f = open("sample.bin" , 'wb')
f.write(bytes)
f.close()