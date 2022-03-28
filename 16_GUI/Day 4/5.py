from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
root["bg"]="gold"
languages = [
    ("Python", 1),
    ("Java", 2),
    ("Rust", 3),
    ("Javascript", 4),
    ("Ruby", 5)
]
L1 = Label(root, text="Choose your favourite programming language: ",bg="gold", font="comicsansms 10 bold")
L1.pack()

for language, val in languages:
    R1 = Radiobutton(root, text=language, value=val,bg="gold")
    R1.pack()

root.mainloop()
