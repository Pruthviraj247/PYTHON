from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

F = Frame(root, bg="red", borderwidth=80)
F.pack(side=LEFT,fill=Y)

L = Label(F, text="This Is Frame")
L1 = Label(F, text="Day 1 ^")
L2 = Label(F, text="Day 2 ^")
L.pack()
L1.pack()
L2.pack()
root.mainloop()

