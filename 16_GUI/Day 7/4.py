from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def ShowChoice():
    Value = v.get()
    if Value == 1:
        print("Customer Choose Python Language")
    elif Value == 2:
        print("Customer Choose Java Language")
    elif Value == 3:
        print("Customer Choose Rust Language")
    elif Value == 4:
        print("Customer Choose Javascript Language")
    elif Value == 5:
        print("Customer Choose Ruby Language")
#______________________________________________________________________________________________________________________#

languages = [
    ("Python", 1),
    ("Java", 2),
    ("Rust", 3),
    ("Javascript", 4),
    ("Ruby", 5)
]
#______________________________________________________________________________________________________________________#
L1 = Label(root, text="Choose your favourite programming language: ", font="comicsansms 10 bold")
B = Button(root, text="Submit Your Choose",command=ShowChoice)
#______________________________________________________________________________________________________________________#
v = IntVar()
#______________________________________________________________________________________________________________________#
v.set(1)
#______________________________________________________________________________________________________________________#
for language, val in languages:
    R1 = Radiobutton(root,text=language,variable=v,value=val)
    R1.pack()
#______________________________________________________________________________________________________________________#
L1.pack()
B.pack()
#______________________________________________________________________________________________________________________#
root.mainloop()
