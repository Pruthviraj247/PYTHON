from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def Value():
    print(E9.get(),"\n",E8.get(),"\n",E7.get(),"\n",E6.get(),"\n",C1.get(),"\n")
#______________________________________________________________________________________________________________________#
C1 = IntVar()
#______________________________________________________________________________________________________________________#
L1 = Label(root,text="Enter Your Full Name")
L2 = Label(root,text="Enter Your Education")
L3 = Label(root,text="Enter Your Phone Number")
L4 = Label(root,text="Enter Your Mail Id")
E9 = Entry(root)
E8 = Entry(root)
E7 = Entry(root)
E6 = Entry(root)
C9 = Checkbutton(root,text="Are You Visiting Our Collage ?",variable=C1)
B1 = Button(root,text="Submit",command=Value)
#______________________________________________________________________________________________________________________#
L1.grid(row=1,column=1)
L2.grid(row=2,column=1)
L3.grid(row=3,column=1)
L4.grid(row=4,column=1)
E9.grid(row=1,column=2)
E8.grid(row=2,column=2)
E7.grid(row=3,column=2)
E6.grid(row=4,column=2)
C9.grid(row=5,column=2)
B1.grid(row=6,column=2)
#______________________________________________________________________________________________________________________#
#______________________________________________________________________________________________________________________#


root.mainloop()
