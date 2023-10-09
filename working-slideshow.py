#!/bin/bash/python3

# import required modules
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk


# adjust window via Tkinter
root=tk.Tk()
root.attributes('-fullscreen' , True)
#root.geometry("1920x1080")

# adjust images via Pillow
clubRoom=Image.open("Desktop/slide_show.png")
becomeMember=Image.open("Desktop/slide_show_2.png")
interestedJoining=Image.open("Desktop/IEEE slides for pis (3).png")
whatAbout=Image.open("Desktop/IEEE slides for pis.png")
title=Image.open("Desktop/title.png")
barcodes=Image.open("Desktop/barcodes.png")
slide0=title.resize((1920,1080))
slide1=whatAbout.resize((1920, 1080))
slide2=clubRoom.resize((1920, 1080))
slide3=interestedJoining.resize((1920, 1080))
slide4=barcodes.resize((1920,1080))
slide5=becomeMember.resize((1920, 1080))



# loading the images into slideshow
img=ImageTk.PhotoImage(slide0)
img2=ImageTk.PhotoImage(slide1)
img3=ImageTk.PhotoImage(slide2)
img4=ImageTk.PhotoImage(slide3)
img5=ImageTk.PhotoImage(slide4)
img6=ImageTk.PhotoImage(slide5)



#img3=ImageTk.PhotoImage(Image.open("photo3.png"))

l=Label()
l.pack()



# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	root.bind('<q>', lambda e: root.destroy())
	global x
	if x == 7:
		x = 1
	if x == 1:
		l.config(image=img)
	elif x == 2:
		l.config(image=img2)
	elif x == 3:
                l.config(image=img3)
	elif x == 4:
                l.config(image=img4)
	elif x == 5:
                l.config(image=img5)
	elif x == 6:
                l.config(image=img6)

	x = x+1
	root.after(7000, move)

# calling the function

move()

root.mainloop()
