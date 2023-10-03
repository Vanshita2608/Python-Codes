#file_handling_writelines.py

cities = ["Mumbai\n","Pune\n","Baorda\n"]
file = open("f://cities.txt",mode="a+",encoding="utf-8")
file.writelines(cities)
for city in file:
	print(city)
file.close()