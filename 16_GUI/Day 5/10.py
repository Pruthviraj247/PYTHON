from tkinter import *

root=Tk()
root.title("Hey This Is Title")

Height = 500
Width = 500

root.geometry(f"{Height}x{Width}")

C = Canvas(root)
C.pack()

C.create_rectangle(31,5,800,400,fill="red")
root.mainloop()
