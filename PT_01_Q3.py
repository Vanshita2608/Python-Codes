#PT_01_Q3
#PT_01_Q3.py

t1 = [4,6,4,3,3,4,3,4,3,8]
k = 3
n1 = []
for i in t1:
	if i not in n1:
		if t1.count(i) > k:
			n1.append(i)
print(n1)


d1 = {'Ajay':(1.89,77) , 'Krish':(1.77,65) , 'William':(1.80,68) , 'Joho':(1.95,75)}
d2 = {}
d3 = {}
h = 1.8
w = 70
for k,v in d1.items():
	if (v[0]>h and v[1]>w):
		d2[k] = d1[k]
		d3[k] = v[1]/(v[0])**2
print(d2)
print(d3)


t1 = ('2.5' , '3.8' , '6' , '8.9' , '23')
l1 = []
for i in t1:
	l1.append(float(i))
print(max(l1))
print(min(l1))
print(sum(l1)/len(l1))
print(sum(l1))