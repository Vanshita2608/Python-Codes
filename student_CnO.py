#create a class "student" having id,name,disciple and marks of 3 subjects. Provide setter and getter methods. Calculate the avg marks of the student
#student_CnO.py

'''
class Student:
	def setStu(self):
		self.id = input("Enter id: ") 
		self.name = input("Enter name: ")
		self.disciple = input("Enter disciple: ")
		self.marks1 = int(input("Enter marks of sub1 :"))
		self.marks2 = int(input("Enter marks of sub2 :"))
		self.marks3 = int(input("Enter marks of sub3 :"))
	def getStu(self):
		print("ID = " , self.id)
		print("Name = " , self.name)
		print("Discipline = " , self.discipline)
		print("Marks1 = " , self.marks1)
		print("Marks2 = " , self.marks2)
		print("Marks3 = " , self.marks3)
	def avg(self):
		self.avg = (self.marks1 + self.marks2 + self.marks3) / 3
		print("Average = " , self.avg)

s1 = Student()
s1.setStu()
s1.getStu()
s1.avg()
'''

#modified:
#modify the student class with n number of subjects
class Student:
	def setStu(self):
		self.id = input("Enter id: ") 
		self.name = input("Enter name: ")
		self.discipline = input("Enter discipline: ")
		self.marks = []
		n = int(input("How many subject's marks do you want to enter? :"))
		for i in range(1, n+1):
			print("Enter marks for subject " , + i)
			m = int(input())
			self.marks.append(m)

	def getStu(self):
		print("ID = " , self.id)
		print("Name = " , self.name)
		print("Discipline = " , self.discipline)
		print("Marks = " , self.marks)

	def avg(self):
		self.avg = sum(self.marks) / len(self.marks)
		print("Average = " , self.avg)

s1 = Student()
s1.setStu()
s1.getStu()
s1.avg()


