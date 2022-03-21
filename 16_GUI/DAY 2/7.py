from tkinter import *

root=Tk()

root.geometry("350x350")

root.title("Hey This Is Title")

L1 = Label(root, text="Hey Welcome Come To Label", bg="red")
L1.pack(side=TOP,fill=X)

L1 = Label(root, text="Hey Welcome Come To Label", bg="blue")
L1.pack(side=TOP,fill=X,padx=55)

L1 = Label(root, text="Hey Welcome Come To Label", bg="pink")
L1.pack(side=TOP,fill=X)

L1 = Label(root, text="Hey Welcome Come To Label", bg="green")
L1.pack(side=TOP,fill=X,pady=55)

L1 = Label(root, text="Hey Welcome Come To Label", bg="tan")
L1.pack(side=TOP,fill=X)

root.mainloop()
