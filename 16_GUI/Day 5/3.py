from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

F = Frame(root, bg="red", borderwidth=8)
F.pack(side=TOP,fill=X)

L = Label(F, text="This Is Frame")
L.pack()

L1 = Label(F, text="This Is Frame")
L1.pack()

L2 = Label(F, text="This Is Frame")
L2.pack()

L3 = Label(F, text="This Is Frame")
L3.pack()

root.mainloop()
