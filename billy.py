from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Billy Builder")

window.geometry('1980x1080')

lbl = Label(window, text="Select your desired bottle:")

lbl.grid(column=0, row=0)

c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
lbl = Label(window, text="choose your downstem:")

lbl.grid(column=0, row=4)







window.mainloop()
