#user-defined exceptions
#custom_exceptions.py

#write a pyhton script to create a custom exception SalaryNotInRange which willbe raised if the employee salary is not specified in the given range

class SalaryNotInRangeError(Exception):
	def __init__(self,salary,msg = "Salary is not in (5000 , 15000) range"):
		self.salary = salary
		self.msg = msg
		super().__init__(self.msg)

	def __str___(self):
		return f'{self.salary} -> {self.msg}'

salary = int(input("Enter salary = "))
if not 5000 < salary < 15000:
	raise SalaryNotInRangeError(salary)
else:
	print("Salary = " , salary)