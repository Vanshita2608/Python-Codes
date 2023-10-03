#string functions/methods

#len
print("\nlen() function")
s1 = "Vanshita Shah"
l = len(s1)
print("The length of s1 is :" , l)

#working with alphabet cases
#capitalise
print("\ncapitalize() function")
s2 = "vanshita"
c = s2.capitalize()
print("The capitalized version of s2 is :" , c)

#casefold() / lower()
print("\ncasefold() function")
s3 = "VANSHITA"
cf = s3.casefold()
print("The casefolded version of s3 is :" , cf)

#swapcase()
print("\nswapcase() function")
s4 = "VaNsHiTa"
sc = s4.swapcase()
print("The swapcased version of s4 is :" , sc)

#title()
print("\ntitle() function")
s5 = "the sandwiches are tasty"
t = s5.title()
print("The titled version of s5 is :" , t)

#replace()
print("\nreplace() function")
s6 = "Caris"
r = s6.replace("C" , "P")
print("The replaced version of s6 is :" , r)

#strip()
print("\nstrip() function")
s7 = "			Hello all today is tuesday"
st = s7.strip()
print("The trimmed version of s7 is :" , st)

#count()
print("\ncount() function")
s8 = "An aplle a day keeps the doctor away"
c1 = s8.count("apple")
print("The count of c1 is :" , c1)
c2 = s8.count('a')
print("The count of 'a' is :" , c2)
c3 = s8.count('a' , 5)
print("The count of 'a' after 5 is :" , c3)

#find()
print("\nfind() function")
s9 = "Hello Friends"
print(s9.find('e'))
print(s9.find('g'))

#rindex()
print("\nrindex() function")
s10 = "Welcome to Python lab"
index = s10.rindex('o')
#print(s10.find('x'))

#partition()
print("\npartition() function")
s11 = "COVID-19 is the deadliest virus"
part = s11.partition('deadliest')
print(part)
part1 = s11.partition('wowwww')
print(part1)

#split()
print("\nsplit() function")
s12 = "Hello, Friends, How are you?"
x = s12.split(',')
print(x)
x1 = s12.split(',' , 1)
print(x1)