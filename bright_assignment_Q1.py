#bright_assignment_Q1.py

'''
print("___Enter details of the employee___")
job_num = input("Enter job number = ")
level_num = int(input("Enter level number = "))
basic_pay = float(input("ENter basic pay = "))

if level_num == 1:
	ca=1000
	ea=500
elif level_num == 2:
	ca=750
	ea=200
elif level_num == 3:
	ca=500
	ea=100
elif level_num == 4:
	ca=250
	ea=0
else:
	print("INVALID")

gsal = basic_pay + (basic_pay*0.25) + ca + ea
if gsal<2000:
	income_tax = 0
elif 2000<gsal<=4000:
	income_tax = 0.03*gsal
elif 4000<gsal<=5000:
	income_tax = 0.05*gsal
elif gsal>5000:
	income_tax = 0.08*gsal

net = gsal - income_tax
print("Gross Salary = " , gsal)	
print("Net Salary = " , net)
'''

num_employees = int(input("Enter number of employees: "))
for i in range(num_employees):
    print(f"\nEnter details for employee {i+1}:")
    job_number = input("Enter Job number: ")
    level_number = int(input("Enter Level number: "))
    basic_pay = float(input("Enter Basic pay: "))

    if level_number == 1:
        ca = 1000
        ea = 500
    elif level_number == 2:
        ca = 750
        ea = 200
    elif level_number == 3:
        ca = 500
        ea = 100
    elif level_number == 4:
        ca = 250
        ea = 0

    g_sal = basic_pay + (basic_pay * 0.25) + ca +ea

    if g_sal <= 2000:
        it = 0
    elif 2000< g_sal <= 4000:
        it = 0.03 * g_sal 
    elif 4000< g_sal <= 5000:
        it = 0.05 * g_sal 
    elif g_sal > 5000:
        it = 0.08 * g_sal 

    net_sal = g_sal - it

    print("Gross Salary:" ,g_sal)
    print("Net Salary:" ,net_sal)
