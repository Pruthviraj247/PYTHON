from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def val():
    print("Yes Anu Is Always Best In World")
#______________________________________________________________________________________________________________________#
CC = IntVar()
#______________________________________________________________________________________________________________________#
C = Checkbutton(root, text="Anu Is The Best In World", variable=CC)
B = Button(root, text="Submit", command=val)
#______________________________________________________________________________________________________________________#
C.place(x=170,y=200)
B.place(x=170,y=230)
#______________________________________________________________________________________________________________________#
root.mainloop()
