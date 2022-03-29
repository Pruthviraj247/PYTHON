from tkinter import *

root= Tk()
root.geometry("500x500")
root.title("Admission Form")

Label(root, text="Admission Form", font=("arial", 17)).pack()
Label(root, text="Enter Your Name:").place(x=5, y=40)
Label(root, text="Enter Your Address:").place(x=5, y=80)
Label(root, text="Enter Your Phone Number:").place(x=5, y=120)
Label(root, text="Enter Your Email Id:").place(x=5, y=160)
Checkbutton(text="Do You Visit To Collage For More Information ?").place(x=5, y=190)
Entry(root).place(x=160, y=40)
Entry(root).place(x=160, y=80)
Entry(root).place(x=160, y=120)
Entry(root).place(x=160, y=160)
Button(root, text="Submit").place(x=200, y=220)

root.mainloop()
