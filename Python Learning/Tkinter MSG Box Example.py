#Python 3 Edition Version
import tkinter
from tkinter import messagebox   #This import messagebox via tkinter
tkinter.messagebox               #Imports a Message GUI Module

#Message tkinter
top = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox .showinfo( "Hello Python", "Hello World") #What the box will show

B = tkinter.Button(top, text ="Hello", command = helloCallBack)  #w = Button ( master, option=value, ... ) and the options...
B.pack()                        #Puts the b Variable into a block widget
top.mainloop()                  #Stop program
