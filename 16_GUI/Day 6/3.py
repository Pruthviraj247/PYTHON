from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def Name():
    print("Hey My Name Is Anu")
def Study():
    print("Im Complete My MS(CS) in Taiwan")
def This():
    print("This Is A Laptop")
def Age():
    print("Never Ask A Woman For His Age ")
def City():
    print("This New York City")
#______________________________________________________________________________________________________________________#
B = Button(root, text="What Is Your Name",command=Name)
B1 = Button(root, text="What Is Your Education",command=Study)
B2 = Button(root, text="What Is This",command=This)
B3 = Button(root, text="What Is Your Age",command=Age)
B4 = Button(root, text="What Is Your City",command=City)
#______________________________________________________________________________________________________________________#
B.grid(row=1,column=1)
B1.grid(row=2,column=3)
B2.grid(row=3,column=4)
B3.grid(row=4,column=3)
B4.grid(row=5,column=1)
#______________________________________________________________________________________________________________________#
root.mainloop()
