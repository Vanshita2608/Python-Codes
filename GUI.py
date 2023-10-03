#GUI
#GUI.py

'''
from tkinter import *
window = Tk()
window.geometry("700x350")
window.title("Welcome to Demo GUI")
window.mainloop()
'''

'''
from tkinter import * 
#from tkinter.ttk import *
window = Tk()
window.title("Label Demo")
label = Label(window, text ="LABEL1").pack()
bttn1 = Button(window, text = "BUTTON1")
bttn1.pack()
txt1 = Entry(window, text = "Text1")
txt1.pack()
window.mainloop()
'''

'''
import tkinter as tk
window = tk.Tk()
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()
frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()
frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()
window.mainloop()
'''

'''
import tkinter as tk
window = tk.Tk()
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)
label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)
window.mainloop()
'''

'''
from tkinter import *
# Create a window object
window = Tk()
window.title("Key Event Window")
# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
# Run the event loop
window.mainloop()
'''

'''
from tkinter import *
# Create a window object
window = Tk()
window.title("Key Event Window")
# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
#Handling button click event
def handle_click(event):
    print("The button was clicked!")
button = Button(window,text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)
# Run the event loop
window.mainloop()
'''

'''
from tkinter import * 
from tkinter.ttk import *
window = Tk()
window.geometry("400x300")
window.title("Label Demo")
label = Label(window, text ="LABEL1")
bttn1 = Button(window, text = "BUTTON1")
bttn1.pack()
txt1 = Entry(window, text = "ENTRY1")
#Setting Default Text of Entry Widget
txt1.insert(0, "This is the default text")
txt1.pack()
label.pack()
# OR
"""
text = StringVar()
text.set("This is the default text")
textBox = Entry(window,textvariable = text)
textBox.pack()
"""
txt1.pack()
#Getting label text
print(label.cget("text"))
print(label["text"])

# Setting Button text
bttn1["text"]="My Button"
print(bttn1["text"])
#label.pack(); #pack() method is to be invoked at the last
#Getting entry text
print("Entry Text=",txt1.get())
window.mainloop()
'''


from tkinter import *
def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = txt_temp.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
window = Tk()
window.title("Temperature Converter")
frm_entry = Frame(master=window)
txt_temp = Entry(master=frm_entry, width=10)
lbl_temp = Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
txt_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
btn_convert = Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
#frm_entry.pack()
window.mainloop()
