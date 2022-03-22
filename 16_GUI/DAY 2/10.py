from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("This Is A Title")

L = Label(root, text="Anu is A Very Bad Programmer\n Sara Is A Pro Player\n Disha Computer is A World's Best "
                     "Institute \n Python is A Best Language", bg="pink", fg="black", padx=55, pady=55, font="comicsansms 15 bold",
          borderwidth=12, relief=SUNKEN)

L.pack(side=TOP, fill=X, padx=50, pady=50)

L1 = Label(root, text="Komal is A Very Good Programmer\n Sara Is A Pro player\n Disha Computer is A World's Best "
                     "Institute \n Java is A Worst Language", bg="pink", fg="black", padx=55, pady=55, font="comicsansms 15 bold",
           borderwidth=12, relief=SUNKEN)

L1.pack(fill=X, padx=50, pady=50)


root.mainloop()
