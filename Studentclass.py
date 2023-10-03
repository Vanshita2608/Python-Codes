class Student:
	
	def setStu(self):
		self.Id=input("Enter the id = ")
		self.name=input("Enter the name")
		self.branch=input("Enter the branch")
		self.marks=[]
		n=int(input("Enter how many subjects marks you want to enter="))
		for i in range(1,n+1):
			m=int(input("ENter the marks for subject"))
			self.marks.append(m)

	def getStu(self):
		print("Id=",self.Id)
		print("Name=",self.name)
		print("Branch=",self.branch)
		print(self.marks)

	def avg(self):
		a=sum(self.marks)/len(self.marks)
		print("Average=",a)
		

S1=Student()
S1.setStu()
S1.getStu()
S1.avg()
		


		 
