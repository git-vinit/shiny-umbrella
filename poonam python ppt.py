#mutiplewidgetscal.py
from tkinter import *

def addm( ):
 print("The sum of 5+2 is" ,5+2)

def subm( ):
 print("The sub of 5-2 is",5-2)

def multm( ):
 print("The mult of 5*2 is",5*2)

def divm( ):
 print("The div of 5/2 is" ,5/2)

win = Frame()
win.pack( )

Label(win, text="Arithmatic Calculator").pack(side=TOP)

Button(win, text="Add", command=addm).pack(side=LEFT)
Button(win, text="Sub", command=subm).pack(side=LEFT)
Button(win, text="Mult", command=multm).pack(side=LEFT)
Button(win, text="Div", command=divm).pack(side=LEFT)
Button(win, text="Quit", command=win.quit).pack(side=RIGHT)

win.mainloop( )
