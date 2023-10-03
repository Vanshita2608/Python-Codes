#class and object
#class_and_object.py

class BookStore:
	TotalBooks = 0
	def __init__(self,title,author,qty,price):
		print("Inside Constructor")
		self.title = title
		self.author = author
		self.qty = qty
		self.price = price
		BookStore.TotalBooks += 1
	def getBook(self):
		print("Title = " , self.title)
		print("Author = " , self.author)
		print("Quantity = " , self.qty)
		print("Price = " , self.price)
#modification in bookstore class
#develop a user defined function valuation() which displays the valuation of each book.
	def valuation(self):
		val = self.qty * self.price
		print("Valuation = " , val)
#also provide methods to update qty and price
	def update_qty(self):
		aq = int(input("\nEnter additional qty: "))
		self.qty = self.qty + aq
	def update_price(self):
		up = float(input("Enter increase % :"))
		self.price += self.price * 5/100             #0.05


B1 = BookStore("It Ends With Us!" , "Colleen Hoover" , 5 , 300)
print("Total Books = " , BookStore.TotalBooks)
B2 = BookStore("It Starts With Us!" , "Colleen Hoover" , 5 , 300)
print("Total Books = " , BookStore.TotalBooks)
print("\nBook1 Details: ")
B1.getBook()
B1.valuation()
B1.update_qty()
B1.update_price()
print("\nUpdated Values :")
B1.getBook()
B1.valuation()


print("\nBook2 Details: ")
B2.getBook()
B2.valuation()
B2.update_qty()
B2.update_price()
print("\nUpdated Values :")
B2.getBook()
B2.valuation()
