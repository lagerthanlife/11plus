#! /usr/bin/env python2
#
# testing on simple algebra and area formulae for rectangles.
# use the basic turtle graphics!
# as well as the ubiquitous Tkinter of course.

import Tkinter
import turtle
from random import randint
from PIL import Image, ImageTk

top = Tkinter.Tk()


def nextQn():
    Turtle1.reset()
    Turtle1.hideturtle()
    Turtle1.speed('normal')
    Turtle2.reset()
    Turtle2.hideturtle()

    return False

def AskQn():
    quantity = randint(5,15)
    C.itemconfig(icons["Quantity1"], text="${qty}".format(qty=quantity))

    icons["melonQty1"] = C.create_text(200,-250, text = "$25", font = myFont)
    icons["melonQty2"] = C.create_text(-280,100, text = "2 x", font = myFont)
    icons["noMelons"] = C.create_text(-280,-250, text = "5 x", font = myFont)
    icons["Price"] = C.create_text(200,100, text = "?", font = myFont)

    return False

def showAns():
    return False


C = Tkinter.Canvas(top, width = 800, height = 800)
top.title("Template Quiz")
C.pack()

ts= turtle.TurtleScreen(C)

Turtle1 = turtle.RawTurtle(ts)
Turtle2 = turtle.RawTurtle(ts)
Turtle1.hideturtle()
Turtle2.hideturtle()

Turtle1.speed('fast')

quitButton = Tkinter.Button(top, text="Quit", command=top.quit)
quitButton.place(x=50,y=650)

nextButton = Tkinter.Button(top, text="Next", command=nextQn)
nextButton.place(x=130,y=650)

showButton = Tkinter.Button(top, text="Show Answer", command=showAns)
showButton.place(x=220,y=650)

icons={}
image = Image.open("img/melon.jpg")
image = image.resize((120,120), Image.ANTIALIAS)
photo_melon = ImageTk.PhotoImage(image)

image = Image.open("img/bluearrow.jpg")
image = image.resize((160,80), Image.ANTIALIAS)

right_arrow = ImageTk.PhotoImage(image)

image = image.rotate(270)
down_arrow = ImageTk.PhotoImage(image)

myFont = ("Helvetica", "24")

icons["melon"] = C.create_image(-170,-250,image= photo_melon)
icons["melon"] = C.create_image(-170,100,image= photo_melon)
icons["rightarrow"] = C.create_image(30,-250,image= right_arrow)
icons["Op1"] = C.create_image(-170,-80,image= down_arrow)
icons["Op2"] = C.create_image(200,-80,image= down_arrow)


icons["Price1"] = C.create_text(200,-250, text = "$25", font = myFont)
icons["Price2"] = C.create_text(200,100, text = "?", font = myFont)
icons["Quantity1"] = C.create_text(-280,-250, text = "5 x", font = myFont)
icons["Quantity2"] = C.create_text(-280,100, text = "2 x", font = myFont)

Price1 = Tkinter.StringVar()
Price2 = Tkinter.StringVar()
Quantity1 = Tkinter.StringVar()
Quantity2 = Tkinter.StringVar()

AskQn()
# w.set(width)
# h.set(height)

# C.postscript(file="testmelon.ps")
ts.bgcolor("white")

top.mainloop()



