from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Admission Form")
#_________________________________________________#
Label(text="Admission From",font=("arial 15 bold")).pack()
Label(text="Enter Your Full Name",font=("arial 12 bold")).place(x=5, y=40)
Label(text="Enter Your Phone Number",font=("arial 12 bold")).place(x=5,y=70)
Label(text="Enter Your Email Id",font=("arial 12 bold")).place(x=5,y=100)
Label(text="Enter Your Address", font="arial 12 bold").place(x=5, y=130)
#_____________________________________________________________________________#
Entry().place(x=250,y=40)
Entry().place(x=250,y=70)
Entry().place(x=250,y=100)
Entry().place(x=250,y=130)
#__________________________________________________________________________________#
Checkbutton(text="Are You Come To Collage ?",font=("arial 12 bold")).place(x=5,y=160)
#__________________________________________________________________________________#
Button(text="Submit",command=quit).place(x=200,y=180)
#___________________________________________________________________________________#
root.mainloop()
