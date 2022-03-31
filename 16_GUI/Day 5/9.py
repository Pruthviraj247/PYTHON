from tkinter import *

root=Tk()
root.title("Hey This Is Title")

Height = 500
Width = 500

root.geometry(f"{Height}x{Width}")

C = Canvas(root)
C.pack()

C.create_line(0,0,800,400,fill="red")
C.create_line(0,800,400,0,fill="red")
C.create_line(800,400,0,0,fill="green")
C.create_line(0,0,400,800,fill="blue")

root.mainloop()
