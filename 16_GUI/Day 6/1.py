from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Hey This Is Title")
#______________________________________________________________________________________________________________________#
def Bet():
    print("Yes This Button Working !")
#______________________________________________________________________________________________________________________#
B = Button(root,text="This Button Is Working ? ",command=Bet)
#______________________________________________________________________________________________________________________#
B.place(x=200,y=200)
#______________________________________________________________________________________________________________________#

root.mainloop()
