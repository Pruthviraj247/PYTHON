from tkinter import *

root = Tk()
root.geometry("944x444")

def values():
    print(f"{E1.get(),E2.get(),E3.get(),E4.get(),E5.get()}")


    with open("record.txt", "a") as f:
        f.write(f"{E1.get(),E2.get(),E3.get(),E4.get(),E5.get()}\n")

label = Label(root, text="Addmission Form", font="comicsansms 19 bold")
label.grid(row=0, column=4)

Name = Label(root, text="Name")
Name.grid(row=1,column=0)

No = Label(root, text="phone Number")
No.grid(row=2,column=0)

Eu = Label(root, text="Education")
Eu.grid(row=3,column=0)

per = Label(root, text="Percentage")
per.grid(row=4,column=0)

E1 = StringVar()
E2 = StringVar()
E3 = StringVar()
E4 = StringVar()
E5 = IntVar()



enter = Entry(root, textvariable=E1)
enter.grid(row=1,column=2)

Phenter = Entry(root, textvariable=E2)
Phenter.grid(row=2,column=2)

Euenter = Entry(root, textvariable=E3)
Euenter.grid(row=3,column=2)

Perentery = Entry(root, textvariable=E4)
Perentery.grid(row=4,column=2)

Chack = Checkbutton(root, text="Are Visiting Our Collage", variable=E5)
Chack.grid(row=5,column=2)

b= Button(root, text="Submit" , command=values)
b.grid(row=6,column=2)

root.mainloop()
