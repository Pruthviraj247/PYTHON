from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
def val():
    print(E.get())
#______________________________________________________________________________________________________________________#
L = Label(root, text="Enter Your Name")
E = Entry(root)
B = Button(root, text="Submit",command=val)
#______________________________________________________________________________________________________________________#
L.grid(row=1,column=1)
E.grid(row=1,column=2)
B.grid(row=1,column=3)
#______________________________________________________________________________________________________________________#

root.mainloop()
