#Python 3 Edition Version
import tkinter
from tkinter import messagebox   #This import messagebox via tkinter
tkinter.messagebox               #Imports a Message GUI Module
top = tkinter.Tk()               #Add The GUI window of tkinter
top.mainloop()                   #Code to add widgets will go here...

#Message tkinter
top = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox .showinfo("GO AWAY") #What the box will show

B = tkinter.Button(top, text= "go away", command = helloCallBack)  #w = Button ( master, option=value, ... ) and the options...
B.pack()                        #Puts the b Variable into a block widget
top.mainloop()                  #Stop program
