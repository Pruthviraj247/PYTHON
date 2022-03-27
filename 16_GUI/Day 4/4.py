from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")

B1 = Button(root,text="This Is More Button's",bg="lime")
B2 = Button(root,text="This Is More Button's",bg="yellow", fg="red")
B3 = Button(root,text="This Is More Button's",bg="wheat", fg="teal", font=("arial", 10, "bold"))
B4 = Button(root,text="This Is More Button's",borderwidth=8,bg="grey")
B5 = Button(root,text="This Is More Button's",borderwidth=8,bg="grey",relief=SUNKEN)
#___________________________________________#
B1.place(x=200,y=50)
B2.place(x=200,y=100)
B3.place(x=200,y=150)
B4.place(x=200,y=200)
B5.place(x=200,y=250)

root.mainloop()
