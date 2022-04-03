from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def val():
    Taking_Value = CC.get()
    if Taking_Value == 1:
        print("Yes Customer Is Coming Disha Computer")
    else:
        print("Customer Is Not Coming To Computer Class")

    with open("Checkbutton.txt","a") as x:
        x.write(f"{CC.get()}\n")
#______________________________________________________________________________________________________________________#
CC = IntVar()
#______________________________________________________________________________________________________________________#
C = Checkbutton(root, text="Do You Come To Disha Computer ? ", variable=CC)
B = Button(root, text="Submit", command=val)
#______________________________________________________________________________________________________________________#
C.place(x=170, y=200)
B.place(x=170, y=230)
#______________________________________________________________________________________________________________________#
root.mainloop()
