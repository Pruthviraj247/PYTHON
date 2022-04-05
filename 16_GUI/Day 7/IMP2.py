from tkinter import *

root=Tk()
root.geometry("700x700")
root.title("Admission Form")
#______________________________________________________________________________________________________________________#

#______________________________________________________________________________________________________________________#
L1 = Label(root, text="University Admission Form", font="ComicsansMS 15 bold",fg="cadetBlue")
L2 = Label(root, text="Please Fill In The From Carefully: ",font="ComicsansMS 13 bold",fg="Darksalmon")
L3 = Label(root, text="Name",font="ComicsansMS 15 bold",fg="crimson")
L4 = Label(root, text="First Name",font="ComicsansMS 11 bold",fg="black")
L5 = Label(root, text="Middle Name",font="ComicsansMS 11 bold",fg="black")
L6 = Label(root, text="Last Name",font="ComicsansMS 11 bold",fg="black")
L7 = Label(root, text="Gender",font="ComicsansMS 15 bold",fg="crimson")
L8 = Label(root, text="Date of Birth",font="ComicsansMS 15 bold",fg="crimson")
#______________________________________________________________________________________________________________________#
E1 = Entry(root)
E2 = Entry(root)
E3 = Entry(root)
#______________________________________________________________________________________________________________________#
Gender = [("Male",2)]
G = IntVar()
G.set(0)
for Gen, Val in  Gender:
    R =  Radiobutton(root,text=Gen,variable=G,font="ComicsansMS 11 bold",fg="black")
Gender1 = [("Female",2)]
G1 = IntVar()
G1.set(0)
for Gen1, Val1 in  Gender1:
    R1 = Radiobutton(root,text=Gen1,variable=G1,font="ComicsansMS 11 bold",fg="black")

Gender2 = [("Other",2)]
G2 = IntVar()
G2.set(0)
for Gen2, Val2 in  Gender2:
    R2 = Radiobutton(root,text=Gen2,variable=G2,font="ComicsansMS 11 bold",fg="black")
#______________________________________________________________________________________________________________________#
E4 = Entry(root, width=30)
# E5 = Entry(root, width=30)
E6 = Entry
#______________________________________________________________________________________________________________________#
L1.pack()
L2.place(x=20,y=50)
L3.place(x=320,y=80)
L4.place(x=80,y=130)
L5.place(x=290,y=130)
L6.place(x=500,y=130)
L7.place(x=320,y=160)
L8.place(x=300,y=230)
#______________________________________________________________________________________________________________________#
E1.place(x=80,y=110)
E2.place(x=290,y=110)
E3.place(x=500,y=110)
E4.place(x=270,y=260)
#______________________________________________________________________________________________________________________#
R.place(x=80,y=190)
R1.place(x=290,y=190)
R2.place(x=500,y=190)
#______________________________________________________________________________________________________________________#
#______________________________________________________________________________________________________________________#
root.mainloop()
