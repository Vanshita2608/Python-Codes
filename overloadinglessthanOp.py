class Point:
	def __init__(self,x=0):
		self.x=x
	def __lt__(self,other):
		if(self.x<other.x):
			return True
		else:
			return False

p1=Point(1)
p2=Point(2)
p3=Point(3)

print(p1<p2)
print(p2<p3)
print(p1<p3)