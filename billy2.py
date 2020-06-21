from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Billy Builder")

window.geometry('1980x1080')

lbl = Label(window, text="Select your desired bottle:")

lbl.grid(column=0, row=0)
master = Tk()
print ("Choose your bottle")
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=1, sticky=W)
mainloop()
