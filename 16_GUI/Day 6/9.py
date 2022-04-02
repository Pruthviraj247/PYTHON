from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def Val():
    print(C9.get(),C8.get(),C7.get(),C6.get(),C0.get())
#______________________________________________________________________________________________________________________#
C9 = IntVar()
C8 = IntVar()
C7 = IntVar()
C6 = IntVar()
C0 = IntVar()
#______________________________________________________________________________________________________________________#
C1 = Checkbutton(root,text="Anu Is Best In World", variable=C9)
C2 = Checkbutton(root,text="Disha Computer Is Best In Class", variable=C8)
C3 = Checkbutton(root,text="Lenovo Is Laptop Company", variable=C7)
C4 = Checkbutton(root,text="Python Is Wast Language", variable=C6)
C5 = Checkbutton(root,text="Hey Computer How Are You", variable=C0)
S1 = Button(root, text="Submit",command=Val)
#______________________________________________________________________________________________________________________#
C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
S1.pack()
#______________________________________________________________________________________________________________________#
root.mainloop()
