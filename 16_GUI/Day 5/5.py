from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

F = Frame(root, bg="red", borderwidth=8)
F.pack(side=TOP,fill=X)

F2 = Frame(root, bg="plum", borderwidth=8)
F2.pack(side=BOTTOM,fill=X)

F1 = Frame(root, bg="pink", borderwidth=8)
F1.pack(side=LEFT,fill=Y)

F3 = Frame(root, bg="cyan", borderwidth=8)
F3.pack(side=RIGHT,fill=Y)

L = Label(F, text="This Is Top Frame")
L.pack()

L1 = Label(F1, text="This Is LEFT Frame")
L1.pack()

L2 = Label(F3, text="This Is RIGHT Frame")
L2.pack()

L3 = Label(F2, text="This Is BOTTOM Frame")
L3.pack()

root.mainloop()
