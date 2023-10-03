#Write a python script to copy th content of one file to another file(text file)
#file_handling_copyTA_Binary.py

with open("f1.txt","rb") as fin, open("f:\\dog.jpg","wb") as fout:
	for line in fin:
		fout.write(line)
