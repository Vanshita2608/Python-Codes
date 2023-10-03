class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __str__(self):
		return "({0},{1})".format(self.x,self.y)

	def __add__(self,other):
		p=Point()
		p.x=self.x+other.x
		p.y=self.y+other.y 
		return (p)
		
p1=Point(2,3)
p2=Point(4,5)
p3=p1+p2
print(p3)