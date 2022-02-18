from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("This Is A Title")

label = Label(text="Hey This Is A Label", fg="red", font=("arial", 15, "bold"))
label.pack()

root.mainloop()
