from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Morning World")
B = Button(top, text ="Klik Here", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()