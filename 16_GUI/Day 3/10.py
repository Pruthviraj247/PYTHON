import pygame
from tkinter import *
root = Tk()
root.geometry("200x200")
pygame.init()
def play():
    pygame.mixer.music.load("../Day 3/Sound1.mp3")#Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
Button(root, text="Play", command=play).place(x=80,y=80)
root.mainloop()
