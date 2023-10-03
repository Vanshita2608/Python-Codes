#method overriding
#method_overriding.py

class Parent:
	def __init__(self):
		self.value = "Parent"
	def show(self):
		print(self.value)

class Child(Parent):
	def __init__(self):
		self.value = "Child"
	def show(self):
		print(self.value)

ob1 = Parent()
ob2 = Child()
ob1 = ob2
ob1.show()
#ob2.show()