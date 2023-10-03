class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def getPerson(self):
		print("Name=",self.name)
		print("Age=",self.age)

class Sports:
	def __init__(self):
		self.spoints=0

	def get_spoints(self):
		self.spoints=0
		choice=input("Have you participated in Sports (y/n)= ")
		if(choice=='y' or choice=="yes"):
			level=input("Enter level 'N' for National 'S' for state and 'D' for district = ")
			if(level=='N' or level=='n'):
				self.spoints=25
			elif(level=='S' or level=='s'):
				self.spoints=15
			elif(level=='D' or level=='d'):
				self.spoints=5
			else:
				self.spoints=0


class Student(Person,Sports):
	def __init__(self,name,age,Id,sem,m1,m2):
		super().__init__(name,age)
		self.Id=Id
		self.sem=sem
		self.m1=m1
		self.m2=m2

	def tot_marks(self):
		self.get_spoints()
		total=self.m1+self.m2+self.spoints
		print("Total marks with Sports points = ",total)
		avg=total/2
		print("Avearge marks = ",avg)

	def getStudent(self):
		super().getPerson()
		print("ID=",self.Id)
		print("Semester=",self.sem)
		print("Marks 1=",self.m1)
		print("Marks 2=",self.m2)
		self.tot_marks()

s1=Student("Swayam",30,1221,3,30,40)
s1.getStudent()



