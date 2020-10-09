from tkinter import *
import pygame
from pygame.locals import *
import sys
import os

top = Tk()
pygame.mixer.init()

# Functions
def Test_def():
    print("Test Worked")

def Bt1_sound():
    pygame.mixer.music.load('sounds/sound1.mp3')
    pygame.mixer.music.play(0)

def Bt2_sound():
    pygame.mixer.music.load('sounds/sound2.mp3')
    pygame.mixer.music.play(0)

def Bt3_sound():
    pygame.mixer.music.load('sounds/sound3.mp3')
    pygame.mixer.music.play(0)

def Stop_Sounds():
    pygame.mixer.music.stop()

# Widget Code
Test = Button(top, text="test", command=Test_def)

Bt1 = Button(top, bg="gray70",width=30, height=5, text="Sound 1", command=Bt1_sound)
Bt2 = Button(top, bg="gray70",width=30, height=5, text="Sound 2", command=Bt2_sound)
Bt3 = Button(top, bg="gray70",width=30, height=5, text="Sound 3", command=Bt3_sound, state=DISABLED)
Stop = Button(top, bg="gray70",width=20, height=3, text="Stop Sounds", command=Stop_Sounds)

Footer = Label(top, bg="gray", height=15, text="Developer: Leo Power\nGitHub: https://github.com/powerthecoder\nWebsite: https://powerthecoder.xyz")


# Widget Formating
Bt1.pack()
Bt2.pack()
Bt3.pack()
Stop.pack()
Footer.pack()

# Required Code
top.title("SoundBoard    |    Leo Power")
top.geometry("500x500")
top.configure(bg="gray")
top.mainloop()