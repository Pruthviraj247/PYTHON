from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

L1 = Label(root, text="This Is More Entry:",font=("arial 20 bold"))
L2 = Label(root, text="This Is More Entry:")
L3 = Label(root, text="This Is More Entry:")
L4 = Label(root, text="This Is More Entry:")
L5 = Label(root, text="This Is More Entry:")
#___________________________________________#
E1 = Entry(root,font="20")
E2 = Entry(root)
E3 = Entry(root)
E4 = Entry(root)
E5 = Entry(root)
#___________________________________________#
L1.grid(row=1)
L2.grid(row=2)
L3.grid(row=3)
L4.grid(row=4)
L5.grid(row=5)
#___________________________________________#
E1.grid(row=1,column=1)
E2.grid(row=2,column=1)
E3.grid(row=3,column=1)
E4.grid(row=4,column=1)
E5.grid(row=5,column=1)

root.mainloop()
