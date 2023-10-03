class BookStore:
	TotalBooks=0
	def __init__(self,title,author,qty,price):
		print("Welcome to __init__() constructor")
		self.title=title
		self.qty=qty
		self.author=author
		self.price=price
	def getBook(self):
		print("Title=",self.title)
		print("Author=",self.author)
		print("Quantity=",self.qty)
		print("Price=",self.price)
		BookStore.TotalBooks+=1

	'''def valuation(self):
		return self.qty*self.price'''

	def update_qty(self):
		aq=int(input("Enter additional quantity="))
		self.qty=self.qty+aq

	def update_price(self):
		incrp=float(input("Enter increase in % ="))
		self.price+=self.price*(incrp/100)
		 
B1=BookStore("Python","AndrewNG",20,350)
B1.getBook()
print("Total Books=",BookStore.TotalBooks)
B1.update_qty()
B1.getBook()
B1.update_price()
B1.getBook()

