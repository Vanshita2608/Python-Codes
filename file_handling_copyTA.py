#Write a python script to copy th content of one file to another file(text file)
#file_handling_copyTA.py

with open("f1.txt","r") as fin, open("f:\\f1.txt","w") as fout:
	for line in fin:
		fout.write(line)

