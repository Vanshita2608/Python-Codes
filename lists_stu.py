#student
#lists_stu.py
class Student:
	def setStu(self):
		self.id=input("Enter Id: ")
		self.name=input("Enter Name: ")
		self.dis=input("Enter Discipline: ")
		self.marks=[]
		n=int(input("Enter no. of subjects: "))
		for i in range(1,n+1):
			print("Enter marks of subject ",i , " : ")
			m=int(input())
			self.marks.append(m)
		print(self.marks)

	def getStu(self):
		print("\n\n____DETAILS OF THE STUDENT____")
		print("Id = ",self.id)
		print("Name = ",self.name)
		print("Discipline = ",self.dis)
		'''
		for i in self.marks:
			print(i)
		'''
	def avg(self):
		average=sum(self.marks)/len(self.marks)
		return average

s1=Student()
s1.setStu()
s1.getStu()
avg_marks=s1.avg()
print("Average of 3 subjects = ",avg_marks)