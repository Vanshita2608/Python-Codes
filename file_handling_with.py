#file_handling_with.py

with open("f1.txt","a") as f:
	f.write("with")
with open("f1.txt","r") as file:
	data = file.readlines()
	for line in data:
		 word = line.split()
		 print(word)