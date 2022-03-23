from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x400")
root.title("Hey This Is Title")

image = Image.open("Photo1.jpg")
photo = ImageTk.PhotoImage(image)

L = Label(image=photo)
L.pack()

root.mainloop()
