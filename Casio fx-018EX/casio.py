from tkinter import *
from casio_module import *

window = Tk()
window.geometry("350x550")
window.title("Casio Calculator Version 1.0")
window.configure(bg = "black")

def menu():
	greeting = Label(
		text = "Casio\nfx-018EX\nClassWiz",
		fg = "white",
		bg = "black",
		width = 40)
	greeting.config(
		anchor = "w",
		font=("Courier", 14)
		)
	greeting.pack()
	photo = PhotoImage(file = "image/casio.png")
	solar = Label(
		window,
		image = photo)
	solar.config(
		anchor = "e",
		borderwidth = 0,
		highlightthickness = 0)
	solar.photo = photo
	solar.pack()
	entry = Text(
		window,
		bg = "#d6d96a",
		fg = "black",
		height = 5,
		width = 40)
	entry.pack()
	button = Button(
		text = "0",
		width = 9,
		height = 2,
		bg = "white",
		fg = "black")
	button.pack()
	window.mainloop()


menu()