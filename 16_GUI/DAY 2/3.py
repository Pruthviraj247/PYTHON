from tkinter import *

root=Tk()

root.geometry("1100x500")

root.title("Hey This Is Title")

L1 = Label(text="Hey This Is A Label")
L1.grid(row=5, column=1)

L2 = Label(text="Hey This Is A Label")
L2.grid(row=4,column=2)

L3 = Label(text="Hey This Is A Label")
L3.grid(row=3, column=3)

L4 = Label(text="Hey This Is A Label")
L4.grid(row=2, column=4)

L5 = Label(text="Hey This Is A Label")
L5.grid(row=1, column=5)

L6 = Label(text="Hey This Is A Label")
L6.grid(row=1, column=6)

L7 = Label(text="Hey This Is A Label")
L7.grid(row=2,column=7)

L8 = Label(text="Hey This Is A Label")
L8.grid(row=3, column=8)

L9 = Label(text="Hey This Is A Label")
L9.grid(row=4, column=9)

L10 = Label(text="Hey This Is A Label")
L10.grid(row=5, column=10)

L11 = Label(root, text="Hey This Is A Label")
L11.grid(row=0,sticky="e")

root.mainloop()
