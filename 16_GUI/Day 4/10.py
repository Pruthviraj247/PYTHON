from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

Pizza = [
    "Choice The Correct Sentence",
    "Disha Computer Is The World's Best Institute",
    "Anu Is The Best Programmer In The World",
    "Lenovo Is A Laptop Company",
    "Python Is A Worst Language"
]

clicked = StringVar()
clicked.set("Choice The Correct Sentence")

Drop = OptionMenu(root, clicked, *Pizza)
Drop.place(x=150, y=50)


root.mainloop()
