from tkinter import *
root = Tk()
root.geometry("600x600")
root.title("Welcome To Domino's")
root.configure(bg="aliceblue")


def sub():
    L2.config(text=clicked.get(),bg="aliceblue",fg="green", font=("arial", 10, "bold"))


L = Label(text="Welcome To Domino's",bg="aliceblue", fg="red", font=("arial", 15, "bold"))
L.place(x=200, y=5)

Pizza = [
    "Choice Your Pizza",
    "The Unthinkable Pizza Price: 499",
    "Veg Extravaganza Price: 299",
    "Mexican Green Wave Price: 899",
    "Chicken Dominator Price: 599",
    "Chicken Pepperoll Price: 459",
    "Chicken Flesta Price:299"
]

clicked = StringVar()
clicked.set("Choice Your Pizza")

Drop = OptionMenu(root,clicked,*Pizza)
Drop.place(x=230,y=50)

Ch = Checkbutton(root,text="Do You Want Cocola",bg="aliceblue",fg="red", font=("arial", 9, "bold"))
Ch.place(x=230,y=230)

Submit = Button(root, text="Order", command=sub)
Submit.place(x=260,y=250)

L2 = Label(root,text=" ")
L2.place(x=200,y=300)
root.mainloop()
