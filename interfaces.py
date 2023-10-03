#interface 
#interfaces.py

print("\n\n_____INFORMAL INTERFACE_____")
class Fruits:
	def __init__(self,ele):
		self.__ele = ele 
	def __contains__(self,ele):
		return ele in self.__ele
	def __len__(self):
		return len(self.__ele)
	def __iter__(self):
		return self

F_list = Fruits(['Apple' , 'Mango' , 'Banana'])
print(len(F_list))
print("Apple" in F_list)
print("Mango" in F_list)
print("Orange" not in F_list)


print("\n\n_____FORMAL INTERFACE_____")
import abc
class Figure(abc.ABC):
	def area(self):
		pass

class Rectangle(Figure):
	def __init__(self,d1,d2):
		self.d1 = d1
		self.d2 = d2
	def area(self):
		return self.d1 * self.d2
	def getDim(self):
		print("Length = " , self.d1)
		print("Breadth = " , self.d2)

r = Rectangle(2,5)
r.getDim()
print("Area = " , r.area())