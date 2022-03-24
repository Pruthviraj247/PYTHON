from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Hey This Is A Title")
root.geometry("1000x700")
root.iconbitmap('Photo4.ico')

I1 = PhotoImage(file="Photo6.png")

L1 = Label(root, image=I1)
L1.place(x=20, y=5)

image = Image.open("Photo3.jpeg")
photo = ImageTk.PhotoImage(image)

L2 = Label(image=photo)
L2.place(x=460, y=5)

image1 = Image.open("Photo1.jpg")
photo1 = ImageTk.PhotoImage(image1)

L3 = Label(image=photo1)
L3.place(x=20, y=410)

image2 = Image.open("Photo5.jfif")
photo2 = ImageTk.PhotoImage(image2)

L4 = Label(image=photo2)
L4.place(x=460, y=410)

root.mainloop()
