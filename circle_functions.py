#practice functions
#circle_functions.py

def cal_circle():
	d = 2*r
	a = 3.14*(r**2)
	p = 2*3.14*r
	return(d , a , p)

r = int(input("Enter radius: "))
d , a , p = cal_circle()
print("Diameter of circle is = " , d)
print("Area of circle is = " , a)
print("Perimeter of circle is = " , p)