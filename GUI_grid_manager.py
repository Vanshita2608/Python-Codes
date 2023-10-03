#GUI_grid_manager.py

from tkinter import *  

master = Tk()  

l1 = Label(master, text = "First:")
l2 = Label(master, text = "Second:")
l3 = Label(master, text = "Result:") 
 
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
l3.grid(row = 2, column = 0, sticky = W, pady = 2)

e1 = Entry(master)
e2 = Entry(master) 
e3 = Entry(master)

e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
e3.grid(row = 2, column = 1, pady = 2)

bttn1 = Button(master, text = "Result", command = "add") 
bttn2 = Button(master, text = "Clear", command = "clear")
bttn1.grid(row = 3, column = 0, sticky = W, pady = 2)
bttn1.grid(row = 3, column = 1, sticky = W, pady = 2)
bttn1.grid(row = 3, column = 1, pady = 2)
bttn2.grid(row = 3, column = 1, pady = 2)

e1.delete(0, END)
mainloop()