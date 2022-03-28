from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Checkbutton")

C1 = Checkbutton(root, text="Do You Know How To Code")
C1.place(x=160, y=20)

C2 = Checkbutton(root, text="Anu Is World's Best Coder")
C2.place(x=160, y=50)

C3 = Checkbutton(root, text="Anu's Work Is Inevitable")
C3.place(x=160, y=80)

B1 = Button(root, text="Submit")
B1.place(x=160, y=110)

root.mainloop()
