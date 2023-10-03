#built in attributes
#built_in_attributes.py

class Demo:
	"""Demo Class"""
	def __init__(self,a,b):
		#print("Inside constructor")
		self.a = a
		self.b = b
	def __del__(self):
		print("Object Destroyed")
d1 = Demo(2,3)
d2 = Demo(5,6)
#print(Demo.__doc__)
#print(Demo.__name__)
#print(Demo.__dict__)
#print(d1.__dict__)
#print(Demo.__module__)
#print(Demo.__bases__)



#destructor concept and built-in concept ek me hi hai...just remove the comments and use