from tkinter import *

root=Tk()

root.geometry("400x600")

root.title("Hey This Is Title")

Photo = PhotoImage(file="Photo2.png")

L = Label(image=Photo)
L.pack()

root.mainloop()

