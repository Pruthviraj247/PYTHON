from tkinter import *

root = Tk()

root.geometry("500x500")

root.title("Hey This Is Title")

# v = IntVar()
# v.set(0)

languages = [
    ("Python", 1),
    ("Java", 2),
    ("Rust", 3),
    ("Javascript", 4),
    ("Ruby", 5)

]


def ShowChoice():
    print(v.get())


L1 = Label(root, text="Choose your favourite programming language: ", font="comicsansms 10 bold")
L1.pack()

for language, val in languages:
    R1 = Radiobutton(root,
                     text=language,
                     padx=20,
                     # variable=v,
                     # command=ShowChoice,
                     value=val)
    R1.pack()

root.mainloop()
