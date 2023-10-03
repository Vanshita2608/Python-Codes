#class and object
#class_and_object_ui.py


class BookStore:
	title = ""
	author = ""
	price = 0
	qty = 0 
	def setBook(self):
		print("WELCOME TO BOOK STORE")
		self.title = input("Enter book title: ")
		self.author = input("Enter author name: ")
		self.qty = int(input("Enter book qty: "))
		self.price = int(input("Enter book price: "))

	def getBook(self):
		print("Title = " , self.title)
		print("Author = " , self.author)
		print("Quantity = " , self.qty)
		print("Price = " , self.price)
		print("Total Price = " , self.price * self.qty)

bs = BookStore()
bs.setBook()
bs.getBook()