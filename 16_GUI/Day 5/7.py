from tkinter import *

root=Tk()
root.title("Hey This Is Title")

Height = 500
Width = 500

root.geometry(f"{Height}x{Width}")

C = Canvas(root)
C.pack()

C.create_line(0,200,800,0)
root.mainloop()
