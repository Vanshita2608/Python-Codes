#practice functions
#gross_sal_functions.py

def gsal():
	da = 0.65 * bsal
	hra = 0.39 * bsal
	ta = 0.07 * bsal
	gsal = bsal + ta + da + hra
	return(gsal)


code = input("Enter your code: ")
name = input("Enter your name: ")
bsal = float(input("Enter your basic salary: "))
gross = gsal()
print("Gross salary = " , gross)