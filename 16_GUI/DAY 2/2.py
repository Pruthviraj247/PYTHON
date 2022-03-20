from tkinter import *

root=Tk()

root.geometry("500x500")

root.title("Hey This Is Title")

L1 = Label(text="Hey This Is A Label")
L1.pack()

L2 = Label(text="Hey This Is A Label")
L2.pack(anchor=NW)

L3 = Label(text="Hey This Is A Label")
L3.pack(anchor=N)

L4 = Label(text="Hey This Is A Label")
L4.pack(anchor=NE)

L5 = Label(text="Hey This Is A Label")
L5.pack(anchor=W)

L6 = Label(text="Hey This Is A Label")
L6.pack(anchor=CENTER)

L7 = Label(text="Hey This Is A Label")
L7.pack(anchor=E)

L8 = Label(text="Hey This Is A Label")
L8.pack(anchor=SW)

L9 = Label(text="Hey This Is A Label")
L9.pack(anchor=S)

L10 = Label(text="Hey This Is A Label")
L10.pack(anchor=SE)

root.mainloop()
