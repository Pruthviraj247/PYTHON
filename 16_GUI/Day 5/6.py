from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")


F = Frame(root, bg="red", borderwidth=8,relief=FLAT)
F.pack(side=TOP,fill=X)

F2 = Frame(root, bg="plum", borderwidth=8, relief=RAISED)
F2.pack(side=BOTTOM,fill=X)

F1 = Frame(root, bg="hotpink", borderwidth=8, relief=SUNKEN)
F1.pack(side=LEFT,fill=Y)

F3 = Frame(root, bg="cyan", borderwidth=8, relief=GROOVE)
F3.pack(side=RIGHT,fill=Y)

F4= Frame(root, bg="cyan", borderwidth=12, relief=RIDGE)
F4.place(x=170,y=50)

L = Label(F1, text="This Is RAISED Relief")
L.pack()

L1 = Label(F, text="This Is FLAT Relief")
L1.pack()

L2 = Label(F3, text="This Is SUNKEN Relief")
L2.pack()

L3 = Label(F2, text="This Is GROOVE Relief")
L3.pack()

L4 = Label(F4, text="This Is RIDGE Relief")
L4.pack()

root.mainloop()
