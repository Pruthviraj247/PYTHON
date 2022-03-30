from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

F = Frame(root, bg="red", borderwidth=8)
F.pack(side=TOP,fill=X)

L = Label(F, text="This Is Frame")
L.pack()

root.mainloop()
