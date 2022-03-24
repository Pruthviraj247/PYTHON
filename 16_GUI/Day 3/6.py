from tkinter import *

root = Tk()

root.geometry("900x900")

I1 = PhotoImage(file="Photo6.png")
I2 = PhotoImage(file="Photo7.png")
I3 = PhotoImage(file="Photo8.png")
I4 = PhotoImage(file="Photo9.png")


L1 = Label(root, image=I1)
L2 = Label(root, image=I2)
L3 = Label(root, image=I3)
L4 = Label(root, image=I4)


L1.place(x=20,y=5)
L2.place(x=470,y=5)
L3.place(x=470,y=410)
L4.place(x=20, y=410)

root.mainloop()
