class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def getPerson(self):
		print("Name: ",self.name)
		print("Age: ",self.age)

class Sports:
	def __init__(self):
		super().__init__(name,age)
		self.spoints = 0
	def getSpoints(self):
		self.spoints = 0
		choice = input("Have you participated in Sports (Y)")
		if choice == 'Y':
			level = input("Which level have you psrticipated (NL = National Level,S = State Level, D = District Level)")
			if level == 'NL':
				self.spoints = 25
			elif level == 'S':
				self.spoints = 15
			elif level == 'D':
				self.spoints = 5
		elif choice == 'N':
			print("Ok")
			self.spoints = 0
		else:
			print("Invalid Input")

class Student(Person,Sports):
	def __init__(self,name,age,id1,sem,m1,m2):
		super().__init__(name,age)
		self.id1 = id1
		self.sem = sem
		self.m1 = m1
		self.m2 = m2
	def totalMarks(self):
		super().getSpoints()
		total = self.m1 + self.m2 + self.spoints
		print("Total Marks:" ,total)
	def avgMarks(self):
		avg = (self.m1 + self.m2 +self.spoints)/3
		print("Average Marks:" ,avg)
	def getStudent(self):
		super().getPerson()
		print("Id: ",self.id1)
		print("Semester: ",self.sem)
		print("Marks of subject 1:" ,self.m1)
		print("Marks of subject 2:" ,self.m2)
e1 = Student("Tanay",18,17,4,19,16)
e1.getStudent()
e1.getSpoints()
e1.totalMarks()
e1.avgMarks()
