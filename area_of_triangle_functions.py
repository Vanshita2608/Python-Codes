#practice functions
#area_of_triangle_functions.py


def tarea(b,h):
	area =  1/2*b*h               # (0.5*b*h)
	return(area)

b = float(input("Enter base: "))
h = float(input("Enter height: "))
area = tarea(b,h)
print("Area of triangle is: " , area)