from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("1000x700")

I1 = PhotoImage(file="Photo6.png")

L1 = Label(root, image=I1)
L1.place(x=20,y=5)

image = Image.open("Photo3.jpeg")
photo = ImageTk.PhotoImage(image)

L = Label(image=photo)
L.place(x=460,y=5)

root.mainloop()
