from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

F = Frame(root, bg="red", borderwidth=180)
F.pack(side=TOP,fill=X)

L = Label(F, text="This Is Frame")
L.pack(side=LEFT)

L1 = Label(F, text="This Is Frame")
L1.pack(side=RIGHT)

L2 = Label(F, text="This Is Frame")
L2.pack(side=BOTTOM)

L3 = Label(F, text="This Is Frame")
L3.pack(side=TOP)

root.mainloop()
