from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
root["bg"]="yellow"
L1 = Label(root, text="This Is A Entry Wight:")
L1.grid(row=1)

E1 = Entry(root)
E1.grid(row=1,column=2)

root.mainloop()
