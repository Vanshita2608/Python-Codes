class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def getPerson(self):
		print("Name=",self.name)
		print("Age=",self.age)

class Employee(Person):
	def __init__(self,name,age,code,exp,basic_sal):
		super().__init__(name,age)
		self.code=code
		self.exp=exp
		self.basic_sal=basic_sal

	def getEmp(self):
		super().getPerson()
		print("Code=",self.code)
		print("Experience=",self.exp," years")
		print("Basic Salary=",self.basic_sal)
		self.grossSal()

	def grossSal(self):
		hra=self.basic_sal*0.37
		da=self.basic_sal*0.78
		ta=self.basic_sal*0.06
		gross_salary=self.basic_sal+hra+da+ta
		print("Gross Salary=",gross_salary)	

e1=Employee("Swayam",30,121,5,10000)
e1.getEmp()