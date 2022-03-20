from tkinter import *

root=Tk()

root.geometry("500x500")

root.title("Hey This Is Title")

L1 = Label(text="Hey This Is A Label")
L1.pack()

L1 = Label(text="Hey This Is A Label")
L1.pack(side=LEFT)

L1 = Label(text="Hey This Is A Label")
L1.pack(side=BOTTOM)

L1 = Label(text="Hey This Is A Label")
L1.pack(side=RIGHT)

L1 = Label(text="Hey This Is A Label")
L1.pack(side=TOP)

root.mainloop()
