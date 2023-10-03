#student
#studentCno2.py
class Student:
	def setStu(self):
		self.id=input("Enter Id ")
		self.name=input("Enter Name ")
		self.dis=input("Enter Discipline ")
		self.m1=int(input("Enter marks of 1st subject "))
		self.m2=int(input("Enter marks of 2nd subject "))
		self.m3=int(input("Enter marks of 3rd subject "))
	def getStu(self):
		print("Id = ",self.id)
		print("Name = ",self.name)
		print("Discipline = ",self.dis)
		print("Marks of subject 1 = ",self.m1)
		print("Marks of subject 2 = ",self.m2)
		print("Marks of subject 3 = ",self.m3)
	def avg(self):
		average=(self.m1+self.m2+self.m3)/3
		return average
s1=Student()
s1.setStu()
s1.getStu()
avg_marks=s1.avg()
print("Average of 3 subjects = ",avg_marks)