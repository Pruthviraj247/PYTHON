from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("450x600")
root.title("Hey This Is Title")

image = Image.open("Photo3.jpeg")
photo = ImageTk.PhotoImage(image)

L = Label(image=photo)
L.pack()

root.mainloop()
