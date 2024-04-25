## Button, Canvas, Checkbutton, Entry, Frame, Label

from tkinter import *
from tkinter import messagebox


## Membuat Button
top = Tk()

framebutt = Frame(top)
framebutt.pack()
def helloCallback():
    msg = messagebox.showinfo("Hello","Welcome!")
B = Button(framebutt, text = "Click Here", command=helloCallback())
B.pack()

# Membuat Canvas

framecan = Frame(top)
framecan.pack()

C = Canvas(framecan, bg='blue', height=250, width=300)
coord = 10,50,240,210
arc = C.create_arc(coord, start=0, extent = 150, fill='red')
line = C.create_line(10,10,200,200, fill='white')
C.pack()


## Membuat Checkbutton
framecheck = Frame(top)
framecheck.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top,text = 'basket', variable =CheckVar1, onvalue = 1, offvalue=0, height=5, width=20,)
C2 = Checkbutton(top,text = 'sepakbola', variable =CheckVar2, onvalue = 1, offvalue=0, height=5, width=20,)
C1.pack()
C2.pack()

## Membuat Entry

framentry = Frame(top)
framentry.pack()
L1 = Label(framentry, text="User Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side=RIGHT)


## Membuat Frame
frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text='red', fg='red')
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text='Brown', fg='brown')
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text='blue', fg='blue')
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text='black', fg='black')
blackbutton.pack(side=BOTTOM)

top.mainloop()

## Membuat Label
framelabel = Frame(top)
framelabel.pack()

var = StringVar()
label = Label(framelabel, textvariable=var, relief=RAISED)
var.set("Hellow, Welcome")
label.pack()
top.mainloop()

## JIKA MAU SATU SATU, HAPUS SAJA FRAME