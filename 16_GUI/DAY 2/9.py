from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("This Is A Title")

L = Label(root, text="Anu is A Very Good Programmer\n Sara Is A Master Mind\n Disha Computer is A World's Best "
                     "Institute \n Python is A Worst Language", bg="pink", fg="black", padx=55, pady=55, font="comicsansms 15 bold",
          borderwidth=12, relief=SUNKEN)

L.pack(side=TOP, fill=X)

root.mainloop()
